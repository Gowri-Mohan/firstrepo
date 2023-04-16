list1=[]
list2=[]
m=int(input('enter no of elements of list1='))
n=int(input('enter no of elements of list2='))
for i in range(m):
    x=int(input('enter element for list1='))
    list1.append(x)
for i in range(n):
    y=int(input('enter element for list2='))
    list2.append(y)
for k in list1:
    if k not in list2:
        print(k)
    
