#Jessica Suarez Ex 15 Reading Files
#imports argv from sys module
from sys import argv

#unpacking arguments?
script, filename = argv
#tells txt to open the file
txt = open(filename)



print("Type the filename again:")
#user must input here
file_again = input (">")
#the file is retrieved once again by txt
txt_again = open(file_again)
#this prinst the contents of the file
print(txt_again.read())

txt_again = close(file_again)
txt = close(filename)
