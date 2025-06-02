from operations import top,top_buyers,daily_ord_count,month,vendor,low_stock,product_count,average_ord

while True:
    print("Task E-Commerce Database\nSelect the option get answers ")
    print(f"1. Top 5 best-selling products (by quantity sold)\n2. Total revenue generated per month (last 6 months)\n3. Vendors with the most products listed\n4. Low stock products (less than 10 in stock)\n5. Average order value per buyer\n6. Category-wise total product count\n7. Top 3 buyers by total spending\n8. Daily order count for the current week\n9. To View all Answers\n10. Exit ")
    u_choice=int(input("Enter your option: "))
    if u_choice==1:
        top()
    elif u_choice==2:
        month()
    elif u_choice==3:
        vendor()
    elif u_choice==4:
        low_stock()
    elif u_choice==5:
        average_ord()
    elif u_choice==6:
        product_count()
    elif u_choice==7:
        top_buyers()
    elif u_choice==8:
        daily_ord_count()
    elif u_choice==9:
        print("All Answers")
        top()
        month()
        vendor()
        low_stock()
        average_ord()
        product_count()
        top_buyers()
        daily_ord_count()
    elif u_choice==10:
        exit()
    else:
        print(f"{u_choice} is a Invalid Choice")
