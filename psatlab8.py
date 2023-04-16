list1=[]
n=int(input('enter no of elements='))
for i in range(n):
    x=int(input('enter element='))
    list1.append(x)
print(list1)
list1.remove(x)
list1.insert(0,x)
print(list1)
