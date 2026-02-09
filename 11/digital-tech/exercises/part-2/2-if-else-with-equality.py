# Ask the user for a password.
# If it equals &quot;python&quot;, print &quot;Access granted&quot;.
# Otherwise, print &quot;Access denied&quot;.

import getpass

try:
    # Prompt for password using built in getpass module
    password = getpass.getpass(prompt="Enter password: ", echo_char="*")
except Exception:
    # Fallback to input() if getpass doesn't work
    print("Password input not available, falling back to input")
    password = input("Enter password: ")

# Check password
if password == "python":
    print("Access granted")
else:
    print("Access denied")
