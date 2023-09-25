perf_num = int(input("Enter a number to determine whether it is a perfect number or not: "))

sum_div = 0

if perf_num <= 0:
    print("Invalid number.")
else:
    for i in range(1, perf_num):   
        if perf_num % i == 0:
            sum_div += i
        
        
    
if sum_div == perf_num:
    print("Your number is a perfect number")
else:
    print("Your number is not a perfect number")