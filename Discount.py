from datetime import datetime

current_time= datetime.now()
weekday = current_time.isoweekday()

print(weekday)

# Call the isoweekday() method to get the day
# of the week from the current datetime object.
subtotal = float(input("What is your subtotal? "))
#This variable is to keep the subtotal value for the strech challenge
subtotal_for_challenge = subtotal
#Here is a condition of a amount grater than 50 and if it is thursday or friday
if subtotal >=50 and (weekday == 4 or weekday == 5):
    #Here I am subtracting the 10%
    discount = subtotal * 0.1
    subtotal = subtotal - discount
    #Here we are getting the tax amount
    tax = float(subtotal * 0.06)
    #Now we get the total
    total = float(subtotal + tax)
    print(f"Discount amount: {discount:.2f}")
else:
    tax = float(subtotal * 0.06)
    total = float(subtotal + tax)

print(f"Tax: {tax:.2f}")
print(f"Total: {total:.2f}")

#STRETCH CHALLENGE
if subtotal_for_challenge < 50 and (weekday == 4 or weekday == 5):   
    to_get_discount = float(50 - subtotal_for_challenge)
    print(f"\nYou need to spend ${to_get_discount:.2f} more if you want the discount.\n")
    answer = input("Do you want to spend more to get the discount? YES/NO:   ")
    if answer.lower() == "yes":
        subtotal_for_challenge = float(input("\nWhat is your new subtotal:?  "))
        #Here I am subtracting the 10%
        discount = subtotal_for_challenge * 0.1
        subtotal_for_challenge = subtotal_for_challenge - discount
        #Here we are getting the tax amount
        tax = float(subtotal_for_challenge * 0.06)
        #Now we get the total
        total = float(subtotal_for_challenge + tax)
        print(f"\nDiscount amount: {discount:.2f}")
        print(f"Tax: {tax:.2f}")
        print(f"Total: {total:.2f}")
    else:
        print("\nThank you.\n")