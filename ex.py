def power(base, exponent):
	''' gives the result of a number to any power '''
	
	if exponent == 0:
		return 1
	answer = base * power(base, exponent - 1)
	
	return answer
	
	
	
# ---- Test cases ---- #
print("2 to the power of 5 is {}".format(power(2,5)))
print("3 to the power of 0 is {}".format(power(3,0)))
print("5 to the power of 3 is {}".format(power(5,3)))


# ---- Main program ---- #
print("Choose a base number  ")
base = int(input()
print("Raise it to an exponent  ")
exponent = int(input())

answer = power(base, exponent)
print("Your answer is {} ".format(answer))