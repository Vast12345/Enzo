tuition = 10_000

sum_num = 0

while tuition <= 20_000:
    tuition *= 1.07
    sum_num += 1


print(f"It takes {sum_num} years for the tuition to reach $20,000")

