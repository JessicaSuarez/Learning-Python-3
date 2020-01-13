#Jessica Suarez Ex 14 Prompting and Passing

from sys import argv

script, user_firstname, user_lastname = argv
prompt = '*'

print(f"Hi {user_firstname} {user_lastname}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_firstname} {user_lastname}?")
likes = input(prompt)
#Ask if there is a way for two quotes to not come out at the end
print(f"Where do you live {user_firstname} {user_lastname}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

    print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
