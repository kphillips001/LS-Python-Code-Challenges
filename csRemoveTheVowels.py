def csRemoveTheVowels(input_str):
    # create a set of all vowels to use when we are checking if a character is a vowel
    vowel_set = ('a', 'e','i', 'o', 'u')
    
    # we will build a new string that has no vowels
    result_str = ''
    
    # loop over each character, and check if its a vowel
    # if its a vowel, DO NOT add it to result_str, otherwise, add to result
    for i in input_str:   
        if i.lower() not in vowel_set:
            result_str += i    
            
    return result_str