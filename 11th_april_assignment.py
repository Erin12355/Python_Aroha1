# # # 1) input any 5 numbers and store in set
# # #    find the highest number
# # #    find the lowest number
# # #    find the avg of all the numbers
# # #    display the set in DESC order of numbers

# # 2) once 1 is working
# #    convert the set to the list - call it list1
# #    given list2 = [89,23,67,22,100,105,15]
# #    process the list2 and add it into the list1
# #    in the last 5 elements find the highest
# #    in the first 6 elements find the lowest
# #    find the avg of all the list1 elements
# #    how many numbers are above the avg ?

# from statistics import mean
# def num_set(num1):
#     highest=max(num1)
#     lowest=min(num1)
#     average=mean(num1)
#     print("Highest number from the given set is : ",highest)
#     print("Lowest number from the given set : ",lowest)
#     print("Average number is : ",average)
# def num_set2(num1,num2):
#     num1_lst=list(num1)
#     num_add=num1_lst+num2
#     hig=0
#     low=float('inf')
#     for i in num_add[-5:]:
#         if i>hig:
#             hig=i
#     print(hig)
#     for j in num1_lst[0:6]:
#         if j<low:
#             low=j
#     print(low)
#     average=mean(num1)
#     print(average)

# def init():
#     x=1
#     num1=set()
#     while x<=5:
#         try:
#             n=int(input("Enter the number : \n"))
#             num1.add(n)
#             x+=1
#         except :
#             print("invalid input !! Enter a number ")
#     return num1

# num2=[89,23,67,22,100,105,15]
# ini=init()
# num_set(ini)
# num_set2(ini,num2)


    

# # 3) st1 = {'Java','Python','C'}
# #    st2 = {'SQL','Java','C#','Python'}
# #    to the st1 add those elements from st2 which is not there in st1
# #    remove the skill 'Java' from both st1, st2
# #    add the skills st3 = {'SQLServer','ASP.net','AWS'}
# #    into both st1 and st2 using for loop
# #    display the st2 in DESC order of sorting

# st1 = {'Java','Python','C'}
# st2 = {'SQL','Java','C#','Python'}
# st3 = {'SQLServer','ASP.net','AWS'}
# def set_exe(s1,st2,st3):
#     for i in st2:
#         if i not in st1:
#             st1.add(i)
#     st1.remove('Java')
#     st2.remove('Java')
#     for j in st3:
#         st1.add(j)
#         st2.add(j)
#     print("Before sorting st2 : ")
#     print(st2)
#     st2=list(st2)
#     st2.sort()
#     print("After sorting st2 : ")
#     print(st2)
# set_exe(st1,st2,st3)
print("hello")
