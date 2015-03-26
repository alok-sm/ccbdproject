import json
from random import random

NUMBER_OF_POINTS = 1000

def generate_data(n, training):
	data = []
	for i in range(n):
		data.append(generate_point(training))
	return data


def generate_point(training):
	point = {
		'cpu'  : round(random()*100, 2),
		'ram'  : round(random()*100, 2),
		'disk' : round(random()*100, 2)
	}

	if(training):
		if((point['cpu'] + point['ram'] + point['disk'] > 240) or (point['cpu'] > 90) or (point['ram'] > 90) or (point['disk'] > 90)):
			point['good'] = False
		else:
			point['good'] = True

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