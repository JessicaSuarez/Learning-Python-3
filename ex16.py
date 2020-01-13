#Jessica Suarez Ex 16 Reading and Writing Files
#import argv from sys module
from sys import argv

script, filename = argv #short way of assigning value to two variables

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
#The prompt
input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines. ")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to a file.")

target.write(line1 + '\n' + line2 + '\n' + line3 + '\n') #Got Stuck here need more research

print("And finally, we close it.")
target.close()
