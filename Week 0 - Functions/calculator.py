"""
# Integers - -2, -1, 0, 1, 2
x = int(input("Whats x? "))
y = int(input("Whats y? "))

print(x + y)

# print(int(input("Whats x? ")) + int(input("Whats y? ")))
"""

"""
# Floats - numbers with decimals
x = float(input("Whats x? "))
y = float(input("Whats y? "))

z = round(x + y)

# the f function plus :, helps to add the thousand, million seperator seperators
print(f"{z:,}")
"""

x = float(input("Whats x? "))
y = float(input("Whats y? "))

# the round and the 2 is for the rounding to the 2 decimal places
#z = round(x / y, 2)

#print(z)

z = x / y

# f string approach, .2f is showing 2 significant figures
print(f"{z:.2f}")