"""
Challenge #8:
Create a function that returns the number of arguments it was called with.
Examples:
- num_args() ➞ 0
- num_args("foo") ➞ 1
- num_args("foo", "bar") ➞ 2
- num_args(True, False) ➞ 2
- num_args({}) ➞ 1
"""
# similiar to ...array in JS => *args

def num_args(*args, arg2):
    # Your code here
    print(len(args))
    return

num_args("foo", "bar")
num_args("foo")
num_args("foo", "bar", arg2='this is a keyword arg')