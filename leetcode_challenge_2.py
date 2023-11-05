prev = 1
curr = 2

result = 0

while prev < 4000000:
	print prev, curr
	curr = curr + prev
	prev = curr - prev
	if prev % 2 == 0:
		result += prev

print(result)