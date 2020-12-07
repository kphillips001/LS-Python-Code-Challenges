def csShortestWord(input_str):
    # splitting the words so we have an array of just words (no whitespace)
    # eg "the big brown fox" => ["the", "big", "brown", "fox"]
    words = input_str.split()
    
    # now just find the shortest word
    shortest_length = len(words[0])
    
    # to find shortest word, check all words and update the shortest_length variable every time we see a shorter word
    for word in words:
        if len(word) < shortest_length:
            shortest_length = len(word)
            
    return shortest_length  