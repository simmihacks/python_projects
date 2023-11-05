import math

remaining_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

permutation_number = 1000000
current_permutation = []

while permutation_number > 1:

	index = 0
	while index * math.factorial(len(remaining_digits) - 1) < permutation_number:
		index += 1
	index = index - 1
	
	permutation_number -= index * math.factorial(len(remaining_digits) - 1)
	print(len(remaining_digits), index, permutation_number, "appending", remaining_digits[index])

	current_permutation.append(remaining_digits[index])
	del remaining_digits[index]
print(''.join(current_permutation + remaining_digits))
