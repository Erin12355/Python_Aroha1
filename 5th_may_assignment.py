# lst1=[10,20,30,50,10,20,60,10]
# # dup=[]
# # for i in range(len(lst1)):
# #     if lst1.count(lst1[i])>1:
# #         if lst1[i]not in dup:
# #             dup.append(lst1[i])
# # for j in dup:
# #     while True:
# #         if j in lst1:
# #             if lst1.count(j)>1:
# #                 lst1.remove(j)
# #             else:
# #                 break
# #         else:
# #             break
# # print(lst1)
# count=0
# for i in range(len(lst1)):
#     while True:
#         if lst1.count(lst1[i-count])>1:
#             lst1.remove(lst1[i-count])
#             count+=1
#         else:
#             break
# print(lst1)

##==========================================================================================

# lst1=[10,20,30,4,44]
# lst2=['a','c','e']
# lst3=[11,22,33,44,55,66]
# for i,j,k in zip(lst1,lst2,lst3):
#     print(i,j,k)
0
##==========================================================================================

# dict1={101:'jaeson',102:'jimmy'}
# dict2={103:'baikunta',104:'yaswant'}
# dict1.update(dict2)
# print(dict1)


import re
count=0   
pattern=re.compile("aba")   
matcher=pattern.finditer("abababa")   
for match in matcher:   
    count+=1   
    print(match)
    print(match.start(),"...",match.end()-1,"...",match.group())   
print("The number of occurrences: ",count)

 
matcher=re.finditer('[^abc]',"a7b@ck9z")   
for match in matcher:   
    print(match.start(),"......",match.group())

