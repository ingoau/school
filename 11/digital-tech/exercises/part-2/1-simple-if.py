# Ask the user for a number.
# If the number is greater than 10, print &quot;Big number&quot;.
# Otherwise, print &quot;Small number&quot;.

numberInput = input("Enter number: ")

try:
    number = float(numberInput)
except ValueError:
    print("Input isn't a number")
    exit()

if number > 10:
    print("Big number")
else:
    print("Small number")
