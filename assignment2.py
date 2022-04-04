# April 4th assignment
# use the concept of if else, or , and , ladder if
# appropriately...
# ===
# 1. input a number and check whether the 
#    number is in this range or not
#    157 to 489  (FIRST RANGE)
#    if the number is not in the range then 
#    check whether the number is in this range
#    670 to 978
#    if it is then add 10 to it else add 15 to it
#    if the number is in the FIRST RANGE
#    then raise the number to the power of 3

# 2. input the avg of the student
#    and the category say 
#    G - General
#    D - Defence
#    O - Others
#    also input the year of passing 
#    the criteria for admission is as follwing 
#    For G the avg must be above 80 and the 
#    YOP must be 2021
#    For D the avg must be above 68 and the YOP
#    can be 2019 2020 or 2021
#    For O then avg must not be less than 60 and 
#    YOP could be 2020 or 2021

# 3. once solution 2 is working as above 
#    then add the following check
#    for the candidate who could not get in the above 

#    if the candidate parents/gurdian income is 
#    less than 80000 pa and they have passed after 2019
#    and thier avg is above 55 then grant admission
#    otherwise no admission

# *************


 
    

import time

##-----------------------1-----------------------------------------
num=int(input("Enter a number : "))
if num in range(157,489):
    res=num**3
elif num in range(670,978):
    res=num+10
else:
    res=num+15
print(res)


#----------------------2/3----------------------------------------------
avg=int(input("Enter the average mark : "))
catg=input("""Choose the category : 
G. General
D. Defence
O. Others \n""")
yop=input("Enter the Year of Passing : ")
inc=int(input("enter your parent annual income : "))
print("Checking.....")
time.sleep(3)
def else_con():
    if inc<80000 and int(yop)>2019 and avg>55:
            print("@ Qualified!!")
    else:
        print("Not Qualify !!")
if catg=='G':
    if avg>80 and yop=='2021':
        print("Qualify for admission ")
    else:
        else_con()
elif catg=='D':
    if avg >68 and (yop=='2019' or yop=='2020' or yop=='2021'):
        print("Qualified for admission !!!")
    else:
        else_con()
elif catg=='O':
    if avg>=60 and (yop=='2020' or yop=='2021'):
        print("Qualified!!")
    else:
        else_con()

