import random
numbers = random.sample(range(100), 8)
print ("Numbrid: " + str(numbers))
results = [numbers[0], numbers[-1]]
print ("Tulemus: " + str(results))