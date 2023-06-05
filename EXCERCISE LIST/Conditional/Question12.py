#                                             QUESTIONS DATABASE
#                                           DATA INPUT AND OUTPUT
#                 https://docs.google.com/document/d/1nD_SMgHm3IbEVLh_uYNODUSUI5lmi92p7zUkVD-x_yM/edit#

#12° Question: Write a program to check if an individual still gotta vote, according to the following
# Under 16: Don't vote
# Between 16 and 18: Optional vote
# Between 18(Included in) and 60(Included in): Compulsory vote
# More than 60: Optional vote
Name = str(input("Please, what's your name? "))
print (f"Welcome {Name}, this program gonna check if a person still needs to vote")

Birth_Year = int(input("In which year were you born? "))
Actual_Year = int(input("In which year are we now? "))

Age = (Actual_Year - Birth_Year)

if Age < 16:
    print (f"Since you are {Age} years old, you don't vote yet.")
elif Age>16 and Age<18 or Age>60:
    print (f"Since you are {Age} years old, you vote if you want.")
else:
    print (f"Since you have between 18 and 60 years old, your vote is mandatory.")