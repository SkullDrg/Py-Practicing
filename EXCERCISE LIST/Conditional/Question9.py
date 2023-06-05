#                                             QUESTIONS DATABASE
#                                           DATA INPUT AND OUTPUT
#                 https://docs.google.com/document/d/1nD_SMgHm3IbEVLh_uYNODUSUI5lmi92p7zUkVD-x_yM/edit#

#9° Question: Write a program to check if a letter is a vowel or a consonant
Name = str(input("Please, what's your name? "))
print (f"Welcome {Name}, this program gonna check if a letter is a vowel or a consonant")
Vowel = ["A", "E", "I", "O", "U"]

Letter = str.upper(input("Please, type here a letter: "))

if Letter in Vowel:
    print (f"{Letter} is a vowel.")
else:
    print (f"{Letter} is a consonant.")