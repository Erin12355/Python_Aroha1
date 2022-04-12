# # 1) given
# #   prod = { 100 : ['Laptop',45550,True], 200 : ['Mouse',2000,False] }
# #   key is 100
# #   value is list describing the item name, price and True indicates
# #   available in store, False not available
# #   write a function to add more products till the user type -1 to stop
# #   write a function display_all to iterate and display all the items
# #   which are AVAILABLE in the store
# #   write a function display_item which accepts the item code and if that
# #   item exists then display the details and if the item code is not there
# #   display ITEM not found
# #   have a function called item_not_available which has a dict
# #   by name itm_not_in store = { } which holds all the items with the 
# #   status False
# #   the code should be menu driven.....
# #   1. Add
# #   2. Display all
# #   3. display specific item
# #   4. Move item NOT avialable
# #   5. E X I T out of menu
# #   enter your choice .....

# prod = { 100 : ['Laptop',45550,True], 200 : ['Mouse',2000,False] }
# def add():
#     while True:
#         while True:
#             try:
#                 item_id=int(input("Enter the item id :\n"))
#                 if item_id not in prod:
#                     break
#                 else:
#                     print("Item_id is already exist")
#             except:
#                 print("Invalid item_id format it should be number ")
#         item_name=input("Enter the item name :\n")
#         while True:
#             try:
#                 price=float(input("Enter the price of the item :\n"))
#                 break
#             except:
#                 print("Invalid Price Enter again!!")
#         avai=input("Enter True if it is available to store or False if it is not :\n")
#         if avai=='False' or avai=='false':
#             avai=bool('')
#         else:
#             avai=bool(1)
#         print(avai)
#         prod.update({item_id:[item_name,price,avai]})
#         flag=input("Press ENTER to continue adding and -1 to exit\n")
#         if flag=='-1':
#             break
# def display_all(prod):
#     print("ITEM_NO"+' '*13,end='')
#     print("ITEM_NAME"+' '*23,end='')
#     print("PRICE"+' '*15,end="")
#     print("AVAILABLE TO STORE")
#     print('-'*100)
#     for i,j in prod.items():
#         print(i,' '*(20-len(str(i))),end='')
#         print(j[0],' '*(30-len(j[0])),end='')
#         print(j[1],' '*(20-len(str(j[1]))),end="")
#         print(j[2])
# def spec_display(prod):
#     while True:  
#         try:
#             search=int(input("Enter the item_id to search\n"))
#             if search in prod:
#                 print("ITEM_NO"+' '*13,end='')
#                 print("ITEM_NAME"+' '*23,end='')
#                 print("PRICE"+' '*15,end="")
#                 print("AVAILABLE TO STORE")
#                 print('-'*100)
#                 print(search,' '*(20-len(str(search))),end='')
#                 print(prod[search][0],' '*(30-len(prod[search][0])),end='')
#                 print(prod[search][1],' '*(20-len(str(prod[search][1]))),end="")
#                 print(prod[search][2])
#                 if prod[search][2]==False:
#                     print("Item is not avaliable to store now!!")
#                 else:
#                     print("Item is available to store now ....")
#             else:
#                 print("Item_id not found!!!")
#             break
#         except:
#             print("Invalid Item_id format!!! Enter again ")
# while True:
#     choose=input("Choose the option :\n1. Add item\n2. Display_all\n3.Display_Specific_item\n4. Exit\n")
#     if choose=='1':
#         add()
#     elif choose=='2':
#         display_all(prod)
#     elif choose=='3':
#         spec_display(prod)
#     elif choose=='4':
#         break
#     else:
#         print("Invalid Choose!! Choose again")


# #------------------------------------------------------------------------------------------------------

# # 2) have any text file (motivational.txt) , 
# #    created in notepad having few sentences
# #    say this one....
# #    *******
# #    Sudha Murthy was hardworking and determined to succeed in her studies, 
# #    which is why she emerged a topper in both her undergraduate and 
# #    postgraduate studies. After graduation, Sudha Murthy was hired by 
# #    TATA Engineering and Locomotive Company, also known as TELCO, 
# #    and she was the first female engineer in the company.
# #    At every stage in our lives, we come across immense challenges and 
# #    various forms of discrimination. But that should not discourage 
# #    us from performing our best. We should be determined and 
# #    strive to achieve success despite the obstacles we 
# #    face in life. And we should have the courage to fight and 
# #    eradicate policies that may stifle the growth of our country. 
# #    These are some of the lessons that we can learn from Sudha Murthy.
# #    ************* 
# #    open that file , find out how many words are there 
# #    which word is having the max length (there can be many words of the same length)
# #    have ALL those words
# #    Display the LAST 10 words from the file

# file=open('D:\Aroha_Tech\python_vishwanath\oops\Python_Aroha1\Python_Aroha1\motivational.txt','r')
# f=file.read()
# lst=f.split(' ')
# length=''
# for i in lst:
#     if len(i)>len(length):
#         length=i
# for j in lst:
#     if len(j)==len(length):
#         print(j)
# print(lst[-10:])

# #---------------------------------------------------------------------------------------------------------

# # 3. Store 'n' names in the a set (till the user types STOP), 
# #    sort the name set 
# #    how many names are there which starts from R to U
# #    display the last 2 char of the names from the set (use SLICING)
# #    How many names are there with Last name
# #    say the name can be Ravi Rao, Anish Kamath, Uday , Rashmi Bhat etc...

# def names():
#     names_set=set()
#     count=l_name=0
#     while True:
#         n=input("Enter the name: or 'STOP' to exit \n")
#         names_set.add(n)
#         if n=='STOP':
#             break
#     for i in list(names_set):
#         if i.startswith('R') or i.startswith('U'):
#             count+=1
#         if len(i.split(' '))>1:
#             l_name+=1
#     print("name starts with 'R' or 'U' : ",count)
#     print("Numbers of name that have last name : ",l_name)
# names()