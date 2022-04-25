# import json
# try :
#     with open('contact_json1.json','r') as file:
#         contact=json.loads(file.read())
# except:
#     with open('contact_json1.json','w') as file:
#         contact={}
#         json.dump(contact,file)
#     with open('contact_json1.json','r') as file:
#         contact=json.loads(file.read())
# print(contact)
# print(type(contact))
# while True:
#     choose=input("""1. Add Data
# 2. View all
# 3. View specific data
# 4. Remove data
# 5. Modify data
# 6. Exit\n""")

#     def add_data():
#         phone=int(input("Enter the phone number \n"))
#         if str(phone) not in contact:
#             while True:
#                 name=input("Enter the name\n")
#                 if len(name)>0:
#                     flag=True
#                     for i in name:
#                         if i>='a' and i<='z' or i>='A' and i<='Z':
#                             pass
#                         else:
#                             flag=False
#                             print("Invalid name!! enter again")
#                             break
#                     if flag==True:
#                         break
#                 else:
#                     print("Invalid name!! enter again")
#             while True:
#                 email=input("Enter the email\n")
#                 if len(email)>0:
#                     break
#                 else:
#                     print("Invalid email!!")
#             contact.update({phone:[name,email]})
#             with open('contact_json1.json','w') as file:
#                 json.dump(contact,file)
#         else:
#             print("Phone number already exist!!!")
#     def view_all():
#         for i,j in contact.items():
#             print('PHONE_NUMBER : ',i)
#             print('NAME : ',j[0])
#             print('EMAIL: ',j[1])
#             print('-'*50)
#     def view_specific_data():
#         try:
#             key=int(input("Enter the phone number \n"))
#             if str(key) in contact:
#                 print('PHONE_NUMBER : ',key)
#                 print('NAME : ',contact[key][0])
#                 print('EMAIL: ',contact[key][1])
#             else:
#                 print("Phone number not exist !!!")
#         except:
#             print("Invalid input!!")
#     def remove_data():
#         try:
#             key=int(input("Enter the phone number \n"))
#             if str(key) in contact:
#                 del contact[str(key)]
#                 print('Successfully deleted!!')
#             else:
#                 print("Phone number not exist!!")
#         except:
#             print("Invalid phone number!!")
#     def modify_data():
#         try:
#             key=int(input("Enter the mobile number\n"))
#             if str(key) in contact:
#                 sel=input("""1. Name modify
# 2. Email modify\n""")
#                 if sel=='1':
#                         name=input("Enter the new name you want to change\n")
#                         if len(name)>0:
#                             flag=True
#                             for i in name:
#                                 if i>='a' and i<='z' or i>='A' and i<='Z':
#                                     pass
#                                 else:
#                                     flag=False
#                                     print("Invalid name!! enter again")
#                                     break
#                         else:
#                             print("Invalid name!! enter again")
#                         if flag==True:
#                             contact[str(key)][0]=name
#                 elif sel=='2':
#                     email=input("Enter the new modify email\n")
#                     contact[str(key)][1]=email
#                 else:
#                     print("Invalid input!!")
#                 with open('contact_json1.json','w') as file:
#                     json.dump(contact,file)
#             else:
#                 print("number not found!!")
#         except:
#             print("Invalid InputE!!")

#     if choose=='1':
#         add_data()
#     elif choose=='2':
#         view_all()
#     elif choose=='3':
#         view_specific_data()
#     elif choose=='4':
#         remove_data()
#     elif choose=='5':
#         modify_data()
#     elif choose=='6':
#         break
#     else:
#         print("Invalid input!!")

str1 ="Rakesh,Mahesh,Kiran Kumar,Chandrashekar,Aarthi,Vijay,Sowmya"
str1=str1.split(',')
with open('D:/Aroha_Tech/python_vishwanath/oops/Aroha_Assignments/Python_Aroha1/friends.txt','a') as file:
    for i in str1:
        file.write('\n')
        file.write(i)
# with open('D:/Aroha_Tech/python_vishwanath/oops/Aroha_Assignments/Python_Aroha1/friends.txt','r') as file:
#     print(file.read())
# with open('')
