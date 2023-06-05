#                                             QUESTIONS DATABASE
#                                           DATA INPUT AND OUTPUT
#                 https://docs.google.com/document/d/1nD_SMgHm3IbEVLh_uYNODUSUI5lmi92p7zUkVD-x_yM/edit#

#4° Question: Program that asks for a student's name and 3 grades. Calculate the average and show the result
print ("Welcome teacher.")
Student = str(input("Type the student's name: "))
G1 = int(input("Type here the student's first grade: "))
G2 = int(input("Type here the student's second grade: "))
G3 = int(input("Type here the students third grade: "))

Average = (G1 + G2 + G3)/3

print (f"{Student}'s average is {Average}.")