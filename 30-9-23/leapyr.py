year=int(input("Enter year to be checked"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("the year is leap year!")
else:
    print("the year is not an leap year")
