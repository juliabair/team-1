a, b = 0, 1
sum_even = 0
while b < 4000000: #while b is less than 4 billion
    if b % 2 == 0:
        sum_even += b
    a, b = b, a+b

print(sum_even) # printing the sum of even numbers

# answer should be 4613732

# otherwise program fails
