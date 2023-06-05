#                                             QUESTIONS DATABASE
#                                           DATA INPUT AND OUTPUT
#                 https://docs.google.com/document/d/1nD_SMgHm3IbEVLh_uYNODUSUI5lmi92p7zUkVD-x_yM/edit#

#13° Question: Write a program to receive 2 values and then asks which operation it wants to run, 
#with the following attributes:
# Even or Odd value
# Positive or negative value
# Integer or decimal value
Name = str(input("Please, what's your name? "))
print (f"Welcome {Name}, this program gonna check a few things about 2 values")

Value1 = float(input("Type here the 1st value: "))
Value2 = float(input("Type here the 2st value: "))

Operation = str(input("Now tell me, what do you want to do with these values Add/Sub/Div/Multp? "))
Result = 0

if Operation == "Add":
    Result = (Value1 + Value2)
elif Operation == "Sub":
    Result = (Value1 - Value2)
elif Operation == "Div":
    Result = (Value1/Value2)
else:
    Result = (Value1 * Value2)

print (Result)

if Result%2 == 0:
    print (f"The result {Result:.1f} is an even value.")
else:
    print (f"The result {Result:.1f} is and odd value.")

if Result > 0:
    print (f"The result {Result:.1f} is a positive number.")
else:
    print (f"The result {Result:.1f} is a negative number.")

if Result.is_integer:
    print (f"The result {Result:.1f} is an integer value.")
else:
    print (f"The result {Result:.1f} is a decimal value.")