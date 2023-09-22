
number = int(input("Type the first number: "))
number2 = int(input("Tyoe the second number: "))
number3 = int(input("Type the third number: "))



if number >= number2 and number >= number3:
    if number2 >= number3:
        print(number, number2, number3)
    else:
        print(number, number3, number2)
elif number2 >= number and number2 >= number3:
    if number >= number3:
        print(number2, number, number3)
    else:
        print(number2, number3, number)
elif number3 >= number2 and number2 >= number:
    print(number3, number2, number)
    if number >= number2:
        print(number3, number, number2)
else:
    print("Error")
