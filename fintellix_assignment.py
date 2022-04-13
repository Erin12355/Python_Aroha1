# # 2. a=[1,24,3,43,66,5]
# #    how to get [1,3,5] only as a list

# # class One_digi:
# #     def __init__(self):
# #         self.list=[1,24,3,43,7,66,5]
# #         self.res=[]
# #     def find(self):
# #         for i in self.list:
# #             if i>0 and i<10:
# #                 self.res.append(i)
# #         return self.res
# # obj=One_digi()
# # obj_find=obj.find()
# # print(obj_find)

# # e=[[9,4],[3,5]] how to print e as [9,4,3,5]

# class TwoD_OneD:
#     def __init__(self):
#         self.list_2D=[[9,4],[3,5]]
#         self.list_1D=[]
#     def convr(self):
#         for i in self.list_2D:
#             if type(i)==list:
#                 for j in i:
#                     self.list_1D.append(j)
#             elif type(i)==int:
#                 self.list_1D.append(i)
#         return self.list_1D
# obj=TwoD_OneD()
# obj_convr=obj.convr()
# print(obj_convr)

# # write a programe to allow only if the str contains continues same letter. like apple contains two p
# # continuesly


# class Str_chk:
#     def __init__(self):
#         self.str=input("Enter a name : \n")
#     def chk(self):
#         len_str=len(self.str)
#         flag=False
#         for i in range(0,len_str-1):
#             if self.str[i]==self.str[i+1]:
#                 flag=True
#                 break
#         if flag==True:
#             print("Accepted!!")
#         else:
#             print("Decline, no repeated word !!")
# obj=Str_chk()
# obj.chk()