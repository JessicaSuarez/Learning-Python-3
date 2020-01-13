#Jessica Suarez Ex16 Study Drill 2
#write a script that uses argv and read for the file
from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here is the file you want to open {filename}.")
print(txt.read())
