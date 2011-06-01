from django.db.models import Avg, Max, Min, Count, Sum
from django.template.defaultfilters import floatformat
import re
import urllib2
import string
from decimal import *

def dec_or_zero(maybe_dec, default):
    '''
    Define a function which determines whether a given variable evaluates as an decimal with a sane default.
    Input: maybe_dec, a possible decimal.
    Input: default, a default integer, e.g., 0.0.
    Output: Your possible integer as an decimal or your default.
    '''
    # Make sure at least the default is an integer.
    try:
        getcontext().prec = 1
        Decimal(default)
    except:
        raise ValueError('Your default is not an integer.')
        
    # Try to cast our possible integer as an integer.
    try:
        getcontext().prec = 1
        default = Decimal(maybe_dec)
    except ValueError, TypeError:
        pass
        
    # Return either the default or our properly int()'ed integer.
    return default
    

def int_or_zero(maybe_int, default):
    '''
    Define a function which determines whether a given variable evaluates as an int with a sane default.
    Input: maybe_int, a possible integer.
    Input: default, a default integer, e.g., 0.
    Output: Your possible integer as an integer or your default.
    '''
    # Make sure at least the default is an integer.
    try:
        int(default)
    except:
        raise ValueError('Your default is not an integer.')
        
    # Try to cast our possible integer as an integer.
    try:
        default = int(maybe_int)
    except ValueError, TypeError:
        pass
        
    # Return either the default or our properly int()'ed integer.
    return default
    

def detect_boolean(test_word):
    '''
    Defaults to false unless it can find truth. Who wants to do this inline?
    Input: The string to test for truth.
    Output: Boolean True or False.
    '''
    # Check if the test word is some type of "true".
    truth_words = re.compile(r'^(true|t)$', re.IGNORECASE)
    
    # If it's true, return true.
    if truth_words.match(test_word):
        return True
    
    # Unless it's not true. Then, return false.
    else:
        return False
    

def flex_aggregate(method, queryset, fieldname):
    '''
    Defines a function which performs an aggregation on a queryset.
    Input: method, description of a A
    Input: queryset, a queryset of objects to aggregate across.
    Input: fieldname, the name of the field to aggregate on.
    '''
    # Map the method to a class.
    if method == 'count':
        method = Count
    if method == 'avg':
        method = Avg
    if method == 'max':
        method = Max
    if method == 'min':
        method = Min
    if method == 'sum':
        method = Sum
    
    # Perform the aggregation.
    aggregation = queryset.aggregate(field=method(fieldname))
    
    # Try to return a number.
    try:
        return int_or_zero(aggregation['field'], 0)
        
    # If'n that doesn't work, return a 0.
    except:
        return 0
    

def handle_fg_distances(playergames):
    '''
    Defines a function which returns a custom-formatted string for FG distances.
    Input: playergames, a queryset of PlayerGames.
    Output: A string representing FG distances.
    '''
    
    # Set up a pair of lists.
    distances_strs = []
    distances_ints = []
    
    # Loop through the list of playergames
    for game in playergames:
        
        # Make sure this playergame has a field goal attempt.
        if game.fg_distances != '' or None:
            
            # Split on the comma if it's a comma-separated list.
            try:
                game_fgs = str.split(game.fg_distances, ', ')
                
                # For each one of these, add to the list.
                for g in game_fgs:
                    distances_strs.append(g)
                    
            # Wait, what if there's only one?
            except:
                try:
                    
                    # If there's only one, it would be a number. Try and int() it.
                    int(game.fg_distances)
                    
                    # If it is an integer, append it to the list.
                    distances_strs.append(game.fg_distances)
                except:
                    return ''
                    
    # Format the output -- make sure the list isn't empty.
    if distances_strs != []:
        
        # Loop through the list.
        for z in distances_strs:
            
            # Append to the other list as an int.
            distances_ints.append(int(z))
            
        # Man, I'm doing something weird here. IWDFWI, I guess.
        return str(distances_ints).strip('[').strip(']')
    
    # If it's empty, give up.
    else:
        return ''
    

def handle_points(tree, tag, type, item):
    '''
    Defines a function which constructs a valid record string from an XML tree and a tag.
    Input: tree, an ET.parse() object.
    Input: tag, a string representing an XML tag name.
    Input: type, a string representing an XML tag's "type" attribute value.
    Input: item, a string representing the item we want from the XML tag above.
    Output: An integer representing item.
    '''
    
    # Loop a list of objects matching the tag.
    for record in tree.findall(tag):
        
        # Find just the one instance of the tag we want based on the name attribute.
        if record.attrib['type'] == type:
            
            # Return the integer value of item, or 0.
            try:
                return int_or_zero(record.attrib[item], 0)
            except:
                return 0
    

def handle_record(tree, tag, attrib, name, token):
    '''
    Defines a function which constructs a valid record string from an XML tree and a tag.
    Input: tree, an ET.parse() object.
    Input: tag, a string representing an XML tag name.
    Input: name, a string representing an XML tag's "name" attribute value.
    Input: token, a comma-separated string representing the parts of the record to be joined.
    Output: A string representing a team record.
    '''
    # Prepare a list to hold the individual items.
    output_list = []
    
    # Split the token on a comma.
    split_token = string.split(token, ',')
    
    # Loop a list of objects matching the tag.
    for record in tree.findall(tag):
        
        # Find just the one instance of the tag we want based on the name attribute.
        if record.attrib[attrib] == name:
            
            # Find the pieces of the tag which match the token.
            for item in split_token:
                
                # Add the pieces to the list.
                output_list.append(record.attrib[item])
    
    # Return the list joined on dashes, since that looks fancy.
    return string.join(output_list, '-')

def handle_streak(tree):
    '''
    Defines a function which constructs a valid streak string from an XML tree and a tag.
    Input: tree, an ET.parse() object.
    Output: A string representing the streak.
    '''
    streak_tree = tree.find('streak')
    try:
        if streak_tree.attrib['games'] != '' or '0' or None:
            return u'%s game %s streak' % (streak_tree.attrib['games'], streak_tree.attrib['kind'])
        else:
            return ''
    except:
        return ''

def handle_percents(operand, divisor):
    '''
    Defines a function which handles percent construction with decimals.
    '''
    try:
        operand = operand + 0.0
        divisor = divisor + 0.0
        result = operand / divisor
        return result
    except:
        return 0.0