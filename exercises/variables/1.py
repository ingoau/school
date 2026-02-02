# Create a program to calculate the area of a room depending on the inputs from a user.
# Display the result to the user.

inputtedWidth = input("Width: ")
inputtedHeight = input("Height: ")

width = 0
height = 0

try:
    width = float(inputtedWidth)
    height = float(inputtedHeight)
except ValueError:
    print("Input isn't a number")
    exit()


area = width * height

print(f"Area: {area}")
