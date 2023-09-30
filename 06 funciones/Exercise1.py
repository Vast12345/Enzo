import math

# def Distancia(xt, yt, xs, ys):
#     d = math.sqrt((xt - xs)**2 + (yt - ys)**2)
#     return d
# x1 = 1
# x2 = 3
# y1 = 2
# y2 = 4
# dist = Distancia(x1, y1, x2, y2)
# print(f"The distance is {dist:.2f}")

# def Perimiter(xp, yp, xq, yq, xr, yr):
#     a = Distancia(xp, yp, xr, yr)
#     b = Distancia(xr, yr, xq, yq)
#     c = Distancia(xq, yq, xp, yp)
#     s = (a + b + c) 
#     return s

# x1 = 1
# y1 = 4
# x2 = 3
# y2 = 0
# x3 = 5
# y3 = 3
# per = Perimiter(x1, y1, x2, y2, x3, y3)
# print(f"The perimiter is {per:.2f}")

# def Discount(price):
#     if price > 150:
#         discount = price * 0.05
#     else:
#         discount = price
#     return discount

# num = float(input("How much did your item cost: "))

# discount = Discount(num)
# print(f"Your discount is ${discount:.2f}\nThe total price with the discount is ${num - discount:.2f}")


# def readResult(msj):
#         grade = msj
#         if grade < 1 or grade > 5:
#             print("Grade can only be between 1 and 5")
#         else:
#             return grade
def result(n1, n2, n3, n4, n5):
    win = (n1+ n2+ n3+ n4+ n5) / 5
    if win > 3.5:
        print("You passed")
    else:
        print("You failed")
    return win
        
# def result(n1, n2, n3, n4, n5):
#     win = (n1+ n2+ n3+ n4+ n5) / 5
#     if win > 3.5:
#         return True
#     else:
#         return False
    
grade1 = float(input("What was the score on your first test"))
grade2 = float(input("What was the score on your second test"))
grade3 = float(input("What was the score on your third test"))
grade4 = float(input("What was the score on your fourth test"))
grade5 = float(input("What was the score on your fifth test"))

grade = result(grade1, grade2, grade3, grade4, grade5)
print(grade)
    
# if result(grade1,grade2,grade3,grade4,grade5):
#   print("You passed")
# else:
#   print("You didn't pass")
        


