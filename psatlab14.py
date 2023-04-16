feet=int(input('enter the length in feet='))
choice=int(input('enter 0 for inches, 1 for yards, 2 for miles, 3 for millimeters, 4 for centimeters, 5 for metres and 6 for kilometres='))
list1=[feet*12,feet/3,feet/5280,feet*304,feet*30,feet/3,feet/3281]
print(list1[choice])
