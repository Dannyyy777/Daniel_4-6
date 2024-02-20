l1 = list(input("Enter a number = "))
print(l1)

a = int(l1[0])
b = int(l1[1])
c = int(l1[2])

if a > b:
    print(f"{a} is greater!")
elif b > c:
    print(f"{b} is greater!")
else:
    print(f"{c} is greater!")

