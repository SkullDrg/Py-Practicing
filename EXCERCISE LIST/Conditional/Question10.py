#                                             QUESTIONS DATABASE
#                                           DATA INPUT AND OUTPUT
#                 https://docs.google.com/document/d/1nD_SMgHm3IbEVLh_uYNODUSUI5lmi92p7zUkVD-x_yM/edit#

#10° Question: Re-do question 4, from QUESTION DATABASE-DATA INPUT AND OUTPUT, than, print your situation
#according to the following:
# <5 = Disapproved
# >=5 and <7 = Extra class
# >=7 = Approved
Name = str(input("Login: "))
Student = str(input(f"Welcome teacher {Name}, which student do you want the average of? "))
print (f"Okay, please then insert {Student}'s grades below:")

G1 = float(input("1° grade: "))
G2 = float(input("2° grade: "))
G3 = float(input("3° grade: "))

Average = (G1 + G2 + G3)/3
print (f"{Student}'s average is {Average:.1f}")

if Average < 5:
    print (f"Since {Student}'s average was {Average:.1f}, he/she got disapproved =(.")
elif Average >=5 and Average <7:
    print (f"Since {Student}'s average was {Average:.1f}, he/she gonna need soma extra classes. You can still do it.")
else:
    print (f"Congratulations {Student}, you got approved =D, your average was {Average:.1f}.")