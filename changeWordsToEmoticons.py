"""
Challenge #4:

Create a function that changes specific words into emoticons. Given a sentence
as a string, replace the words `smile`, `grin`, `sad`, and `mad` with their
corresponding emoticons.

word -> emoticon
---
smile -> :D
grin -> :)
sad -> :(
mad	-> :P

Examples:
- emotify("Make me smile") ➞ "Make me :D"
- emotify("Make me grin") ➞ "Make me :)"
- emotify("Make me sad") ➞ "Make me :("

Notes:
- The sentence always starts with "Make me" and ends with an emote.
- Try to solve this without using conditional statements like if/else.
"""


def emotify(txt):
    # Your code here
    txt = txt.replace("smile", ":D").replace("grin", ":)").replace('sad', ":(").replace("mad", ":P")
    return txt

print(emotify("Make me smile, mad, sad"))
print(emotify("Make me mad"))
print(emotify("Make me sad"))