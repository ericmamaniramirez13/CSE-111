def main():
    start = float(input("Enter value in miles of starting ondometer:"))
    end = float(input("Enter ending odometer value in miles:  "))
    gallons = float(input("Enter amount of fuel gallons:  "))
    mpg = miles(start, end, gallons)
    lp100k = kilometers(mpg)
    print(f"{mpg:.1f} miles per gallon")
    print(f"{lp100k:.2f} liters per 100 kilometers")

def miles(start, end, gallons):
    mpg = (end - start)/gallons
    return mpg
def kilometers(mpg):
    lp100k = 235.215/mpg
    return lp100k
main()