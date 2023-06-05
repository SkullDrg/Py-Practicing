#                                             QUESTIONS DATABASE
#                                           DATA INPUT AND OUTPUT
#                 https://docs.google.com/document/d/1nD_SMgHm3IbEVLh_uYNODUSUI5lmi92p7zUkVD-x_yM/edit#

#7° Question: Write a program to check if a gender is F or M or doesn't have a defined gender
Name = str(input("Please, what's your name? "))
print (f"Welcome {Name}, this program gonna check if the gender is F/M/UNDEFINED")

Letter = str.upper(input("Please, type here your gender F/M: "))

if Letter == "F":
    print ("Welcome, mistress.")
elif Letter == "M":
    print ("Welcome, mister.")
else:
    print ("Welcome, how should i call you?")