# Given a string, return a new string with all the vowels removed.

# Examples:

#     csRemoveTheVowels("Lambda School is awesome!") -> "Lmbd Schl s wsm!"

# Notes:

#     For this challenge, "y" is not considered a vowel.


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





#     import re
# def csRemoveTheVowels(input_str):
#     result = re.sub(r'[AEIOU]', '', input_str, flags=re.IGNORECASE)
#     return result