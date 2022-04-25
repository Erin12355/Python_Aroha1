# # 1) data1= [ 100,200,'500','6501',400]
# #    process the data1 (hint use type and int)
# #    add all the numbers , find the sum, avg, min and max
# #    use for loop

# import math
# data1= [ 100,200,'500','6501',400]
# sum=count=hig=0
# low=math.inf
# for i in data1:
#     if type(i)==int:
#         sum+=i
#         count+=1
#         if i>hig:
#             hig=i
#         if i<low:
#             low=i
#     else:
#         try:
#             i=int(i)
#             sum+=i
#             count+=1
#             if i>hig:
#                 hig=i
#             if i<low:
#                 low=i
#         except:
#             pass
# print('total= ',sum)
# print('highest= ',hig)
# print('Lowest= ',low)
# print('Average= ',sum/count)


# # 2) data2 = (10,22,[45,33,78],[90,99],(10,12,44,100),35,99)
# #    note the above tuple could have lists and other tuple
# #    HINT use type to process using the for loop
# #    Find the total, max, min, avg

# import math
# data2 = (10,22,[45,33,78],[90,99],(10,12,44,100),35,99)
# sum=count=hig=0
# low=math.inf
# for i in data2:
#     if type(i)==int:
#         sum+=i
#         count+=1
#         if i>hig:
#             hig=i
#         if i<low:
#             low=i
#     elif type(i)==list:
#         for j in i:
#             if type(j)==int:
#                 sum+=j
#                 count+=1
#                 if j>hig:
#                     hig=j
#                 if j<low:
#                     low=j
#     elif type(i)==tuple:
#         for k in i:
#             if type(k)==int:
#                 sum+=k
#                 count+=1
#                 if k>hig:
#                     hig=k
#                 if k<low:
#                     low=k
# print('Total= ' ,sum)
# print('Highest= ',hig)
# print('Lowest= ',low)
# print('Average= ',sum/count)



# # 3) 
# #    Write user defined functions 
# #    generate 100 random numbers in the range of 1 to 1000
# #    store all the numbers less than or equal to 500 in 
# #    set_500 and others in set_1000
# #    store all the odd_numbers in the set_odd and even in set_even
# #    find the max odd number
# #    find the min even number
# #    find the avg of all the even numbers
# #    Sort the set_odd, in that find the avg of last 10 highest numbers
# #    in the set_odd

# import random
# #generate 100 random number from 1 to 1000
# randomlist = random.sample(range(1, 1000), 100)
# print(randomlist)
# def demo(randomlist):
#     set_500=set()
#     set_1000=set()
#     set_odd=set()
#     set_even=set()
#     for i in randomlist:
#         if i <=500:
#             set_500.add(i)
#         elif i<=1000:
#             set_1000.add(i)
#         if i%2==0:
#             set_even.add(i)
#         elif i%2!=0:
#             set_odd.add(i)
#     print('max among the odd number : ',max(set_odd))
#     print('Minimum among the even number : ',min(set_even))
#     print('Average of the even number : ',sum(set_even)/len(set_even))
#     set_odd=list(set_odd)
#     set_odd.sort()
#     odd_sum=0
#     for i in range(len(set_odd)-10):
#         odd_sum+=i
#     print('Average of the last 10 highest in odd set : ',odd_sum/10)
# demo(randomlist)


# # 4) input the sentence into a string
# #    convert the sentence into upper case
# #    use the converted upper case string for the following...
# #    convert the string to the list (HINT use split)
# #    sort the list
# #    store the word having more than 3 or more vowels in the set
# #    set_vowel
# #    create a dict with keys as 100 and 200
# #    100 indicates that all the words starting with A to M will be 
# #    stored as set against the key 100
# #    200 indicates that all the words starting with N to Z will be stored 
# #    against the key 200
# #    example...
# #    100 :  {'AND','LIVING','DIETY','GARDEN',.....}
# #    200 :  {'NEITHER', 'ODD', 'PROFESSIONAL','ZUBEN','X-MAS','VIOLIN',...}

# sen='Hello good morning to all the Aroha Member'
# sen=sen.upper()
# print(sen)
# sen_list=sen.split()
# sen_list.sort()
# set_vowel=set()
# dict1={100:set(),200:set()}
# for i in sen_list:
#     count=0
#     for j in i:
#         if j in 'AEIOU':
#             count+=1
#     if count>=3:
#         set_vowel.add(i)
#     if i[0]>='A' and i[0]<='M':
#         dict1[100].add(i)
#     elif i[0]>'M' and i[0]<='Z':
#         dict1[200].add(i)
# print('word having 3 or more than 3 vowels : ',set_vowel)
# print(dict1)