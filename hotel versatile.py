import random 
import datetime 
import pandas as pd 
import pymysql 
from sqlalchemy import create_engine
import mysql.connector as sqltor
# Global List Declaration  
name = [] 
phno = [] 
add = [] 
checkin = [] 
checkout = [] 
room = [] 
price = [] 
rc = [] 
p = [] 
roomno = [] 
custid = [] 
day = []    
# Global Vaariable Declaration    
i = 0   
dict1={}
# Home Function 

def Home(): 
    print("\t\t\t\t\t\t WELCOME TO VERSATILE \n") 
    print("\t\t\t 1 Booking\n") 
    print("\t\t\t 2 Rooms Info\n") 
    print("\t\t\t 3 Record\n") 
    print("\t\t\t 4 customer info\n") 
    print("\t\t\t 0 Exit\n") 
    ch=int(input("->")) 
    if ch == 1: 
        print(" ") 
        Booking()   
    elif ch == 2: 
        print(" ") 
        Rooms_Info()    
    elif ch == 3: 
        print(" ") 
        Record() 
    elif ch == 4: 
        print(" ") 
        custinfo()
    else: 
        exit() 
        # Function used in booking 
def date(c):    
    if c[2] >= 2000 and c[2] <= 2021: 
        if c[1] != 0 and c[1] <= 12:
            if c[1] == 2 and c[0] != 0 and c[0] <= 31:                
                if c[2]%4 == 0 and c[0] <= 29: 
                    pass               
                elif c[0]<29: 
                    pass     
                else: 
                    print("Invalid date\n") 
                    name.pop(i) 
                    phno.pop(i) 
                    add.pop(i) 
                    checkin.pop(i) 
                    checkout.pop(i) 
                    Booking() 
            # if month is odd & less than equal  
            # to 7th  month  
            elif c[1] <= 7 and c[1]%2 != 0 and c[0] <= 31: 
                pass
            # if month is even & less than equal to 7th 
            # month and not 2nd month 
            elif c[1] <= 7 and c[1]%2 == 0 and c[0] <= 30 and c[1] != 2: 
                pass
            # if month is even & greater than equal  
            # to 8th  month 
            elif c[1] >= 8 and c[1]%2 == 0 and c[0] <= 31: 
                pass           
            # if month is odd & greater than equal 
            # to 8th  month 
            elif c[1]>=8 and c[1]%2!=0 and c[0]<=30:
                pass           
            else:  
                print("Invalid date\n") 
                name.pop(i) 
                phno.pop(i) 
                add.pop(i) 
                checkin.pop(i) 
                checkout.pop(i) 
                Booking()               
        else: 
            print("Invalid date\n") 
            name.pop(i) 
            phno.pop(i) 
            add.pop(i) 
            checkin.pop(i) 
            checkout.pop(i) 
            Booking() 
    else: 
        print("Invalid date\n") 
        name.pop(i) 
        phno.pop(i) 
        add.pop(i) 
        checkin.pop(i) 
        checkout.pop(i) 
        Booking()    
