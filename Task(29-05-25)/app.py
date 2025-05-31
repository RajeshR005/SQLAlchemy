from crud import insert,view,update,delete,view_all

while True:
    print(f"Student Management System\n\nThe Operations you can perform:\n")
    print("Menu:\n\n Insert = 1\n View = 2\n Update = 3\n Delete = 4\n View all = 5\n Exit = 6")
    User_input=(int(input("Enter the Operation Number: ")))
    if User_input==1:
        insert()
    elif User_input==2:
        view()
    elif User_input==3:
        update()
    elif User_input==4:
        delete()
    elif User_input==5:
        view_all()
    elif User_input==6:
        exit()
    

    else:
        print("Invalid Choice")