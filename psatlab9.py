list1=[]
n=int(input('enter no of elements='))
for i in range(n):
    x=int(input('enter element='))
    list1.append(x)
for i in range(n):
    if list1[i]>list1[i-1] and list1[i]>list1[i+1]:
        print(list1[i])
    
    
