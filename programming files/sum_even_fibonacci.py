#bugs introduced: changed the while less than value to 400; changed the last line of the while loop to a-b, it was a+b;   jb
a, b = 0, 1
sum_even = 0
while b < 400: #while b is less than 4 billion
    if b % 2 == 0:
        sum_even += b
    a, b = b, a-b

print(sum_even) # printing the sum of even numbers

# answer should be 4613732

# otherwise program fails
