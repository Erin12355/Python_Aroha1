## 1. Enter a name and check whether the 8th element is dwdwdfdfdfdfdfdfdfdfdwfdvwd,ffdf,d,
##    vowel or not vowel
##                             |
##    example:  i/p is sanjay kumar
##    handle if the length of the string is small (say less than 8)

class V_check:
    def __init__(self,name,vow):
        self.name=name
        self.vow=vow
        if self.name[7] in self.vow:
            print("position 8 is vowel")
        else:
            print("position 8 is not vowel")
while True:
    name=input("Enter a name : \n")
    vow='aeiou'
    if len(name)>=8:
        a=V_check(name,vow)
        break
    else:
        print("Length of the name is short it is less than 8 . Enter again \n")

# 2. enter a sentence
#    enter a word to search in it
#    does the word exists ?
#    if it does how many words are there?
#    which position is the first occurance of the word in the sentence?

sentence=input("Enter a Sentence \n")
word=input("Enter the word to be search \n")
w_count=pos_first=0
if word in sentence:
    w_count=sentence.count(word)
    pos_first=sentence.index(word)
else:
    print("word not found")
print("Numbers of the word contain in the sentence is : ",w_count)
print("Position of the first occurance of the word to the sentence : ",pos_first)

# 3. enter a name 
#    print the name in upper case, lower case  and title case
#    find out how many char are there?

name=input("Enter a name : ")
print("upper: ",name.upper())
print("lower: ",name.lower())
print("title: ",name.title())
chr=set()
for i in name:
    chr.add(i)
print("number of character : ",len(chr))

# 4. input the mobile number (as string)
#    check whether the last digit of the mobile number is either 5 or 8
#                       |
#    example:  9886612675
#    if the mobile number inputted is not 10 char then display 
#    'INVALID mobile number'

while True:
    try:
        phn=int(input("Enter the mobile number : "))
        break
    except:
        print("invalid data type !! enter again")
phn=str(phn)
if len(phn)==10:
    if phn[-1]=='5':
        print("ended with 5")
    elif phn[-1]==8:
        print("Ended with 8")
else:
    print("Invalid phone number!!")

# 5. given a string say
#    name1 ='Mohan,Ajay,harish,anand,veena,rashmi,Kiran'
#    word1 ='VEENA'
#    find this word1 in name1 irresprective of lower case/upper case
#    how will you solve it?

name1 ='Mohan,Ajay,harish,anand,veena,rashmi,Kiran'
name1=name1.split(',')
word1=input("Enter the name to be search : ")
flag=True
for i in name1:
    if word1.upper()==i.upper():
        print("Name is there.")
        flag=False
        break
if flag==True:
    print("Name is not there")

# 6. enter the day, month and year as numbers, one by one
#    dd = 9
#    mn = 12
#    yr = 2020
#    display it is valid date or not
#    valid date rule is 
#    day must be 1 to 31 for any month 1 to 12
#    day must be 1 to 30 if the month is 4,6,9,11
#    day must be 1 to 29 if the year is Leap and the month is 2
#    Leap year rule
#    if the year is not century year like 2004, 1984 , 1996 etc then
#    divide such year by 4, if it is divisible then it is Leap or not
#    leap
#    Non-leap year have 28 days
#    if the year is like 1700, 1800, 1900, 2000 - then they are century
#    year , such year divide by 400 and if it is divisible then it is 
#    leap century year such year will have 29 days in Feb
#    hence 29 2 1800 is invalid
#          29 2 1600 is valid
#          29 2 2000 is valid
#          29 2 1900 is invalid
while True:
    try:
        year=int(input("Enter the year :\n"))
        break
    except:
        print("Enter a proper year in number !!")
leap=bool()
if year%100==0:
    if year%400==0:
        leap=True
elif year%4==0:
    leap=True
else:
    leap=False
while True:
    try:
        month=int(input("Enter the month :\n"))
        if month in range(1,13):
            break
        else:
            print("Invalid month!! enter again")
    except:
        print("Enter proper month in number!!")
while True:
    try:
        day=int(input("Enter the day :\n"))
        if day in range(1,32):
            if month not in (4,6,9,11,2):
                if day in range(1,32):
                    break
                else:
                    print("Invalid date!! enter again ")
            elif month in (4,6,9,11):
                if day in range(1,31):
                    break
                else:
                    print("Invalid date !! enter again")
            else:
                if leap:
                    if day in range(1,30):
                        break
                    else:
                        print("Invalid date !! it is leap year ,enter again")
                else:
                    if day in range(1,29):
                        break
                    else:
                        print("Invalid day !! it is not leap year ,enter again")
        else:
            print("Invalid day !! out of range")
    except:
        print("Enter a proper day in number !!")
print(day,'-',month,'-',year,' is Valid ')

# 7. given
#    price of LPG for domestic is 950 rs
#    price of LPG for commercail is 1450 rs
#    domestic LPG the user cannot take more than 2 qty
#    commercial LPG the user cannot take more than 6 qty
#    input the category (commercial OR domestic)
#    input the qty (apply the rules) 
#    display the bill amount
#    give discount of 5% is the LPG qty is more than 3 in case of commercial 
#    category


# 7. given
#    price of LPG for domestic is 950 rs
#    price of LPG for commercail is 1450 rs
#    domestic LPG the user cannot take more than 2 qty
#    commercial LPG the user cannot take more than 6 qty
#    input the category (commercial OR domestic)
#    input the qty (apply the rules) 
#    display the bill amount
#    give discount of 5% is the LPG qty is more than 3 in case of commercial 
#    category
while True:
    catg=input("""Choose the Category :
    A. Domestic
    B. Commercial
    """)
    if catg in 'Aa':
        while True:
            qty=int(input("Enter the number of cyclinder : "))
            if qty<=2:
                print("Bill : ",qty*950)
                break
            else:
                print("For Domestic number of cylinder cannot exceed 2 !")
        break
    elif catg in 'Bb':
            qty=int(input("Enter the number of cyclinder : "))
            if qty>3:
                print("Bill : ",(1450*qty)-((5/100)*1450))
            else:
                print("Bill : ",(1450*qty))
            break
    else:
        print("Invalid Category!!!")

# 8. input a number and display one of the following
#    it is a SINGLE digit number ::: if it is 1 to 9
#    it is DOUBLE digit number ::: if it is 10 to 99
#    and so on...
#    do it till SIX digit number
#    if number is above SIX digits then display this number is LARGE number
#    NOTE
#    if the user inputs a NEGATIVE number then - donot do the above processing
#    instead display :: cannot process NEGATIVE numbers
while True:
    try:
        num=int(input("Enter a number : \n"))
        break
    except:
        print("Invalid number !! Enter agan")
if num<=0:
    print(" cannot process NEGATIVE numbers and ZERO")
elif len(str(num))>5:
    print("this number is LARGE number")
else:
    num=str(num)
    lst=['SINGLE','DOUBLE','TRIPLE','QUADRUPLE','QUINTUPLE']
    print('It is ',lst[len(num)-1])
            
