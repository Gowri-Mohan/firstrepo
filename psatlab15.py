list1=[]
n=int(input('enter no of elements='))
for i in range(n):
    x=int(input('enter element for list1='))
    list1.append(x)
list1.remove(max(list1))
print (max(list1))
