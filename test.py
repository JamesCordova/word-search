import random

weights = [0.5, 0.9, 0.01]

options = [[1, 0], [1, 1], [1, -1]]

option = random.choices(options, weights = weights, k = 1)[0]

print(option)