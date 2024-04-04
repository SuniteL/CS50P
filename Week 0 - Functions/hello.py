# Ask user for their name?
name = input("What's your name? ").strip().title() 

""" - Commented out to make it visible easier to see
# User name print
print("Hello, " + name)

# User name print, the comma adds a space after the "Hello," when printed
print("Hello,", name)

# with the end=""
print("Hello, ", end="")
print(name)
print("Hello, ", end="???")
print(name)

# with the sep=""
print("Hello,", name, sep="!!!")

# \ in the quotes
print("Hello, \"Friend\"")
"""

# remove whitespace from str
#name = name.strip()

# Capitalise the name
#name = name.capitalize()

# remove whitespace from str
#name = name.strip().title() 

# split the users name into first name and last name
first, last = name.split(" ")

# curley brackets for f = function
print(f"Hello, {first}")
print(f"Hello, {last}")



