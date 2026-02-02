# Extend the previous project to calculate the amount of tax paid at a rate of 30% and display
# the previous information along with tax to the user, what their pay will be minus tax and
# amount of time worked in days, hours and minutes

PAY_PER_HOUR = 18
TAX_RATE = 0.3

inputtedHours = input("Enter work hours: ")

try:
    hours = float(inputtedHours)
except ValueError:
    print("Input isn't a number")
    exit()

payBeforeTax = PAY_PER_HOUR * hours
tax = payBeforeTax * TAX_RATE
payAfterTax = payBeforeTax - tax

print(f"""Before tax: ${round(payBeforeTax, 2)}
Amount scammed by the government: ${round(tax, 2)}
Income after being scammed by the government: ${round(payAfterTax, 2)}""")
