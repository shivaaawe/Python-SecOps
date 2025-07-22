def takatakatakatak():
    print("Hello")

#When I stop the code here and try to run it, it doesn't do anything.
#In order for functions to execute we need to call them

takatakatakatak()

#Putting our fuzzbuzz inside a function and also promting a user to choose a range

choice_start = int(input("Please enter the starting number: "))
choice_end = int(input("Please enter the ending number: "))

def fuzzbuzz(choice_start, choice_end):
    for num in range(choice_start, choice_end):
        if num % 3 == 0 and num % 5 == 0:
            print("FuzzBuzz")
        elif num % 3 == 0:
            print("Fuzz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fuzzbuzz(choice_start, choice_end)