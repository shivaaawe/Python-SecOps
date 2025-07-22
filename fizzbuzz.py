#FizzBuzz Challenge

#If a number is divisible by 3, print fizz
#If a number is divisible by 5, print buzz
#If a number is divisible by both, print fizzbuzz

#Taking user input
enter_a_number = int(input("Please enter a number : "))

if enter_a_number%3==0 and enter_a_number%5==0:
    print("FizzBuzz")
elif enter_a_number%5==0:
    print("Buzz")
elif enter_a_number%3==0:
    print("Fizz")
else:
    print(enter_a_number)

#Raginggg Range
for num in range(0,100):
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num%5==0:
        print("Buzz")
    elif num%3==0:
        print("Fizz")
    else:
        print(num)