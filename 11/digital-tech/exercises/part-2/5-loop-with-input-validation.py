# Ask the user for a number greater than 0.
# If they enter an invalid number, keep asking until they enter a valid one.


def validate(numberAsString):
    try:
        number = float(numberAsString)
    except ValueError:
        return False

    return number > 0
