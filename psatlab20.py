list1=[]
n=int(input('enter no of food items='))
for i in range(n):
    x=input('enter food item=')
    list1.append(x)
for j in list1:
    c=list1.count(j)
    if c<2:
        print('bite')
    else:
        print('not bite')
    
