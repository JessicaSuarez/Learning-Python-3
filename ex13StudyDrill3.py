#Jessica Suarez Ex 13 Study Drill a script with fewer arguments

from sys import argv # we import argv module from sys
script, salsa, bachata, merengue, flamenco = argv
#Added another argument
print("The name of this script is", script)
print("The first type of dance is", salsa)
#used the f for formatting, but whats the difference? Ask group

print(f"The second type of dance is", bachata)
print("The third type of dance is", merengue)
print("The fourth type of dance is", flamenco)
#Added an input statement to show how one differs from the other
print("You can't have these dances without what?")
Music = input()
print("Very Good!")


#NOTE
#input requires user input when script is running
#argv requires user when running the script on command line
