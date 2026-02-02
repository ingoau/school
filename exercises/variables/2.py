# Create a program that asks the user to enter an amount of time worked. Then, using these
# hours, calculate the user’s pay, working at $18/hour, and display this to the user.

PAY_PER_HOUR = 18

inputtedHours = input("Enter work hours: ")

try:
    hours = float(inputtedHours)
except ValueError:
    print("Input isn't a number")
    exit()

pay = PAY_PER_HOUR * hours

print(f"Pay: ${round(pay, 2)}")
