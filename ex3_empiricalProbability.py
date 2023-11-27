# Example 3
# See written notes for mathematical possibilities
import random

num_games = 1000
bankroll = 100
ran_out = 0

for game in range (num_games):
    for tosses in range(30):
        toss1 = random.randint(1,6) # Need the random. to call the function from the package
        toss2 = random.randint(1,6)

        if toss1 + toss2 <= 10:
            bankroll += 10
        else: 
            bankroll -= 50
        if bankroll <= 0:
            ran_out += 1
            break # Terminates loop

print("Empirical probability of having money:",1 - ran_out/num_games)
# The output implies we'll most likely make money from the game
