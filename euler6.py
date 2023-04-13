# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Define sum_of_squares = 0
sum_of_squares = 0
# Define sum = 0
sum = 0
# Define i = 1

# while i <= 100
for i in range(101):
    # sum_of_squares = sum_of_squares + i*i
    sum_of_squares += pow(i, 2)
    # sum = sum + i
    sum += i
    # i = i + 1

# square_of_sums = sum * sum
square_of_sums = sum * sum
# diff = square_of_sums - sum_of_squares
diff = square_of_sums - sum_of_squares
# Display diff
print(diff)