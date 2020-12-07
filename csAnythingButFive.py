def csAnythingButFive(start, end):
    # this is fairly tricky. We basically want to scan all numbers from start to end, and check that they do not have the digit 5
    # the easiest thing to do here, is to generate a range of numbers, convert them to strings, and check if the string contains the character "5"
    
    # generate the range (remember the question says end is inclusive, so use end + 1 !)
    num_range = range(start, end + 1)
    
    # now lets just count all numbers that do not have the character 5 in it
    # we cant easily check for digits using integers, but strings are easy! lets convert the numbers to strings
    number_count = 0
    for num in num_range:
        # convert the number to a string, and check if it has the character 5
        num_str = str(num)
        if '5' not in num_str:
            number_count += 1
    
    return number_count