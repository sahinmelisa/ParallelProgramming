import random
import math

def next_pi():
    inner_points = 0
    total_points = 0
    
    while True:
        x_random = random.random()
        y_random = random.random()
        z = math.sqrt(x_random**2 + y_random**2)
        if z <= 1:
            inner_points += 1
        total_points += 1
        
        my_pi = 4 * (inner_points / total_points)
        yield my_pi 
