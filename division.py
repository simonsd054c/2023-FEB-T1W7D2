# Take two numbers from the user and display the result of their division

# Input numerator as n and denominator as d
n = float(input("Enter numerator: "))
d = float(input("Enter denominator: "))

# If d == 0
if d == 0:
    # Display "Denominator cannot be zero"
    print("Denominator cannot be zero")
# else
else:
    # q = n / d
    q = n / d
    # Display q
    print(q)