
def fibonacci(n):
	prev = 0
	next = 1

	if n < 0:
		print("Incorrect input")

	elif n == 0:
		return 0
	
	# Check if n is equal to 1
	elif n == 1:
		return b
	else:
		for i in range(1, n):
			curr = prev + next
			prev = next
			next = curr

			print(next, end = ",")
		# return next

print(fibonacci(10))





