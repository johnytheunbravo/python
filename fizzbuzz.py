# to write a program which prints the no 1 to 100
# for multiples of 3 print fizz instead of the no 
# fo rmultiples of 5 print "Buzz"
# for multiples of both 3 and 5 print "FizzBuzz"

# hint: %(modulo) tells you whats left over when you divide one number by another 
# ex number % 3 == 0

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 ==0:
        print("Buzz")
    elif number % 3 == 0:
        print("FizzBuzz")
    else:
        print(number)