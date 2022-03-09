# print('-------Calculator-------')
# a = int(input('Enter your divisor: '))
# b = int(input('Enter your dividend: '))
# c = a+b
# d = b-a
# e=a*b
# f=b/a
#
# print('Select mode for calculation\n press 1 for add \n press 2 for sub\n press 3 for division\n press 4 for multiplication')
# val = int(input('Enter your choice here!'))
# if val == 1:
#     print(c)
# elif val == 2:
#     print(d)
# elif val == 3:
#     print(f)
# elif val == 4:
#     print('Result of Multiplcation: ',e)
# else:
#     print('Kindly enter the valid number!!!')
#
# # Second code
#
# for x in range(11):
#     print('2','x',x,'=',2*x)

# pyramid
# star = int(input('Enter your divisor: '))
#
# for i in range(1,star):
#     print('0')
#
#     for j in range(i):
#         print('1',end='')
#
#     for m in range(i*1):
#         print('*',end='')
#

# rows = int(input("Enter number of rows: "))
# for i in range(rows, 0,-1):
# # for i in range(1, rows):
#     for j in range(0, i):
#         print("*", end=" ")
#
#     print("\n")

#-----Factorial Code ------
#
# num = int(input('Enter number for factorial here : '))
# fact = 1
# if num < 0:
#     print('Error! kindly enter valid number')
# elif num == 0:
#     print(1)
# else:
#     for i in range(1,num+1):
#         fact = fact * i
#     print('Your factorial result is ',fact)

# list1 = [['valley1',1],['valley2',2],['valley3',3],['valley4',4],['valley5',5]]
# dict1 = dict(list1)
# print(dict1)
# for ok,okk in list1:
#     print(ok,'->',okk)

# Swap variables without creating third variable.
a = 2
b = 3

a = a^b
print(a)
b = b^a
print(b)
a = a^b
print(a)

print('After swapping A to B---->>>>>',a)
print('After swapping B to A ---->>>>>',b)
