a=str(input("Enter the sentence:"))
b=str(input("Enter the word you want to count:"))
ls=a.split()
count=0
for i in ls:
    if i==b:
        count=count+1
print("number of ",i,"is",count)
