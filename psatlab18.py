list1=[]
n=int(input('enter no of elements='))
k=int(input('enter element to be searched='))
for i in range(n):
    x=int(input('enter element for list1='))
    list1.append(x)
    
#unsortedlist
print(list1.index(k))

#sortedlist
list1.sort()
first=0
flag=0
last=n-1
while first<=last:
    middle=(first+last)//2
    if k==list1[middle]:
        flag=1
        break
    elif k>list1[middle]:
        first=middle+1
    elif k<list1[middle]:
        last=middle-1
if flag==1:
    print('found',k)
else:
    print('not found')


