#                                             QUESTIONS DATABASE
#                                           DATA INPUT AND OUTPUT
#                 https://docs.google.com/document/d/1nD_SMgHm3IbEVLh_uYNODUSUI5lmi92p7zUkVD-x_yM/edit#

#6° Question: Write a program to test if 2 values are equal or if one is higher than the other
Name = str(input("What's your name? "))
print (f"Welcome, {Name}, this program gonna test if a value is higher or equal than another value.")
N1 = int(input("Please, insert here the first value: "))
N2 = int(input("Please, insert here the second value: "))

if N1 > N2:
    print (f"{N1} is higher than {N2}.")
elif N1 < N2:
    print (f"{N1} isn't higher than {N2}.")
else:
    print ("Both values inserted are equal.")