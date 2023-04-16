list1=[]
n=int(input('enter no of elements='))
for i in range(n):
    x=int(input('enter element='))
    list1.append(x)
    if list1[i]>10:
        list1[i]=10
print(list1)
