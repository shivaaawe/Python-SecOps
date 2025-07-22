#FizzBuzz Challenge

#If a number is divisible by 3, print fizz
#If a number is divisible by 5, print buzz
#If a number is divisible by both, print fizzbuzz

enter_a_number = int(input("Please enter a number : "))

if enter_a_number%3==0 and enter_a_number%5==0:
    print("FizzBuzz")
elif enter_a_number%5==0:
    print("Buzz")
elif enter_a_number%3==0:
    print("Fizz")