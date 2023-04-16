list1=[]
n1=int(input('enter no of elements for list1='))
s1=0
for i in range(n1):
    x1=int(input('enter element for list1='))
    s1+=x1
    list1.append(x1)
list2=[]
n2=int(input('enter no of elements for list2='))
s2=0
for j in range(n2):
    x2=int(input('enter element for list2='))
    s2+=x2
    list1.append(x2)

if n1==n2:
    print('the lists are of same length')
else:
    print('the lists arent of same length')

if s1==s2:
    print('sum of numbers is same in both lists')
else:
    print('sum of numbers isnt same in both lists')

list3=[]
for k in list1:
    if k in list2:
        list3.append(k)
print(list3)
  
