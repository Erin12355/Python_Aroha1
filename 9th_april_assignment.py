
# # 1. enter the inital meter reading 
# #    enter the final meter reading
# #    enter D for Domestic or C for commercial
# #    ask whether the bill payment is done after the due
# #    date ? if yes then Fine is applied else no fine
# #    calc
# #    for the domestic category - ask whether Solar pannels are there
# #    for water heating - if yes then give a discount in the bill of 2%
# #    otherwise no discount.

# #    Domestic category
# #         units
# #        1 to 1000     1.90/unit
# #      1001 to 2500    2.85/unit
# #      2501 ...        4.10/unit
# #     fine 5% of the bill amt
 
# #     commercial category      
# #      1 to 2000       2.25/unit
# #     2001 to 5000     3.75/unit
# #     5001 to 8000     4.90/unit
# #     8001 ...         6.15/unit
# #     fine is 10% of the bill amt

# from datetime import *
# while True:
#     while True:
#         try:
#             initial=int(input("Enter your Initial meter number :\n"))
#             break
#         except ValueError:
#             print("Enter a valid number !!")
#     while True:
#         try:
#             final=float(input("Enter your final meter number : \n"))
#             break
#         except ValueError:
#             print("Enter a valid number !!")
#     if final-initial>=1:
#         break
#     else:
#         print("Invalid Meter Calculation!!!")
# class Category:
#     def __init__(self):
#         self.due=False
#         while True:
#             self.catg=input("""Choose the category :
# 1. Enter D for Domestic 
# 2. Enter C for commercial\n""")
#             if self.catg=='D' or self.catg=='C':
#                 break
#             else:
#                 print("Invalid category Enter again!!")
#         if self.catg=='D':
#             print("Enter the due date for Domestic Category ")
#             self.due_check()
#         elif self.catg=='C':
#             print("Enter the due date for Commercial category")
#             self.due_check()
#         return self.catg,self.due
#     def due_check(self):
#         while True:
#             try:
#                 self.year=input("Enter year in number (eg:2000) \n")
#                 self.day=input("Enter Day number (eg: 15)\n")
#                 self.month=input("Enter month in number (eg: 12)\n")
#                 self.due_date=datetime(int(self.year),int(self.month),int(self.day))
#                 break
#             except:
#                 print("Invalid date Enter again!")
#         self.today = datetime.now()
#         print("today",self.today)
#         print("due",self.due_date)
#         if self.today>self.due_date:
#            self.due=True
#            print("due")
#         else:
#             self.due=False
#             print("not")
#         print(self.year,self.day,self.month)
# class MeterCal(Category):
#     def __init__(self,initial,final):
#         self.initial=initial
#         self.final=final
#         self.res=self.final-self.initial
#         self.catg,self.due=super().__init__()
#         self.bill=0
#     def calc(self):
#         if self.catg=='D':
#             solar=input("Enter 'y' if you use solarpannel and enter any if you don't use :\n")
#             if self.res>=1 and self.res<=1000:
#                 self.bill=1.90*self.res
#             elif self.res>1000 and self.res<=2500:
#                 self.bill=2.85*self.res
#             elif self.res>2500 :
#                 self.bill=4.10*self.res   
#             if solar=='y':
#                 self.bill=self.bill-((2/100)*self.bill)
#             else:
#                 self.bill=self.bill
#             if self.due==True:
#                 self.bill=self.bill+((5/100)*self.bill)
#         elif self.catg=='C':
#             if self.res>=1 and self.res<=2000:
#                 self.bill=2.25*self.res
#             elif self.res>2000 and self.res<=5000:
#                 self.bill=3.75*self.res
#             elif self.res>5000 and self.res<=8000:
#                 self.bill=4.90*self.res
#             elif self.res>8000:
#                 self.bill=6.15*self.res
#         return self.bill 
# bill=MeterCal(initial,final)
# print("Electric Bill : ",bill.calc())

# #----------------------------------------------------------------------------------------------------------
# # 2. Display all the numbers in the range say 345 to 590
# #    (range could be anything ...)
# #    Find out how many numbers are not divisible by 7
# #    how many prime numbers are there in that range
# #    how many numbers are divisible by BOTH 3 as well as 4
# #    add the FIRST and the LAST number of the range and print the sum

def numbers():
    while True:
        try:
            ini=int(input("Enter the Initial number \n"))
            break
        except:
            print("INVALID INPUT !! Enter again")
    while True:
        try:   
            fin=int(input("Enter the Final number \n"))
            break
        except:
            print("INVALID INPUT!! Enter again ")
    return ini,fin
ini,fin=numbers()
def display_range(ini,fin):
    n_div_7=0
    div_3_4=0
    sum=ini+fin
    prime=0
    step=end=0
    if ini>fin:
        step=-1
        end=fin-1
    else:
        step=1
        end=fin+1
    for i in range(ini,end,step):
        flag=False
        print(i,end=" ")
        if i%7!=0:
            n_div_7+=1
        if i%3==0 and i%4==0:
            div_3_4+=1
        for j in range(2,i):
            if i%j==0:
                flag=True
                break
        if flag==False:
            prime+=1
    return div_3_4,n_div_7,sum,prime
div_3_4,n_div_7,sum,prime=display_range(ini,fin)
print()
print("divisible by BOTH 3 as well as 4 : ",div_3_4)
print("not divisible by 7 : ",n_div_7)
print("Sum of the FIRST and the LAST number of the range : ",sum)
print("prime numbers in that range : ",prime)

# #---------------------------------------------------------------------------------------------------------------