# Booking fucntion  
def Booking(): 
        # used global keyword to  
        # use global variable 'i' 
        global i 
        print(" BOOKING ROOMS") 
        print(" ") 
        while 1: 
            n = str(input("Name: ")) 
            p1 = str(input("Phone No.: ")) 
            a = str(input("Address: "))
            # checks if any field is not empty 
            if n!="" and p1!="" and a!="": 
                name.append(n) 
                add.append(a) 
                break
            else:
                 print("\tName, Phone no. & Address cannot be empty..!!") 
        cii=str(input("Check-In: ")) 
        checkin.append(cii) 
        cii=cii.split('/') 
        ci=cii 
        ci[0]=int(ci[0]) 
        ci[1]=int(ci[1]) 

        ci[2]=int(ci[2]) 
        date(ci)
        coo=str(input("Check-Out: "))
        checkout.append(coo) 
        coo=coo.split('/') 
        co=coo 
        co[0]=int(co[0]) 
        co[1]=int(co[1]) 
        co[2]=int(co[2]) 
        # checks if check-out date falls after  
        # check-in date 
        if co[1]<ci[1] and co[2]<ci[2]:
            print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n") 
            name.pop(i) 
            add.pop(i) 
            checkin.pop(i) 
            checkout.pop(i) 
            Booking() 
        elif co[1]==ci[1] and co[2]>=ci[2] and co[0]<=ci[0]:             
            print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n") 
            name.pop(i) 
            add.pop(i) 
            checkin.pop(i) 
            checkout.pop(i) 
            Booking() 
        else: 
            pass         
        date(co) 
        d1 = datetime.datetime(ci[2],ci[1],ci[0]) 
        d2 = datetime.datetime(co[2],co[1],co[0]) 
        d = (d2-d1).days 
        day.append(d)           
        print("----SELECT ROOM TYPE----") 
        print(" 1. Standard Non-AC") 
        print(" 2. Standard AC") 
        print(" 3. 3-Bed Non-AC") 
        print(" 4. 3-Bed AC") 
        print(("\t\tPress 0 for Room Prices"))           
        ch=int(input("->"))           
        # if-conditions to display alloted room 
        # type and it's price 
        if ch==0: 
            print(" 1. Standard Non-AC - Rs. 3500") 
            print(" 2. Standard AC - Rs. 4000") 
            print(" 3. 3-Bed Non-AC - Rs. 4500") 
            print(" 4. 3-Bed AC - Rs. 5000") 
            ch=int(input("->")) 
        if ch==1: 
            room.append('Standard Non-AC') 
            print("Room Type- Standard Non-AC")   
            price.append(3500) 
            print("Price- 3500") 
        elif ch==2: 
            room.append('Standard AC') 
            print("Room Type- Standard AC") 
            price.append(4000) 
            print("Price- 4000") 
        elif ch==3: 
            room.append('3-Bed Non-AC') 
            print("Room Type- 3-Bed Non-AC") 
            price.append(4500) 
            print("Price- 4500") 
        elif ch==4: 
            room.append('3-Bed AC') 
            print("Room Type- 3-Bed AC") 
            price.append(5000) 
            print("Price- 5000") 
        else: 
            print(" Wrong choice..!!")   
        # randomly generating room no. and customer  
        # id for customer 
        rn = random.randrange(40)+300
        cid = random.randrange(40)+10                    
        # checks if alloted room no. & customer  
        # id already not alloted 
        while rn in roomno or cid in custid: 
            rn = random.randrange(60)+300
            cid = random.randrange(60)+10
        rc.append(0) 
        p.append(0) 
        if p1 not in phno: 
            phno.append(p1) 
        elif p1 in phno: 
            for n in range(0,i): 
                if p1== phno[n]: 
                    if p[n]==1: 
                        phno.append(p1) 
        elif p1 in phno: 
            for n in range(0,i): 
                if p1== phno[n]: 
                    if p[n]==0:
                        print("\tPhone no. already exists and payment yet not done..!!") 
                        name.pop(i) 
                        add.pop(i) 
                        checkin.pop(i) 
                        checkout.pop(i) 
                        Booking() 
        print("") 
        print("\t\t\t**ROOM BOOKED SUCCESSFULLY**\n") 
        print("Room No. - ",rn) 
        print("Customer Id - ",cid) 
        roomno.append(rn) 
        custid.append(cid) 
        i=i+1
        dict1={"name":name ,"phno":phno ,"address":add ,"checkin":checkin ,"checkout":checkout ,"prices":price ,"room no":roomno ,"cust id":custid }
        a=pd.DataFrame(dict1)
        #codes for saving information in database
        engine=create_engine("mysql+pymysql://root:root123@localhost/versatile")
        conn=engine.connect()
        a.to_sql("booking",conn,index=False,if_exists="append")
        n=int(input("0-BACK\n ->"))         
        if n==0: 
            Home() 
        else: 
            exit() 
# ROOMS INFO  
def Rooms_Info(): 
    print("         ------ HOTEL ROOMS INFO ------") 
    print("") 
    print("STANDARD NON-AC") 
    print("---------------------------------------------------------------") 
    print("Room amenities include: 1 Double Bed, Television, Telephone,") 
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and") 
    print("an attached washroom with hot/cold water.\n") 
    print("STANDARD NON-AC") 
    print("---------------------------------------------------------------") 
    print("Room amenities include: 1 Double Bed, Television, Telephone,") 
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and") 
    print("an attached washroom with hot/cold water + Window/Split AC.\n") 
    print("3-Bed NON-AC") 
    print("---------------------------------------------------------------") 
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,") 
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1") 
    print("Side table, Balcony with an Accent table with 2 Chair and an") 
    print("attached washroom with hot/cold water.\n") 
    print("3-Bed AC") 
    print("---------------------------------------------------------------") 
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,") 
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ") 
    print("1 Side table, Balcony with an Accent table with 2 Chair and an") 
    print("attached washroom with hot/cold water + Window/Split AC.\n\n") 
    print() 
    n=int(input("0-BACK\n ->")) 
    if n==0: 
        Home() 
    else: 
        exit() 
# RECORD FUNCTION  
        
def Record(): 
    mycon=sqltor.connect(host="localhost",user="root",passwd='root123',database="versatile")
    df=pd.read_sql("select * from booking;",mycon)
    print("\t\t\t\t\t\t HOTEL RECORD \n") 
    print(df)
    n=int(input("0-BACK\n ->"))         
    if n==0: 
        Home() 
    else: 
        exit()

#custinfo function
def custinfo():
    phn=str(input("enter phone number of customer:"))
    mycon2=sqltor.connect(host="localhost",user="root",passwd='root123',database="versatile")
    qry="select * from booking where phno='%s';"%(phn)
    custin=pd.read_sql(qry,mycon2)
    print(custin)
    n=int(input("0-BACK\n ->"))         
    if n==0: 
        Home() 
    else: 
        exit()
# Driver Code  
Home()