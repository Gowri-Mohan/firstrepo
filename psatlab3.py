n=int(input('enter the no of elements='))
x=int(input('enter number x='))
list1=[]
for i in range(n):
    e=int(input('enter element='))
    list1.append(e)
print(list1)
if e>=x:
    c=list1.count(e)
    c+=c
    print(c)
