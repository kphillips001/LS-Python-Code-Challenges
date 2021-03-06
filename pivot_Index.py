"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.
The "pivot" index is where the sum of all the numbers on the left of that index is equal to the sum of all the numbers on the right of that index.
If the input array does not have a "pivot" index, then the function should return `-1`. If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.
Example 1:
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.
Example 2:
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""
# input = array of numbers
# return a number (an index)
# return -1 otherwise
# Plan
# search through array to find pivot index => is i a pivot index
# Get sums of left subarray and right subarray and compare => if true => return index(i) => if false - keep looking. 
# return -1 if not found

def pivot_index_old(nums):
    # Search through nums list for a pivot index
    # go through each item in nums
    for i in range(len(nums)):
        # check if current index(i) is the pivot index
        # get sum of left subarray
        left_subarray = nums[0:i] # 0 up to i
        right_subarray = nums[i+1:] # don't include i => use i + 1 (don't want to include i)
        # get sum of left subarray
        left_sum = sum(left_subarray)
        # get sum of right subarray
        right_sum = sum(right_subarray)
        # check if they are equal
        if left_sum == right_sum:
            return i
        # if equal, return I
    return -1

#2 solution - More efficient
def pivot_index(nums):
    # create Lsum & Rsum
    l_sum = 0
    r_sum = sum(nums[1:]) #1 one onward

    # search through the array and check if index is pivot index
    for i in range(len(nums)):
        # check if l_sum == r_sum
        if l_sum == r_sum:
            return i
        # add number at current index to left sum
        l_sum += nums[i]
        # check that we are not at the last index
        if (i + 1 == len(nums)):
            r_sum = 0
        else:
            r_sum -= [i+1]
    return -1


