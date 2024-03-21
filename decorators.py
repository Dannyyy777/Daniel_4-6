i = 0
list_fname = []
list_lname = []
list_age = []
list_gender = []

num = int(input("Enter the number of people = "))
for i in range(num):
    fname = input("Enter first name = ")
    l1 = list_fname.append(fname)
    lname = input('Enter last name = ')
    l2 = list_lname.append(lname)
    age = input("Enter age = ")
    l3 = list_age.append(age)
    gender = input("Enter gender (M or F) = ")
    l4 = list_gender.append(gender)

    if gender == "M" or gender == "m":
        male = f"Mr. {fname} {lname} is {age}"
    else:
        female = f"Ms. {fname} {lname} is {age}"

if age[0] >= age[1]:
    print(male)
    print(female)
else:
    print(female)
    print(male)
