import math
list1=[]
list2=[]
n=int(input('enter no of elements='))
for i in range(n//2):
    x=int(input('enter elements for list='))
    list1.append(x)
for j in range(math.ceil(n/2),n):
    y=int(input('enter elements for list='))
    list2.append(y)
list2.extend(list1)
print(list2)
