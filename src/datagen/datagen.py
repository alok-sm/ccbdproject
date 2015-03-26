import json
from random import random

NUMBER_OF_POINTS = 1000

def generate_data(n, training):
	data = []
	for i in range(n):
		data.append(generate_point(training))
	return data


def generate_point(training):
	point = [round(random()*100, 2), round(random()*100, 2), round(random()*100, 2)]

	if(training):
		if(point[0] + point[1] + point[2] > 240):
			point.append(-1)
		else:
			point.append(1)

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