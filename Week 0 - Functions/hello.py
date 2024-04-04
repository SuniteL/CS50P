# Ask user for their name?
name = input("What's your name? ")

# User name print
print("Hello, " + name)

"""
This is also a comment
"""

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

# curley brackets
print(f"hello, {name}")
