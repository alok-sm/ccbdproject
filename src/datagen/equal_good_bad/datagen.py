import json
from random import random

NUMBER_OF_POINTS = 300

def generate_data(n, training):
	data = []
	for i in range(n):
		data.append(generate_point(training))
	return data

good_point = True
def generate_point(training):
	a = round(random()*100, 2)
	b = round(random()*100, 2)
	c = round(random()*100, 2)
	global good_point
	while(good_point and a + b + c < 240):
		a = round(random()*100, 2)
		b = round(random()*100, 2)
		c = round(random()*100, 2)

	point = [a, b, c]

	if(training):
		if(good_point):
			point.append(-1)
		else:
			point.append(1)

	good_point = not good_point

	return point

def main():
	data = generate_data(NUMBER_OF_POINTS, training = True)
	with open('training_data.json', 'w') as outfile:
		json.dump(data, outfile)

	data = generate_data(NUMBER_OF_POINTS, training = False)
	with open('testing_data.json', 'w') as outfile:
		json.dump(data, outfile)

if(__name__ == '__main__'):
	main()