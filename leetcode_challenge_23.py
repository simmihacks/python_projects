import math

def sum_divisors(num):
	total_sum = 0
	for i in range(1, int(math.sqrt(num)) + 1):
		if num % i == 0:
			if i == math.sqrt(num):
				total_sum += i
			else:
				total_sum += i + num / i
	return total_sum - num


max_num = 28123
abundants = set()
total = 0
for i in range(1, max_num + 1):
	for abundant in abundants:
		if i - abundant in abundants:
			total -= i
			break
	total += i
	if sum_divisors(i) > i:
		abundants.add(i)

print(total)
