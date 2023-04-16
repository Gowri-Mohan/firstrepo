n=int(input('enter the no of elements='))
list1=[]
list2=[]
for i in range(n):
    x=int(input('enter element='))
    list1.append(x)
for x in list1:
    s=x**2
    list2.append(s)
print(list1)
print(list2)
    
