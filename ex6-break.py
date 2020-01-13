#Jessica Suarez (& FiatMami)
#Ex 6 Strings and Text (& me messing some thangs up)
#sets #sets variable to 10
types_of_people = 550
#sets x to a string with a variable inside
x = "There are {types_of_people} types of people."
#declaring variables
binary = "binary"
do_not = "don't"
#sets y to a string containing a variable
y = f"Those who know {binary} and those who do_not."
#print variables x and y
print(x)
print(y)
#print a string with the variables x and y inside them. a different way to show how you can print strings in various ways
print(f"I said: {x}")
print(f"I also said: '{y}'")
#set variable for hilarious to false
hilarious = True;

joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print (w + e);
