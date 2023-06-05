#                                             QUESTIONS DATABASE
#                                           DATA INPUT AND OUTPUT
#                 https://docs.google.com/document/d/1nD_SMgHm3IbEVLh_uYNODUSUI5lmi92p7zUkVD-x_yM/edit#

#8° Question: Write a program to check if a value is positive or negative
Name = str(input("Please, what's your name? "))
print (f"Welcome {Name}, this program gonna check if a value is positive or not")

Value = float(input("Please, type here a value: "))

if Value > 0:
    print (f"{Value} is a positive number.")
else:
    print (f"{Value} is a negative number.")