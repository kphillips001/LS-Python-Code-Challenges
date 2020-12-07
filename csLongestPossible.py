def csLongestPossible(str_1, str_2):
    # theres a few ways to get this done
    # one of the simplest ways is to just build an array of unique characters
    # then sort it and return it
    unique_chars = []

    for char in str_1:
        # check if the character has never been seen before
        if char not in unique_chars:
            # add to unique_chars
            unique_chars.append(char)
    
    # do the same loop for str_2
    for char in str_2:
        # check if the character has never been seen before
        if char not in unique_chars:
            # add to unique_chars
            unique_chars.append(char)
    
    # sort the array
    unique_chars.sort()
    
    # to turn the array to a string, use string.join()
    return ''.join(unique_chars)
    