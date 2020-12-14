# Given a string, write a function that returns the index of the first unique (non-repeating) character. If there isn't a unique (non-repeating) character, return -1.

# Examples:

#     csFirstUniqueChar(input_str = "lambdaschool") -> 2
#     csFirstUniqueChar(input_str = "ilovelambdaschool") -> 0
#     csFirstUniqueChar(input_str = "vvv") -> -1

# Notes:

#     input_str will only contain lowercase alpha characters.



def csFirstUniqueChar(input_str):
    _map = {}
    
    for i in input_str:
        if i in _map:
            _map[i] += 1
        else:
            _map[i] = 1
    
    # enumerate => for i in range(input_str): input_str[i]
    for idx, ch in enumerate(input_str):
        if _map[ch] == 1:
            return idx
    
    return -1 