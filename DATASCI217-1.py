# DATASCI217 - Assignment 1

# Name: Shwetha Kandhalu

# If we list all the natural numbers below 10 that are multiples 
# of 3 or 5, we get (3, 5, 6, 9). The sum of these multiples 
# is 23. Find the sum of all multiples of 3 or 5 below 1000.

count = 0

for i in range(1000):
    if i%3 == 0 or i%5 == 0:
        count = count + i

print(count)