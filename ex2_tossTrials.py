import random

# Example 2: Simulate 1000 trials, each of which will have 2 tosses
# Report the % of times no heads appears, 1 head appeared, and 2 heads appeared
# Then, increase the number of trials until stability appears
# Expected convergence value = ~25% (see handwritten notes for math explanation)

num_trials = 1000
no_head = 0 # TT
one_head = 0 #TH or HT
two_head = 0 # HH

for trial in range(num_trials):
    toss_1 = random.random()
    toss_2 = random.random()

    if (toss_1 > 0.5) and (toss_2 > 0.5):
        no_head += 1
    elif (toss_1 > 0.5) and (toss_2 < 0.5) or (toss_1 < 0.5) and (toss_2 > 0.5):
        one_head += 1
    else:
        two_head += 1

print("No heads:", no_head/num_trials)
print("Exactly One Head:", one_head/num_trials)
print("Two Heads:", two_head/num_trials)

# We can see that both ho head and two heard converge to approx. 0.25, as expected
