#                                             QUESTIONS DATABASE
#                                           DATA INPUT AND OUTPUT
#                 https://docs.google.com/document/d/1nD_SMgHm3IbEVLh_uYNODUSUI5lmi92p7zUkVD-x_yM/edit#

#11° Question: Write a program to check if a number is an even value or and odd value
Name = str(input("Please, what's your name? "))
print (f"Welcome {Name}, this program gonna check if a value is even or odd")

Value = float(input("Type here a value: "))

if Value%2 == 0:
    print ("The value inserted was an even number.")
else:
    print ("The value inserted was an odd number.")