# import math
# n1 = 1
# n2 = 1
# sign = -1
# print(n1, n2, end=", ")
# for i in range(5):
#     s = n1 + (sign**i) * n2
#     n1 = n2 
#     n2 = s
#     print(s, end=", ")


def number():
    while True:
        try:
            n = int(input("Input a number greater than or equal to 1: "))
            if n < 1:
                print("Invalid: number must be greater than or equal to 1.")
                input()
                continue
            return n
        except ValueError:
            print("Error: input must be a number.")
            input()


def Series(list, n):
    dataList = {}
    for i in range(1, n+1):
        add = 1/i
        dataList[f"num{i}"] = add
    
    list.append(dataList)


# def calculation(list):
#     for i in list[0]:
#         num1 = list[0][0]
#         num2 = 1/(i+2)
#         sign = -1
#         sum = num1 + (sign**i) * num2
#         num1 = num2
#         num2 = sum
#         print(sum, end=", ")




def calculation(list):
    dic = list[0]
    for k, v in dic.items():
        num = v
        sign = 1
        result = 0
        result += sign * num

        sign *= -1

    return result
     

List = []
Series(List, number())
print(List)
sum = calculation(List)
print(f"Result is: {sum}")



