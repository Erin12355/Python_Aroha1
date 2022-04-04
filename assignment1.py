## 1. create a Item class which should have 
##    item id, name , cost price of the item
##    item catogery, selling price
##    selling price is decided on the following way
##    for cateogry A type of item it is 8.5% profit
##    SP = CP + (CP * profit%)
##    for cateogry B type of item it is 12.5% profit
##    SP = CP + (CP * profit%)
##   display the item details with the SP

class Shop:
    def dis():
        item_id=input("Enter the Item Id: ")
        name=input("Enter the item name : ")
        while True:
            try:
                cp=float(input("Enter the cost price : "))
            except:
                print("Invalid cost price!!!")
            else:
                break
        while True:
                catg=input(""" Choose the Profit Category :- 
                A. 8.5% 
                B. 12.5% \n""")
                if catg=='A' or catg=='a':
                    sp=cp+((8.5/100)*cp)
                    print("ITEM ID : ",item_id,"\nITEM NAME : ",name,"\nCOST PRICE : ",cp,"\nSELLING PRICE IS : ",sp,"\nSelling at the profit of 8.5%")
                    break
                elif catg=='B' or catg=='b':
                    sp=cp+((12.5/100)*cp)
                    print("ITEM ID : ",item_id,"\nITEM NAME : ",name,"\nCOST PRICE : ",cp,"\nSELLING PRICE IS : ",sp,"\n Selling at the profit of 12.5%")
                    break
                else:
                    print("Invalid Category!!!")
                    exit=input("If you want to EXIT the process press 'y' \n")
                    if exit=='y':
                        break
a=Shop
a.dis()

##---------------------------------------------------------------------------------------------------------------------------

# # 2. Enter a number or assign a number in a class called Prime
# #    determine whether it is Prime or Not Prime
# #    for example 
# #    p1 = Prime(10)
# #    p1.display()   output is 10 is NOT Prime
# #    p2 = Prime(29)
# #    p2.display()  output 29 is PRIME

class Prime:
    def __init__(self,x):
        self.x=x
        flag=False
        for i in range(2,self.x):
            if self.x%i==0:
                flag=True
                break
        if flag==False:
            print(self.x," is PRIME number ")
        else:
            print(self.x,' is NOT PRIME number ')
res=Prime(10)
res2=Prime(29)

#---------------------------------------------------------------------------------------------------------------

## 3. assign a char say * and how many times it should be printed
##    say 15
##    print the * that many times 
##    p1 = Pattern('*',10)
##    p1.display()
##   * * * * * * * * *
  
class Pattern:
    def __init__(self,char,times):
        self.char=char
        self.times=times
    def display(self):
        print(self.char*self.times)
res=Pattern('*',10)
res.display()

##------------------------------------------------------------------------------------------

# # 4. Assign a year and check whether it is Leap or not Leap
# #    a1 =  Leap(1999)
# #    a1.display()  .... Not Leap

class Leap:
    def __init__(self,year):
        self.year=year
    def display(self):
        if (self.year%100==0 and self.year%400==0) or (self.year%100!=0 and self.year%4==0):
            print(self.year," is Leap Year ")
        else:
            print(self.year," is not Leap Year ")
res=Leap(1999)
res.display()