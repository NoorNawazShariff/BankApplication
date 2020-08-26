                        ######    BANKING Application Database Using SQlite  ######


print("Project by,")
print("\t\tNoor Nawaz Shariff")

import sqlite3
import time
import datetime

conn = sqlite3.connect('database.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(Name TEXT, Aadhar_number TEXT, Address TEXT, Customer_id TEXT, Password TEXT, Account_type TEXT, Balance REAL)")

def sign_up():
    name=input("ENTER YOUR NAME\t\t\t\t:")
    aadhar_number=input("\nENTER YOUR AADHAR NUMBER\t\t:")
    address=input("\nENTER YOUR ADDRESS\t\t\t:")
    customer_id=input("\nENTER NEW CUSTOMER ID \n(5 numbers min)\t\t\t\t:")
    password=input("\nENTER NEW PASSWORD(min 9 characters)\t:")
    print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t\t\tACCOUNT TYPE\n\t\t1 SAVING ACCOUNT\n\t\t2 CURRENT ACCOUNT\n\t\t3 QUIT\n\t\t(choose your account type)")
    z=input()
    while True:
        if z=='1':
            account_type="Saving Account"
            print("ACCOUNT TYPE\t\t\t\t:SAVING ACCOUNT")
            break
            
        elif z=='2':
            account_type="Current Account"
            print("ACCOUNT TYPE\t\t\t\t:CURRENT ACCOUNT")
            break
        elif z=='3':
            begin()
            
        else:
            print("INVALID OPTION(Please Sign UP Again)")
            sign_up()
            
            
    balance=input("AMOUNT TO BE DEPOSITED:\t\t\t:")
    

    c.execute("INSERT INTO stuffToPlot (name, aadhar_number, address, customer_id, password, account_type, balance)VALUES (?, ?, ?, ?, ?, ?, ?)",(name, aadhar_number, address, customer_id, password, account_type, balance))

    conn.commit()

    
def sign_in():


    cust_id=input("ENTER YOUR CUSTOMER ID\t\t\t:")
    pswd=input("\nENTER YOUR PASSWORD\t\t\t:")
    c.execute('SELECT * FROM stuffToPlot WHERE customer_id = (?) AND password=(?)',(cust_id,pswd,))
    data = c.fetchall()
    for row in data:
        print("\n\t****@@@@@@    YOU HAVE BEEN SUCCESSFULLY LOGGED IN    @@@@@@****")
        print("____________________________________________________________________________")
        menu()
    else:
        print("Invalid customer id or password Please try Again\n\n\n\n")
    
def menu():
    print("\n\t\t1 ADDRESS CHANGE \n\t\t2 MONEY DEPOSITE\n\t\t3 MONEY WITHDRAWAL\n\t\t4 PRINT DETAILS\n\t\t5 TRANSFER MONEY\n\t\t6 ACCOUNT CLOSURE\n\t\t7 CUSTOMER LOGOUT")
    print("\t\t(choose any 1 Option)")
    z=input()
    if z=='1':
        time.sleep(1)
        print("\t>>>>>CHANGE OF ADDRESS<<<<<\n")
        address_change()
    elif z=='2':
        time.sleep(1)
        print("\t>>>>>MONEY DEPOSITION<<<<<\n")
        money_deposite()
    elif z=='3':
        time.sleep(1)
        print("\t>>>>>MONEY WITHDRAWAL<<<<<\n")
        money_withdrawal()
    elif z=='4':
        time.sleep(1)
        print("\t>>>>>PRINT DETAILS<<<<<\n")
        details()
    elif z=='5':
        time.sleep(1)
        print("\t>>>>>TRANSFER MONEY<<<<<\n")
        transfer_money()
    elif z=='6':
        time.sleep(1)
        print("\t>>>>>ACCOUNT CLOSURE<<<<<\n")
        account_closure()
    elif z=='7':
        time.sleep(3)
        print("\t>>>>>YOU HAVE BEEN LOGGED OUT<<<<<\n")
        begin()
    else:
        print("INVALID OPTION")
        print('****************************')
        menu()
        

def address_change():
    cust_id=input("Enter your Customer id (for verification)\n")
    pswd=input("Enter your Password (for verification)\n")
    c.execute('SELECT * FROM stuffToPlot WHERE customer_id = (?) AND password=(?)',(cust_id,pswd,))
    exist = c.fetchall()
    if exist:
        button=input("Press 1 to Proceed \n Press 2 to Quit\n")
        if button=='1':
            ads=input("Enter Your New Address\n")
            c.execute("UPDATE stuffToPlot SET address=? WHERE customer_id=? AND password=?",(ads,cust_id,pswd,))
            print("your Adress have been succussfully changed")
            conn.commit()
            menu()
            
        elif button=='2':
            menu()
        else:
            print("INVALID OPTION(please try again)")
            print('****************************')
            address_change()
    else:
        print("Invalid Custermer id or Password(Please Try Again)")
        begin()


   
def money_deposite():
    cust_id=input("Enter your customer id (for verification)\n")
    pswd=input("Enter your password (for verification)\n")
    c.execute('SELECT * FROM stuffToPlot WHERE customer_id = (?) AND password=(?)',(cust_id,pswd,))
    exist = c.fetchall()
    if exist:
        button=input("Press 1 to Proceed \nPress 2 to Quit\n")
        if button=='1':
            deposite=int(input("Enter the amount to be deposited"))
            c.execute('SELECT balance FROM stuffToPlot WHERE customer_id = (?) AND password=(?)',(cust_id,pswd,))
            data = c.fetchall()
            for row in data:
                x=row
                y=list(x)
                print("earlier balance:",y[0])
                break
            balnc=deposite+y[0]
            c.execute("UPDATE stuffToPlot SET balance=? WHERE customer_id=? AND password=?",(balnc,cust_id,pswd,))
##            c.execute('SELECT * FROM stuffToPlot WHERE customer_id = (?) AND password=(?)',(cust_id,pswd,))
##            data = c.fetchall()
##            for row in data:
##                print(row)
##                break
##            print(balnc)
            print("Current balance:",balnc)
            conn.commit()


            
        elif button=='2':
            menu()
        else:
            print("INVALID OPTION(please try again)")
            print('****************************')
            menu()
    else:
        menu()
       
    
def money_withdrawal():
    cust_id=input("Enter your customer id (for verification)\n")
    pswd=input("Enter your password (for verification)\n")
    c.execute('SELECT * FROM stuffToPlot WHERE customer_id = (?) AND password=(?)',(cust_id,pswd,))
    exist = c.fetchall()
    if exist:
        button=input("Press 1 to Proceed\n 2 to Quit\n")
        if button=='1':
            withdraw=int(input("Enter the amount to be withdrawn"))
            c.execute('SELECT balance FROM stuffToPlot WHERE customer_id = (?) AND password=(?)',(cust_id,pswd,))
            data = c.fetchall()
            for row in data:
                x=row
                y=list(x)
                print("Earlier balance:",y[0])
                break
            if withdraw+200 < y[0]:    
                balnc=y[0]-withdraw
                c.execute("UPDATE stuffToPlot SET balance=? WHERE customer_id=? AND password=?",(balnc,cust_id,pswd,))
                c.execute('SELECT * FROM stuffToPlot WHERE customer_id = (?) AND password=(?)',(cust_id,pswd,))
                data = c.fetchall()
                print("Present balance 1:",balnc)
                conn.commit()
            else:
                print("You dont have Sufficient Balance to make such withdraw")
        elif button=='2':
            menu()
    else:
        print("INVALID OPTION(please try again)")
        print('****************************')
        menu()
        
        
def details():
    cust_id=input("Enter your customer id (for verification)\n")
    pswd=input("Enter your password (for verification)\n")
    c.execute('SELECT * FROM stuffToPlot WHERE customer_id = (?) AND password=(?)',(cust_id,pswd,))
    data = c.fetchall()
    for row in data:
        x=row
        z=list(x)
        print("Your Name is:",z[0])
        print("Your Aadhar number is",z[1])
        print("Your Address is:",z[2])
        print("Your customer Id is:",z[3])
        print("Your password is:",z[4])
        print("Your Account Type is:",z[5])
        print("Your Balance is:",z[6])
        break
    
        
def transfer_money():
    cust_id=input("Enter your customer id (for verification)\n")
    pswd=input("Enter your password (for verification)\n")
    c.execute('SELECT * FROM stuffToPlot WHERE customer_id = (?) AND password=(?)',(cust_id,pswd,))
    exist = c.fetchall()
    if exist:
        aadhar_number=input("Enter the aadhar number of the person to whome You want to transfer money")
        cut_id=input("Enter their customer_id")
        c.execute('SELECT * FROM stuffToPlot WHERE aadhar_number = (?) AND customer_id=(?)',(aadhar_number,cut_id,))
        exist = c.fetchall()
        if exist:
            button=input("Press 1 to Proceed \nPress 2 to Quit\n")
            if button=='1':
                amount=int(input("Enter the amount you want to transfer:"))
                c.execute('SELECT balance FROM stuffToPlot WHERE customer_id = (?) AND password=(?)',(cust_id,pswd,))
                data = c.fetchall()
                for row in data:
                    x=row
                    y=list(x)
                    print("Earlier balance:",y[0])
                    break
                y[0]=y[0]-amount
                print("After transaction your Ammount is:",y[0])
                c.execute("UPDATE stuffToPlot SET balance=? WHERE customer_id=? AND password=?",(y[0],cust_id,pswd,))
                c.execute('SELECT * FROM stuffToPlot WHERE customer_id = (?) AND password=(?)',(cust_id,pswd,))
                data = c.fetchall()
                conn.commit()
    
    
                c.execute('SELECT balance FROM stuffToPlot WHERE aadhar_number = (?) AND customer_id=(?)',(aadhar_number,cut_id,))
                data = c.fetchall()
                for row in data:
                    w=row
                    a=list(x)
                a[0]=a[0]+amount
                c.execute("UPDATE stuffToPlot SET balance=? WHERE aadhar_number=? AND customer_id=?",(a[0],aadhar_number,cut_id,))
                c.execute('SELECT * FROM stuffToPlot WHERE customer_id = (?) AND password=(?)',(cust_id,pswd,))
                conn.commit()
            elif button=='2':
                menu()
            else:
                begin()
        else:
            print("No such Customer is present in our Bank(Or please try Again)")
            transfer_money()
    else:
        print("INVALID OPTION(please try again)")
        print('****************************')
        transfer_money()
    
def account_closure():
    cust_id=input("Enter your customer id (for verification)\n")
    pswd=input("Enter your password (for verification)\n")
    c.execute('SELECT * FROM stuffToPlot WHERE customer_id = (?) AND password=(?)',(cust_id,pswd,))
    exist = c.fetchall()
    if exist:
        aadhar_number=input("If you are sure deleting Your account from our bank the please enter your aadhar number and hit Enter")
        c.execute('SELECT * FROM stuffToPlot WHERE customer_id = (?) AND password=(?)',(cust_id,pswd,))
        exist = c.fetchall()
        if exist:
            button=input("Press 1 to Proceed \n 2 to Quit\n")
            if button=='1':
                c.execute("DELETE FROM stuffToPlot WHERE customer_id=? AND aadhar_number=? AND password=?",(cust_id,aadhar_number,pswd,))
                print("YOUR Account have been removed successfully from our bank")
                begin()
                conn.commit()
            elif button=='2':
                menu()
            else:
                begin()
        else:
             print("Invalid Aadhar Number")
             accoount_closure()
    else:
        print("Their is no account with such number")
    
        begin()
def admin():
    cust_id=input("Enter Admin ID \n")
    pswd=input("Enter Admin Password\n")
    c.execute('SELECT * FROM stuffToPlot WHERE customer_id = (?) AND password=(?)',(cust_id,pswd,))
    exist = c.fetchall()
    if exist:
        c.execute("SELECT * FROM stuffToPlot WHERE customer_id = 'noor' AND password='nawaz' ")
        exist = c.fetchall()
        if exist:
            c.execute('SELECT * FROM stuffToPlot')
            data=c.fetchall()
            for row in data:
                print(row,'\n')
    
    
create_table()
'''for i in range(10):
    dynamic_data_entry(
    )
    
    time.sleep(1)'''



def begin():
    while True:
        
        
        print("===============================================================================")
        localtime = time.asctime( time.localtime(time.time()) )
        print ("Time :", localtime)      

        print("===============================================================================")
        print("\t\t\t1 SIGN_UP(New Customer)\n\t\t\t2 SIGN_IN(Existing Customer)\n\t\t\t3 ADMIN LOGIN\n\t\t\t4 Quit")    
        x=input()

    
        if x=='1':
            time.sleep(1)
            sign_up()
        elif x=='2':
            time.sleep(1)
            sign_in()
        elif x=='3':
            time.sleep(1)
            admin()
        elif x=='4':
            time.sleep(1)
            quit()
        else:
            print("INVALID OPTION")
begin()
def quit():
    c.close
    conn.close()
    
    
