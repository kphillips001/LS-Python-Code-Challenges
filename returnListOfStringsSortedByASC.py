"""
Challenge #5:
Create a function that returns a list of strings sorted by length in ascending order. 
**Same as an array in JS**
Examples:
- sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
- sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
- sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
- sort_by_length([]) ➞ []
"""
def sort_by_length(lst):
    # Your code here
    # lst.sort(key = lambda list_item: len(list_item) )
    # print(lst)

    lst.sort(key = len)
    print(lst)

    # reverse
    lst.sort(key = len, reverse=True)
    print(lst)

sort_by_length(["a", "ccc", "dddd", "bb"])
sort_by_length(["apple", "pie", "shortcake"])