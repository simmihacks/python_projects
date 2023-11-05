import math

def countDigits(num):
	digits = 0
	while num != 0:
		num /= 10
		digits += 1
	return digits

def getNthDigit(num, digit):
	# print(num, digit, num / 10^(digit) % 10)
	return num / 10**(digit) % 10

def isPalindrome(num):
	right = 0
	left = countDigits(num) - 1

	while left > right:
		if getNthDigit(num, left) != getNthDigit(num, right):
			return False
		left -= 1
		right += 1
	print(num, "is palindrome")
	return True

max_product = float("-inf")

for larger in range(999, -99, -1):
	for smaller in range(larger - 1, 99, -1):
		prod = larger * smaller
		print(larger, smaller, prod)
		if isPalindrome(prod):
			max_product = max(max_product, prod)

print(max_product)
	