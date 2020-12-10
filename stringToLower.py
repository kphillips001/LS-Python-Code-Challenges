"""
Given a string, implement a function that returns the string with all lowercase
characters.
Example 1:
Input: "LambdaSchool"
Output: "lambdaschool"
Example 2:
Input: "austen"
Output: "austen"
Example 3:
Input: "LLAMA"
Output: "llama"
*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*
"""
# Can not use built in functions. 
# convert characters to ASCII
# "z" => 122 ASCI
# if ASCII number is between 97 - 122 => then it's lowercase. 
# 65 to 122 is uppercase => Z uppercase is 90
# if 

def to_lower_case(string):
    # Your code here