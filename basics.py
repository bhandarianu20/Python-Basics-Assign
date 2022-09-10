# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
a=[]
for x in range(2000, 3201):
    if (x%7==0) and (x%5!=0):
        a.append(str(x))
print(a)
combinedString = ', '.join(a)
print(combinedString)

#2 python program for reverse name
fname = input('what is your first name?')
sname = input('what is your last name?')
print(sname + " "+fname)

#3 Volume of cone
pi = 3.1415926535897931
D=12
r= 6.0
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',V)
