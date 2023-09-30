a=int(input(" enter current year"))
b=int(input("enter final year"))

if a<b:
    print("list of leap years between",a,"to",b,"is:")
while a<b:
    if (a%4==0)&(a%100!=0):
        print(a)
    if (a%100==0)&(a%400==0):
        print(a)

    a=a+1
if a>=b:
    print("check your input again")
