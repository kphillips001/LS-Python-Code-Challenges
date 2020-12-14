# Given a sorted array (in ascending order) of integers and a target, write a function that finds the two integers that add up to the target.

# Examples:

#     csSortedTwoSum([3,8,12,16], 11) -> [0,1]
#     csSortedTwoSum([3,4,5], 8) -> [0,2]
#     csSortedTwoSum([0,1], 1) -> [0,1]

# Notes:

#     Each input will have exactly one solution.
#     You may not use the same element twice.


def csSortedTwoSum(numbers, target):
    lookup = {}
    
    for i in range(len(numbers)):
        if numbers[i] in lookup:
            return[lookup[numbers[i]], i]
        else:
            lookup[target-numbers[i]] = i
    return None