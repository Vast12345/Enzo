# Exercice 1
# Make a program in python that generates the following number sequence: 
# 1,1,2,-1,1,-2,

n1 = 1
n2 = 1
sign = -1
print(n1, n2, end=", ")
for i in range(5):
    s = n1 + (sign**i) * n2
    n1 = n2 
    n2 = s
    print(s, end=", ")