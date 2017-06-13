#Function to return fizz,buzz or fizzbuzz
def fizz_buzz(num):
	#check if number is divisible by both numbers
	if (num%3 == 0)and(num%5 == 0):
		return "FizzBuzz"
	#check if divisible by 3
	elif num%3==0:
		return "Fizz"
	#check if divisible by 5
	elif num%5==0:
		return "Buzz"
	else:
		return num

	

#print(fizz_buzz(3))
#print(fizz_buzz(5))
#print(fizz_buzz(15))
print(fizz_buzz(101))