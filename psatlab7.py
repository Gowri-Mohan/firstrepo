n=int(input('enter the no of elements='))
list1=[]
list2=[]
list3=[]
for i in range(n):
    x=int(input('enter element in list1='))
    list1.append(x)
for j in range(n):
    y=int(input('enter element in list2='))
    list2.append(y)
for k in range(n):
    z=x+y
    list3.append(z)
print(list3)
