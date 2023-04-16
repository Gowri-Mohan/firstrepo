n=int(input('enter the no of elements='))
list1=[]
for i in range(n):
    x=int(input('enter element='))
    list1.append(x)
for j in list1:
    c=list1.count(j)
    print(c)
