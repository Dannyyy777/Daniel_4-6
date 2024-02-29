f = open("m4.jpg", "rb")
bin = f.read()

f1 = open("m4_bin.txt", "a")
f1.write(str(bin))
f1.close()

f2 = open("m4_bin.txt", "r")
print(f2.read())