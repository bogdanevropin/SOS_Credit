"""
Generating file with random numbers
Script with last n lines from gen file (1h 20min)
"""
import os
import random


def gen_rand_file():
	"""
	generating random file
	"""
	curr_dir = os.getcwd()
	n = input('How many lines in rand file?\n')
	if n.isnumeric():
		with open(curr_dir + '/random_text_file.txt', 'w+') as file:
			for line in range(int(n)):
				for num in range(random.randint(1, 10)):
					file.write(str(random.randint(1, 100)))
					file.write(' ')
				file.write('\n')  # last line only space
	else:
		gen_rand_file()


def read_last_n():
	"""
	reads last n lines
	"""
	curr_dir = os.getcwd()
	with open(curr_dir + '/random_text_file.txt', 'r') as file:
		all_lines = file.readlines()
		n = input('How many lines read from end in rand file?\n')
		if n.isnumeric():
			n = - int(n)
			return all_lines[n:]  # last n lines


def main():
	"""
	Starts all
	"""
	gen_rand_file()
	last_lines = read_last_n()
	for p, el in enumerate(last_lines):
		last_lines[p] = el[:-2]
	for line in last_lines:
		print(line)


if __name__ == '__main__':
	main()
