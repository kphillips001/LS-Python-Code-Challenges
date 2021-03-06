"""
Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to the `target`.

Examples:

- two_sum(nums = [2,5,9,13], target = 7) -> [0,1] (nums[0] + nums[1] == 7)
- two_sum(nums = [4,3,5], target = 8) -> [1,2] (nums[1] + nums[2] == 8)

Notes:
- No negative numbers and no zero in array or target
- return None if no answer
- Each input will have only one solution.
- You may not use the same element twice.
- You can return the answer in any order.
"""
def two_sum(nums, target):
    num_dict = {}

    for i in range(len(nums)):
        num_dict[nums[i]] = i
    
    for i in range(len(nums)):
        current_num = nums[i]
        # check if the compliment is in dict
        compliment = target - current_num

        if compliment in num_dict and i != num_dict[compliment]:
            # compliment exists! return its index
            return [i, num_dict[compliment]]

    # Brute force, try all number combinations
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         num1 = nums[i]
    #         num2 = nums[j]
    #         if num1 + num2 == target:
    #             return [i, j]

    # return None


print(two_sum(nums = [2,5,9,13], target = 7))
print(two_sum(nums = [4,3,5], target = 8))


print(two_sum([8, 9, 13, 1, 14, 17, 14, 6, 8, 3, 2, 17, 1, 2, 12, 11, 3, 11, 3, 13, 14, 13, 14, 1, 9, 2, 13, 10, 10, 5, 3, 2, 9, 12, 9, 2, 4, 5, 9, 17, 2, 12, 3, 13, 12, 2, 5, 7, 3, 14, 16, 11, 8, 4, 13, 15, 11, 17, 16, 18, 1, 4, 17, 4, 6, 17, 2, 7, 3, 9, 2, 2, 12, 14, 3, 6, 14, 10, 14, 10, 19, 16, 6, 18, 9, 18, 18, 7, 19, 4, 7, 16, 12, 16, 3, 19, 15, 2, 15, 6, 2, 17, 4, 14, 14, 11, 16, 17, 18, 3, 10, 20, 4, 11, 19, 18, 3, 13, 6, 15, 17, 12, 14, 8, 3, 9, 13, 15, 9, 2, 18, 17, 2, 20, 5, 8, 12, 18, 15, 12, 20, 19, 7, 8, 17, 6, 6, 15, 11, 17, 16, 12, 16, 16, 10, 19, 3, 11, 17, 11, 2, 14, 20, 10, 4, 12, 3, 16, 9, 8, 3, 18, 14, 14, 17, 7, 6, 20, 12, 10, 8, 12, 2, 14, 6, 16, 4, 2, 7, 19, 20, 6, 16, 20, 9, 10, 6, 19, 6, 5, 6, 19, 4, 19, 17, 7, 4, 14, 12, 11, 1, 16, 8, 11, 14, 12, 8, 3, 14, 4, 3, 6, 10, 20, 4, 12, 15, 20, 16, 8, 11, 4, 17, 1, 11, 19, 2, 19, 10, 14, 18, 17, 8, 18, 8, 10, 18, 8, 17, 4, 10, 19, 14, 2, 6, 14, 19, 5, 18, 1, 7, 7, 10, 9, 18, 1, 12, 12, 8, 16, 5, 2, 16, 15, 7, 14, 15, 15, 12, 18, 18, 9, 15, 11, 15, 10, 17, 3, 19, 20, 17, 19, 12, 18, 1, 1, 13, 12, 10, 2, 5, 20, 17, 12, 13, 5, 14, 6, 7, 12, 1, 15, 12, 6, 19, 4, 17, 19, 17, 3, 18, 13, 17, 12, 19, 15, 8, 2, 18, 6, 11, 12, 6, 14, 8, 8, 1, 13, 14, 5, 7, 16, 12, 14, 17, 5, 13, 8, 3, 8, 16, 1, 20, 6, 10, 20, 18, 12, 4, 13, 18, 4, 13, 10, 10, 5, 19, 1, 20, 11, 19, 1, 1, 1, 1, 16, 8, 12, 3, 9, 10, 2, 8, 11, 10, 18, 15, 10, 11, 18, 13, 15, 15, 13, 12, 1, 16, 20, 4, 6, 3, 15, 18, 15, 10, 15, 11, 10, 19, 12, 18, 17, 2, 15, 10, 2, 12, 1, 18, 15, 5, 15, 10, 10, 5, 19, 9, 19, 6, 8, 3, 1, 14, 18, 12, 9, 15, 12, 12, 8, 3, 4, 1, 17, 14, 12, 15, 1, 9, 12, 12, 11, 5, 10, 1, 7, 15, 17, 4, 12, 20, 11, 17, 17, 14, 10, 13, 4, 4, 6, 20, 9, 16, 4, 5, 13, 19, 19, 13, 7, 18, 15, 20, 14, 2, 1, 12, 10, 11, 19, 13, 12, 11, 11, 15, 10, 1, 5, 19, 10, 4, 7, 19, 7, 7, 18, 6, 14, 6, 14, 11, 13, 9, 18, 15, 8, 10, 2, 19, 16, 15, 17, 11, 5, 1, 5, 4, 10, 6, 3, 9, 15, 12, 1, 16, 9, 12, 17, 3, 15, 8, 5, 18, 10, 4, 13, 5, 3, 5, 2, 6, 12, 7, 5, 7, 5, 19, 17, 10, 13, 8, 10, 12, 13, 12, 16, 18, 1, 15, 20, 19, 11, 12, 9, 10, 3, 6, 18, 8, 14, 16, 1, 11, 20, 2, 19, 1, 14, 5, 8, 15, 11, 16, 18, 2, 14, 2, 2, 11, 16, 1, 19, 3, 17, 5, 7, 7, 16, 15, 10, 6, 4, 14, 8, 8, 15, 8, 4, 4, 19, 9, 9, 14, 4, 19, 1, 17, 20, 16, 20, 11, 13, 3, 1, 20, 16, 11, 4, 4, 5, 20, 2, 4, 6, 11, 14, 18, 17, 2, 8, 14, 17, 4, 10, 3, 8, 5, 17, 8, 2, 6, 2, 10, 14, 11, 2, 13, 14, 4, 2, 12, 4, 15, 6, 8, 8, 3, 10, 13, 11, 13, 9, 10, 15, 14, 19, 15, 7, 20, 16, 10, 6, 2, 16, 19, 19, 7, 4, 19, 19, 6, 18, 2, 17, 11, 19, 12, 14, 15, 8, 8, 18, 9, 8, 1, 11, 1, 3, 4, 18, 2, 7, 16, 7, 19, 16, 12, 13, 6, 18, 11, 5, 11, 5, 11, 15, 20, 10, 12, 10, 10, 12, 13, 9, 15, 2, 15, 12, 16, 12, 19, 1, 5, 14, 1, 15, 13, 13, 19, 7, 18, 16, 1, 5, 12, 11, 12, 18, 7, 7, 12, 6, 3, 15, 4, 9, 8, 13, 10, 12, 5, 9, 16, 5, 16, 17, 9, 18, 6, 18, 14, 17, 10, 15, 15, 7, 11, 10, 2, 8, 5, 6, 15, 7, 4, 18, 5, 6, 18, 4, 13, 3, 3, 19, 6, 8, 1, 16, 9, 10, 14, 18, 20, 7, 15, 13, 7, 5, 18, 9, 11, 10, 13, 5, 8, 11, 17, 14, 13, 15, 9, 2, 2, 5, 11, 11, 14, 4, 6, 1, 18, 20, 19, 12, 1, 13, 2, 10, 5, 17, 5, 6, 19, 1, 20, 11, 1, 14, 15, 20, 1, 18, 17, 16, 12, 18, 10, 13, 8, 19, 6, 1, 19, 18, 5, 19, 15, 3, 19, 13, 10, 18, 8, 16, 18, 6, 13, 14, 20, 9, 20, 17, 1, 3, 11, 10, 9, 13, 7, 19, 14, 18, 5, 16, 6, 5, 2, 19, 13, 18, 5, 7, 10, 7, 9, 11, 15, 17, 19, 10, 7, 3, 6, 14, 19, 2, 8, 2, 19, 9, 10, 18, 9, 6, 11, 19, 9, 11, 17, 10, 4, 6, 5, 5, 8, 16, 16, 18, 14, 10, 8, 13, 6, 13, 17, 9, 9, 12, 11, 8, 17, 14, 4, 19, 3, 9, 6, 11, 4, 6, 1, 11, 12, 4, 18, 20, 8, 20, 10, 5, 5, 18, 2, 22, 23] * 10, target=45))