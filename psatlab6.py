list1=[]
n=int(input('the no of items bailey had='))
for i in range(n):
    f=int(input('enter 1 for carrot, 2 for royal canin and 3 for toblerone'))
    list1.append(f)
a=list1.index(3)
b=a+1
if list1[b]==3:
    print('Yes')
else:
    print('No')
