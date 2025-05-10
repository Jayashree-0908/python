salary=int(input("salary:"))
age=int(input("age:"))
if(salary>=20000 or age<25):
    loan=int(input("loan:"))
    if(loan<50000):
        print("you r eligible")
    else:
        print("not eligible")
else:
    print("not applicablle")
