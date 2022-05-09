# ## WITHOUT USING SPLIT 
# main_str='hi i am jaeson'
# final=''
# substr=''
# for i in range(len(main_str)-1,-1,-1):
#     if main_str[i]!=' ':
#         substr=main_str[i]+substr
#     elif main_str[i]==' ' :
#         final+=substr+' '
#         substr=''
#     if i==0:
#         final+=substr
# print(final)
# ##========output====================
# ## jaeson am i hi
# ##==================================
# ## WITH SPLIT
# main_str='hi i am jaeson'
# lst1=main_str.split()
# for i in range(len(lst1)-1,-1,-1):
#     print(lst1[i],end=' ')     
# ##========output====================
# ## jaeson am i hi
# ##==================================

# a='hi good morning team'
# b=input("Enter the letter you want to count: ")
# count=0
# for i in a :
#     if i==b:
#         count+=1
# print(count)
a='hi jaeson'
print(a.count('5'))