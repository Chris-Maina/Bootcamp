#Function to return fizz,buzz or fizzbuzz
def fizz_buzz(num):
	if num%3==0:
		return "Fizz"
	if num%5==0:
		return "Buzz"

print(fizz_buzz(3))
print(fizz_buzz(5))