# Fizz Buzz
# ---------
# Given a random number as an input to a function, return "FIZZ" if the number is even and "BUZZ" if the number is odd

def fizzbuzz(number):
    if number % 2 == 0:
        return "FIZZ"
    else:
        return "BUZZ"


print(fizzbuzz(2))
print(fizzbuzz(333))
