import math

def sumOfDigits(num):
	sum_digits = 0
	for digit_string in str(num):
		sum_digits += int(digit_string)
	return sum_digits

print(sumOfDigits(math.factorial(100)))