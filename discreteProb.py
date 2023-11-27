# Discrete EC Notes

# Import random package and call the function to output random value
import random
x = random.random()

# Print results
print (x)

# Coin toss
if x < 0.5:
    print('Heads')
else:
    print('Tails')

# 'for' loop 
for i in range(4):
    print(i)

# How many even numbers in a range?
num_evens = 0
for i in range(6):
    if i%2 == 0:
        num_evens += 1 # Goes through every number from 0 to 6, if the number is evenly divisible by 6, 
print (num_evens)
