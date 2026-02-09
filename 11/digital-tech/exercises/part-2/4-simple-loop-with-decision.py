# Use a for loop to print the numbers from 1 to 20.
# Print &quot;Even&quot; next to even numbers and &quot;Odd&quot; next to odd numbers.


def isEven(number):
    return number % 2 == 0


for i in range(1, 21):
    print(f"{i} {'Even' if isEven(i) else 'Odd'}")
