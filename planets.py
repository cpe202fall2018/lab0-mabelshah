def weight_on_planets():
	earth = int(input("What do you weigh on earth? "))
	print('\nOn Mars you would weigh %5.2f pounds.' %(earth * 0.38))
	print('On Jupiter you would weigh %5.2f pounds.' %(earth * 2.34))	   
   
   
if __name__ == '__main__':
   weight_on_planets()