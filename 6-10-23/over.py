a=int(input("enter the number limit:"))

b=[]
v="over"
for i in range(0,a):
    first=int(input("enter the number:"))
    if first<99:
        b.append(first)
    else:
        b.append(v)

print(b)
