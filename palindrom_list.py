l1 = ["racecar","madam","english","apple","noon"]
print(l1)
x = len(l1)
l2 = []
for i in range(x):
    a = l1[i]
    b = a[::-1]
    if a == b:
        l2.append(b)
print(l2)