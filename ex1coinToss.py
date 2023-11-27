import random

# Example 1: Simulate 100 coin tosses & report the number and amount of times it returns heads
num_heads = 0
for toss in range(100):
    x = random.random()
    if x < 0.5:
        num_heads +=1
print ("Number of H:", num_heads)
print ("Proportion of H:", num_heads/100)
