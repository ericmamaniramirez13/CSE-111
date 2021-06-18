import math
from datetime import datetime
def problem(w,a,d):
    v=((math.pi*w**2)*a*(w*a+2540*d))/(10**7)
    return round(v,1)
again = "yes"
while again.lower() == "yes":
    width = float(input("\nEnter the width of the tire in mm:  "))
    ratio = float(input("Enter the aspect ratio of the tire:  "))
    diameter = float(input("Enter the diameter of the wheel in inches:  "))
    print("The approximate volume is: ", problem(width, ratio, diameter), "Milliliters.\n")
    with open("volumes.txt", "at") as line:
   
        print(datetime.now(), width, ratio, diameter, problem(width,ratio, diameter), file=line)
    buy = input("Do you want to buy the tires ")
    if buy.lower() == "yes":
        with open("volumes.txt", "at") as line:
            phone = input("Great. What is your phone number?:  ")
            print ("Phone of buyer: ", phone, file=line)
            
    again = input("Do you want to run this code again?(Yes/No):  \n")
    if again.lower() == "no":
        print("Thank you....\n")






with open("WEEK-1/volumes.txt", "at") as line:
    """for x in line:
        new = x.strip()
        new = x.split(" ")
        print(new[0], end=" ")"""
        