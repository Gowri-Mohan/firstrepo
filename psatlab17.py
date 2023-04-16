list1=[]
n=int(input('enter no of elements='))
c=0
for i in range(n):
    x=input('enter element for list1=')
    list1.append(x)
    if len(x)>3:
       c+=1
print(list1)
print(c)
       
