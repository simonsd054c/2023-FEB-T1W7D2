# Find the highest of the three numbers that the user inputs

# Take three numbers a, b and c from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# If a > b
if a > b:
    # If a > c
    if a > c:
        # Display a
        print(a)
    # Else
    else:
        # Display c
        print(c)
# Else
else:
    # If b > c
    if b > c:
        # Display b
        print(b)
    # Else
    else:
        # Display c
        print(c)