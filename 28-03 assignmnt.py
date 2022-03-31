# ##----------------------------1----------------------------------------------------------------------------------------------------
# def sell(x):
#     while True:
#         category=input("""Choose the category:
#         A. profit percentage 8%
#         B. Profit percentage 6.5%
#         C. Profit percentage 5.5% \n""")
#         if category=='A':
#             selling_price=x+((8*x)/100)
#             break
#         elif category=='B':
#             selling_price=x+((6.5*x)/100)
#             break
#         elif category=='C':
#             selling_price=x+((5.5*x)/100)
#             break
#         else:
#             print("Enter a valid category")
#     return selling_price
# cp=int(input("Enter the cost price of the article : "))
# print("Selling price is : ",sell(cp))

# ##-------------------------------------------------------------------------------------------------------------------------       

# names=[]
# rem_name={'ashok','lalit','pankaj','anand'}
# KR=0
# count=0
# while True:
#     n=input("Enter a name or STOP to exit: ")
#     if n=='STOP':
#         break
#     elif n not in names:
#         names.append(n)
#         if n.endswith('Kumar') or n.endswith('Rao'):
#             KR+=1
#             # names.remove(n)
#             # if n.endswith('Kumar'):
#             #     rem_name.add(n[0:len(n)-5])
#             # else:
#             #     rem_name.add(n[0:len(n)-3])
#         if n in rem_name:
#             names.remove(n)
#             count+=1
#     else:
#         print("Names already exits hence name not added!!")
# print(names)
# print("numbers of names having surnam as kumar or rao : ",KR)
# print("numbers of names removed : ",count)

# ##--------------------------------------------------------------------------------------------------------------------------

prod={}
hig=count=0
low=9999999999999999
hig_product=[]
low_product=[]
while True:
    prod_id=input("Enter the product id : ")
    if prod_id not in prod:
        prod_info=[]
        pname=input("Enter the product name : ")
        price=int(input("Enter the price of the product : "))
        prod_info.append(pname,price)
        prod.update({prod_id:prod_info})
        ##getting highest price product
        ##storing in list if there is more than one product having same price
        if price==hig:
            hig_product.append([pname,price])  ##[['shoes',200],['shirt',200]]
        if price>hig:
            hig=price
            hig_product=[[pname,price]] ##[['shoes',100]]
        ##getting lowest price product
        ##storing in list if there is more than one product having same price
        if price==low:
            low_product.append([pname,price])
        if price<low:
            low=price
            low_product=[[pname,price]]
        ##counting product whoes price is more tha 125000
        if price>125000:
            count+=1
    else:
        print("product id already exist!!")
    flag=input("Enter 'y' to continue adding and 'n' to exit ")
    if flag=='n':
        break
print(prod)
for j in hig_product:
    print("Highest price product is ",j[0]," having price of ",j[1])
for k in low_product:
    print("Lowest price product is ",k[0]," having price of ",k[1])
print("number of product whoes price is more tha 125000 is : ",count)


prod={101:['tv',20000]}
