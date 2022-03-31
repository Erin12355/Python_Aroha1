price_quan={1000:(72.55,10),2000:(56.25,5),3000:(25.25,15)}
prod_name={1000:'toothpaste',2000:'soap',3000:'campor'}
option=1
  ##Displaying the items
for a,b in prod_name.items():
    print(option," ",b)
    option+=1
try:
    def shop():
        flag=False
        p_name=input("Enter the product name : \n")
        for i,j in prod_name.items():
            #checking product in the list
            if j.upper()==p_name.upper():
                ## checking that selected item available in store or not
                if i in price_quan:
                    flag=True
                    print("PRODUCT NAME : ",p_name)
                    print("PRICE : ",price_quan[i][0])
                    print("AVAILABLE QUANTITY : ",price_quan[i][1])
                    quan=int(input("Enter the quantity : "))
                    ##checking quantitity of the product in the store for the selected item
                    if price_quan[i][1]==0:
                        print("product out of stock!!")
                    elif quan<= price_quan[i][1]:
                        bill=price_quan[i][0]*quan
                        price_quan[i]=list(price_quan[i])
                        price_quan[i][1]=price_quan[i][1]-quan
                    else:
                        print("Asked qty is NOT available!!")
                        break
        if flag==False:
            print("Item not available in the store !!")
        print(price_quan)
except:
    pass
finally:
    shop()

#----------------------------------------------------------------------------------------------------------------------

set1={100,560,220,565,-12,10,15}
list1=[890,560,-560,-220,-565,-12,12,-10,14,22,15]
leng=len(list1)
set1=list(set1)
count=0
for i in set1:
    rev=i-(i*2)
    for j in range(len(list1)):
        ##breaking the entire loop after deleting 4 data
        if len(list1) == (leng-4):
            break
        elif i in list1:
            list1.remove(i)
        elif rev in list1:
            list1.remove(rev)
print(list1)

#----------------------------------------------------------------------------------------------------------------------------

def input_data():
    p=int(input("Enter the Principle : "))
    r=float(input("Enter the rate : "))
    t=int(input("Enter the time in year : "))
    return p,r,t
p,r,t=input_data()
def simple_interest():
    SI=(p*r*t)/100
    return SI
def amount():
    smt=simple_interest() + p
    return smt
def compute_interest():
    print("Simple interest : ",simple_interest())
    print("Amount : ",amount())
compute_interest()