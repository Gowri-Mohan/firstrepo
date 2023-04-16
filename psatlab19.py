list1=[]
list2=[]
n=int(input('enter no of elements='))
for i in range(n):
    x=int(input('enter element for list1='))
    list1.append(x)
    if list1.count(x)>2:
        list2.append(x)
for j in list1:
    if j in list2:
        list1.remove(j)
print(list1)
print(list2)
