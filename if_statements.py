fnum = input()
snum = input()

if fnum > snum:
    print(f"{fnum} is greater")
elif fnum < snum:
    print(f"{snum} is greater")
else:
    print(f"{snum} and {fnum} are same")


# Write a program that prompts the user to enter their score (out of 100) and displays
# the corresponding grade based ont the following criteria

# 90 and above A
# 80 - 89 B
# 70 - 79 C
# 60 - 69 D
# <60 F

user_grades = int(input("Please enter your marks out of 100 "))
if user_grades > 90 and user_grades < 100:
    print("A")
elif user_grades > 80 and user_grades < 89:
    print("B")
elif user_grades > 70 and user_grades < 79:
    print("C")
elif user_grades > 60 and user_grades < 69:
    print("D")
else:
    print("F")
