# Extend the previous project to calculate the amount of tax paid at a rate of 30% and display
# the previous information along with tax to the user, what their pay will be minus tax and
# amount of time worked in days, hours and minutes

PAY_PER_HOUR = 18
TAX_RATE = 0.3

inputtedMinutes = input("Enter work minutes: ")

try:
    minutes = float(inputtedMinutes)
except ValueError:
    print("Input isn't a number")
    exit()

payBeforeTax = PAY_PER_HOUR * (minutes / 60)
tax = payBeforeTax * TAX_RATE
payAfterTax = payBeforeTax - tax

print(f"""Before tax: ${round(payBeforeTax, 2)}
Amount scammed by the government: ${round(tax, 2)}
Income after being scammed by the government: ${round(payAfterTax, 2)}""")
