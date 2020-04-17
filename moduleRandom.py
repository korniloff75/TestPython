import random

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
numbers = range(1,8)
# random.shuffle(numbers)
print('numbers= ', numbers)
random_number = random.choice(numbers)
print('random_number= ', random_number)