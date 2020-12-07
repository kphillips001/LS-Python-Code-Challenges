def csSumOfPositive(input_arr):
    # create the variable we will return 
    positive_sum = 0
    
    # loop over the array, check if each number is positive, if it is, add to positive_sum
    for num in input_arr:
        if num > 0:
            positive_sum += num


    return positive_sum