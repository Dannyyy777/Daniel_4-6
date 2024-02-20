x = list(input("Enter a word = "))
y = list(input("Enter another word to check for anagram = "))

x.sort()
y.sort()

if x == y:
    print("True")
else:
    print("False")
