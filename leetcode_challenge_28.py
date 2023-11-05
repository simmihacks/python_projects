def sum_diagonals(size):
	total = 1
	last = 1
	for i in range((size - 1) / 2):
		diff = 2 * i + 2
		print(diff, last, total)
		total += last*4 + diff * 10
		last = 4 * diff + last
	return total

print(sum_diagonals(1001))
