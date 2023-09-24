# Cycle For
#for i in range(10):
#    print(i, end=", ")


for i in range(6):
    print("*", end="")


print("")
for i in range(3):
    print("*    *") 


for i in range(6):
    print("*", end="")




lines = int(input("How many lines would you want to add: "))

for i in range(1, lines+1):
    ast = ("*" * (i))
    print(ast)