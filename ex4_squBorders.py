# Example 4
# See notes for math explanation

import random 

trials = 100
hit = 0
radius = 0.125

for trial in range(trials):
    x = 4 * random.random()
    y = 4 * random.random()
    left = x - radius
    right = x + radius
    up = y + radius
    down = y - radius

    if (left <= 2 <= right) or (down <= 2 <= up):
        hit += 1

print("Percentage of hits:",hit/trials*100,"%")
