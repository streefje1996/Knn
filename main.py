import numpy as np

data = np.genfromtxt('dataset1.csv', delimiter=';', usecols=[0,1,2,3,4,5,6,7], converters={5: lambda s: 0 if s == b"-1" else float(s), 7: lambda s: 0 if s == b"-1" else float(s)})

validation = np.genfromtxt('validation1.csv', delimiter=';', usecols=[0,1,2,3,4,5,6,7], converters={5: lambda s: 0 if s == b"-1" else float(s), 7: lambda s: 0 if s == b"-1" else float(s)})

dates = np.genfromtxt('dataset1.csv', delimiter=';', usecols=[0])
labels = []
for label in dates:
	if label < 20000301:
		labels.append('winter')
	elif 20000301 <= label < 20000601:
		labels.append('lente')
	elif 20000601 <= label < 20000901:
		labels.append('zomer')
	elif 20000901 <= label < 20001201:
		labels.append('herfst')
	else: # from 01-12 to end of year
		labels.append('winter')

def map(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

max_vals = np.amax(data, 0)
min_vals = np.amin(data, 0)


def normalize(data_set):
	for i in range(len(data_set)):  
		for j in range(len(data_set[i])):
			data_set[i][j] = map(data_set[i][j], min_vals[j], max_vals[j], 0, 100)


def calc_distance(validation_point, training_set):
	result = [validation_point[0], []] #this adds the date to the rsult set and adds distance
	for training_point in training_set:
			points = []
			for i in range(len(train_data)-1): #remove one beecause of date
					points.append(pow(validation_point[i+1] - training_point[i+1])) #add one because of date
			result[1].append( ( training_point[0], sum(points) ) )


normalize(data)
normalize(validation)

closest = []

for i in range(len(val_data)):
	closest.append(calc_distance(validation[i], data))
	sorted(closest[i][1], key=lambda x: x[1])



for k in range(365):
	print()


	


