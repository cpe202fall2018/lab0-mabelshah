def weight_on_planets():
	earth = int(input("What do you weigh on earth? "))
	mars = earth*0.38
	jupiter = earth*2.34
	print('\nOn Mars you would weigh {} pounds.\nOn Jupiter you would weigh {} pounds.'.format(mars, jupiter))

if __name__ == '__main__':
   weight_on_planets()