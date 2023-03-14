# Define boolean variables
a = True
b = False

# Use boolean logic to create a new variable
c = a and not b
print(c)  # Output: True

# Define string variable
my_string = "Hello, World!"

# Use string methods to create a new string
new_string = ""
for char in my_string:
    if char in "aeiouAEIOU":
        new_string += char.upper()
    else:
        new_string += char

print(new_string)  # Output: HEllO, World!
