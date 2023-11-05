import math

def count_divisors(num):
	if num == 1:
		return 1
	count = 0
	for i in range(1, int(math.sqrt(num)) + 1):
		if num % i == 0:
			if i == math.sqrt(num):
				count += 1
			else:
				count += 2
	return count

curr = 1
while True:
	curr_sum = sum(range(1, curr + 1))
	count = count_divisors(curr_sum)
	if count > 500:
		print(curr_sum)
		break
	curr += 1

