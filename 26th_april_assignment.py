# 1) given a set1 = set()
#    populate the set with the following :
#    10 random numbers less than 500
#    25 random numbers above 1000 but less than 5000
#    15 random numbers - can be anything

#    convert the set to tuple. use comprehnsion to find the sum
#    of all the odd numbers
#    which is the highest even number?
#    how many numbers are divisible by 5 as well as 7 ? (it should not be
#    2-digit number, except that)
#    find the avg of the number which is in the range of 600 to 800
#    (both the range inclusive)

import random
set1=set()
for i in range(10):
    num1=random.randint(1,500)
    set1.add(num1)
print(set1)
for j in range(25):
    num2=random.randint(1000,5000)
    set1.add(num2)
print(set1)
for k in range(15):
    num3=random.randint(500,1000)
    set1.add(num3)
print(set1)
print(len(set1))

list1=list(set1)