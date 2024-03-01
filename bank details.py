import random
import datetime

name = input("Enter your name = ")

file = open("bankaccount.txt", "w")
file.write("-----------------------------------------------------------------------")
file.write("\n")
file.write(f"********************* Welcome {name}! to SBI Bank *********************")
file.write("\n")
file.write("-----------------------------------------------------------------------")
file.write("\n")

print("-------------------------------------------------------------")
print(f"**************** Welcome {name}! to SBI Bank ****************")
print("-------------------------------------------------------------")

print("1. Signup/Register with Bank")
print("2. Exit")
inp = int(input("Enter the option to proceed "))
#cnlist = []
#aclist = []
#pwlist = []
ba = 10000
mb = 2000

if (inp == 1):
    cn = input("Enter Customer Name: ")
    pw = int(input("Enter the password: "))
    pw1 = int(input("Re-Enter the password: "))
    if pw != pw1:
        print("Password not match, exiting...")
        exit()
    else:
        an = random.randint(1111111111111111, 9999999999999999)

        print("Account registered with below details. ")

        print(f"Cust. Name: {cn} \t", " "*33, datetime.datetime.today())
        print(f"Acc No.: {an}")
        dt = datetime.datetime.today()
        dt1 = str(dt)
        cust = f"Customer Name: {cn} \t" + " "*20 + dt1
        accno = f"Account Number: {an}"

        file.write(cust)
        file.write("\n")
        file.write(accno)
        file.write("\n\n")

        un1 = input("Enter UserName to Login: ")
        pd1 = input("Enter Password: ")
        if un1 == cn or pd1 == pw:
            print("Login Success ")
            print("-" * 70)
            print("Welcome to SBI, ", cn, "                 ", datetime.datetime.today())
            print("1.Credit ")
            print("2.Debit ")
            print("Performing Credit Operation")
            print("Balance before credit", ba)

            bal = f"Initial Balance = {ba} \n"
            file.write(bal)

            for i in range(3):
                da = int(input("Enter the amount to credit :"))
                ba = ba + da
                print("Total Balance after Deposit: ", ba)

            new_bal = f"After Credit = {ba} \n\n"
            file.write(new_bal)

            print("Performing Debit Operation")
            print("Balance before debit", ba)

            bal_1 = f"Balance before debit = {ba} \n"
            file.write(bal_1)

            for i in range(3):
                wa = int(input("Enter the amount to debit :"))
                ba = ba - wa
                if ba <= mb:
                    print("Low Balance:", mb, " No further debit allowed")
                    break
                else:
                    print()
                print("Total Balance after withdrawal: ", ba)

            new_bal1 = f"After Debit = {ba} \n\n"
            file.write(new_bal1)

            print("Balance After Transaction: ", ba)
            aft = f"Balance After Transaction = {ba} \n"
            file.write(aft)

            print("Interest Details @ 10% per Annum: ")
            stat = "Interest Details @ 10% per Annum: \n"
            file.write(stat)

            int1 = ba * 10 / 100
            tb = ba + (ba * 10 / 100)

            print("Interest Amount: ", int1)
            interest = f"Interest Amount = {int1} \n\n"
            file.write(interest)

            print("Total Balance: ", tb)
            total = f"Total Balance = {tb} \n"
            file.write(total)

            print("-" * 75)
            file.write("-----------------------------------------------------------------------")

        else:
            print("Invalid Credentials")
else:
    print("Exiting the program...")
    exit()

file.close()
