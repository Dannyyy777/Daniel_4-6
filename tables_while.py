num = int(input("Enter a number = "))
num_2 = int(input("Enter ending number = "))
i = num
j = 1
while i <= num_2:
    while j <= 10:
        print(f"{i} x {j} =", i * j)
        j += 1
    i += 1
    j = 1
