lst=[]
n=int(input("Enter number of elements : "))
for i in range(0,n):
    ele = input("enter colours:")
    lst.append(ele)  
    print(lst)
print("The first and last elements are:",lst[0],lst[-1])
