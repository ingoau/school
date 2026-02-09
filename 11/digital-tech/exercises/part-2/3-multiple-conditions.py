# Ask the user for a test score (0–100).
# If the score is 50 or higher, print &quot;Pass&quot;
# If the score is between 40 and 49, print &quot;Supplementary&quot;
# Otherwise, print &quot;Fail&quot;

testScoreInput = input("Enter test score (0-100): ")

try:
    testScore = float(testScoreInput)
except ValueError:
    print("Input isn't a number")
    exit()

if testScore >= 50:
    print("Pass")
elif testScore >= 40:
    print("Supplementary")
else:
    print("Fail")
