import random
"""
It eats exactly once a day.
If it ate cheese today, tomorrow it will eat lettuce or grapes with equal probability.
If it ate grapes today, tomorrow it will eat grapes with probability 1/10, cheese with probability 4/10 and lettuce with probability 5/10.
If it ate lettuce today, tomorrow it will eat grapes with probability 4/10 or cheese with probability 6/10. It will not eat lettuce again tomorrow.
"""
PURPLE = '\033[35m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
ENDC = '\033[0m'

food = [0, 1, 2]
# 0--> cheese
# 1--> grapes
# 2--> lettuce
food_dict = {0:'cheese', 1:'grapes', 2:'lettuce'}

last_meal = 0
last_meal = food[random.randint(0,2)]
print("It started in the first day eating {}.".format(food_dict[last_meal]))
for x in range(20):
	if last_meal == 0:
		food = [0] * 33
		food += [1] * 33
		food += [2] * 33
	elif last_meal == 1:
		food = [1] * 10
		food += [0] * 40
		food += [2] * 50
	elif last_meal == 2:
		food = [0] * 60
		food += [1] * 40
	else:
		print("Something went wrong...")
	last_meal = random.choice(food)
	if last_meal == 0:
		color = YELLOW
	elif last_meal == 1:
		color = PURPLE
	else:
		color = GREEN
	print("Today it eat " + color + "{}".format(food_dict[last_meal]) + ENDC)

