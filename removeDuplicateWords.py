# Given a string, write a function that removes all duplicate words from the input. The string that you return should only contain the first occurrence of each word in the string.

# Examples:

#     `csRemoveDuplicateWords("alpha bravo bravo golf golf golf delta alpha bravo bravo golf golf golf delta") -> "alpha bravo golf delta"
#     `csRemoveDuplicateWords("my dog is my dog is super smart") -> "my dog is super smart"



def csRemoveDuplicateWords(input_str):
    input_str = input_str.split()
    unique = []
    for word in input_str:
        if word not in unique:
            unique.append(word)
    input_str = ' '.join(unique)
    
    return input_str
