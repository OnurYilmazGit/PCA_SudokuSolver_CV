import os

def main():
	print('Please press 1 to see PCA analysis on MNIST dataset')
	print('Please press 2 to see Sudoku on your Terminal')
	input1 = input('Enter a number here: ')
	if int(input1) == 1:
		os.system('python3 mnist.py')
	elif int(input1) == 2:		
		os.system('python3 sudoku.py')
	else: 
		print('You pressed wrong number..')

if __name__ == "__main__":
	main()