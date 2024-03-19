"""
Ask your users to list a bunch of information about them: things they like, things they hate, names of family and friends... it's up to you how many and what kinds of things you pick. Keep it wacky!
"""

print("Welcome to your Adventure Story Simulator.")
print ()
print("I am going to ask you a bunch of questions and then create an epic story with you as the star.")
print()
name = input("What is your name? ")
print()
enemyName = input("What is your enemy's name? ")
print()
superPower = input("What is your super power? ")
print()
live = input("Where do you live?")
print()
food = input("What is your favorite food?")
print()

'''
2. Now construct your story - it can be about anything you want, but must use the variables you've created in step 1.
''' 

# Construct a wacky story
print("Hello", name, "Your ability to", superPower, "will make sure you never have to look at", enemyName, "again." "Go eat", food, "as you walk down the streets of", live, "and use", superPower, "for good and not evil!")