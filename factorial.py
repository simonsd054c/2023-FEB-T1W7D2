# Take a number as input from the user and calculate its factorial
# 5! = 5 * 4 * 3 * 2 * 1 = 120

# Input a number as num
num = int(input("Enter a number to calculate its factorial: "))

# Initialize fact = 1
fact = 1
# Initialize i = 1

# while i <= num
for i in range(2, num + 1):
    # fact = fact * i
    fact *= i
    # i = i + 1

# Display fact
print(fact)