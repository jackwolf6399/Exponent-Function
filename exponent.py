def power(base, exponent):
	
	""" Takes the base value that is given and raises it the the given exponent value """
	
	# make a loop that multiplies the base exponent amount of times
	loop = 0
	baseOne = 1
	if exponent!= 0:	
		while loop < exponent:
			answer = baseOne * base
			loop += 1
			baseOne = answer
	else:
		answer = 1
	
	return answer
			
# ---- Main program ---- #
base = int(input("Choose an integer as your base: "))
exponent = int(input("Choose an integer as your exponent: "))

number = power(base, exponent)

print("Your new number is {}.".format(number))