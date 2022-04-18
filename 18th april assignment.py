contact={}
while True:
    choose=input("""1. Add new mobile details
2.View all the details from contacts
3. View the details of the specific mobile 
4. Remove the mobile number from the contact 
5. Edit the details bassed on the mobile numbert . Correcting the email id only
6. Exit
""")

    def add_new():
        phn=int(input("Enter the mobile number \n"))
        if phn not in contact:
            name=input("Enter the name \n")
            email=input("Enter the email \n")
            contact.update({phn:[name,email]})
    def view_all():
        print('PHONE_NUMBER','  NAME'+' '*30,'EMAIL'+' '*50)
        for i,j in contact.items():
            print(i,'  ',j[0],' '*(34-len(j[0])),j[1])
    def view_specific():
        data=int(input("Enter the phone number \n"))
        print('NAME: ',contact[data][0],'EMAIL : ',contact[data][1])
    def delete_data():
        key=int(input("Enter the phone number you want to delete\n"))
        if key in contact:
            del contact[key]
            return True
        elif key not in contact:
            print("Phone number not found!!")
            return False
    def modify_data():
        key=int(input("Enter the phobne number \n"))
        email=input("Enter the new email you want to change \n")
        choose[key][1]=email
        return True
    if choose=='1':
        add_new()
    elif choose=='2':
        view_all()
    elif choose=='3':
        view_specific()
    elif choose=='4':
        delete_data()
    elif choose=='5':
        modify_data()
    elif choose=='6':
        break
    else:
        print("Invalid input!!")
