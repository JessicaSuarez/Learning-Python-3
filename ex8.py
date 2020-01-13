#Jessica Suarez Ex 8 Printing Printing
#formatter defined into 4 pairs of brackets
formatter = "{} {} {} {}"
#formatter here will receive the format in the parentheses instead of the brackets
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
#this prints out the actual brackets declated in formatter variable
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
