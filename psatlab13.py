list1=[]
m=int(input('enter no of elements for list1='))
for i in range(m):
    x=int(input('enter element for list1='))
    list1.append(x)
list2=[]
n=int(input('enter no of elements for list2='))
for j in range(n):
    y=int(input('enter element for list2='))
    list1.append(y)
e=int(input('enter the number that should be the sum of the pair='))
for k,l in [list1,list2]:
    if e==k+l:
        print(k,l)
    

