from os import system
import mysql.connector
con = mysql.connector.connect(host="localhost", user="root",password="Your_Password", database="Product_Data")

# Function to Add Product
def Add_Product():
    PID = input ("\nEnter Product's ID:")
    # Checking if Product ID exists
    if(check_Product(PID) == False) :
        PCategory = input("Enter Product's Category:")
        PBrand = input("Enter Product's Brand:")
        PYOM = int(input("Enter Product's Year of Manufacturing [YYYYMMDD]:"))
        PQuantity = int(input("Enter Product's Quantity:"))
        PCost = int(input("Enter Product's Cost:"))
        PValue = PQuantity * PCost
        data = (PID, PYOM, PCategory,PBrand, PQuantity, PCost, PValue)
        # Inserting Product Details into the Product_Data (Product) Table
        sql = 'insert into Product values(%s,%s,%s,%s,%s,%s,%s)'
        c = con.cursor()
        c.execute(sql, data)
        con .commit()
        print("\nSuccessfully Added Product.")
        press = input("\nPress Any Key To Continue.")
        menu()
    else:
        print("\nProduct ID Already Exists!")
        press = input ("\nPress Any Key To Continue.")
        menu()

# Function to Check if Product with given PID exists
def check_Product(Product_id):
    sql = 'select * from Product where PID = %s'
    b = con .cursor(buffered=True)
    data = (Product_id,)
    b.execute(sql, data)
    x = b.rowcount
    if x == 1:
        return True
    else:
        return False

# Function to Display_Product
def Display_Product():
    print("\nDisplay Product's Record")
    # query to select all rows from Product_Data (Product) Table
    sql = 'select * from Product'
    b = con.cursor()
    b.execute(sql)
    # Fetching all details of all the Products
    r = b.fetchall()
    if not r:
        print("\nProduct Record does not Exist!")
    else:
        for i in r:
            print("\nProduct's Id: ", i[0])
            print("Product's Year of manufacturing: ", i[1])
            print("Product's Category: ", i[2])
            print("Products Brand: ", i[3])
            print("Product's Quantity: ", i[4])
            print("Product's Cost: ", i[5])
            print("Product's Value: ", i[6])

    press = input("\nPress Any Key To Continue.")
    menu()

        

# Function to Update_Product
def Update_Product():
    print("\nUpdate Product's Record")
    PID = input("\nEnter Product's ID: ")
    # checking if Product ID exists
    if (check_Product(PID) == True):
        PQuantity = int(input("Enter Product's Quantity:"))
        PCost = int(input("Enter Product's Cost:"))
        PValue = PQuantity * PCost
        # Updating Product details in Product Table
        sql = 'UPDATE Product SET PQuantity= %s, PCost = %s, PValue = %s WHERE PID = %s'
        data = (PQuantity, PCost, PValue, PID)
        b = con.cursor()
        b.execute(sql, data)
        con.commit()
        print("\nUpdated Product's Record")
        press = input("\nPress Any Key To Continue.")
        menu()
    else :
        print("\nProduct Record does not exist!")
        press = input("\nPress Any Key To Continue.")
        menu()

# Function to Remove_Product
def Remove_Product():
    print("\nRemove Product's Record")
    PID = input("\nEnter Product's ID:")
    # checking if Product ID exists
    if (check_Product(PID) == False):
        print("\nProduct's Record does not exist!")
        press = input("\nPress Any Key To Continue.")
        menu()
    else:
        # query to delete Product from Product table
        sql = 'delete from Product where PID = %s'
        data = (PID,)#Converting it into tuple.
        b = con.cursor()
        b.execute(sql, data)
        con .commit()
        print("\nProduct Removed!")
        press = input("\nPress Any key To Continue.")
        menu()

# Function to Search_Product
def Search_Product():
    print("\nSearch Product's Record")
    PID = input("\nEnter Product ID: ")
    # checking if Product ID exists
    if (check_Product(PID) == True):
    # query to search Product from Product table
        sql = 'select * from Product where PID = %s'
        data = (PID,)#Converting it into tuple.
        b = con.cursor()
        b.execute(sql, data)
        # fetching all details of all the products
        r  = b.fetchall()
        for i in r:
            print("\nProduct's Id: ", i[0])
            print("Product's Year of manufacturing: ", i[1])
            print("Product's Category: ", i[2])
            print("Products Brand: ",i[3])
            print("Product's Quantity: ", i[4])
            print("Product's Cost: ", i[5])
            print("Product's Value: ", i[6])
            press = input("\nPress Any key To Continue.")
            menu()
    else:
        print("\nProduct Record does not Exist!")
        press = input("\nPress Any Key To Continue.")
        menu()


# Menu function to display menu
def menu():
    system("cls")
    print("************************************")
    print("Inventory Management System")
    print("************************************")
    print("    1. Display Product")
    print("    2. Search Product ")
    print("    3. Add Product ")
    print("    4. Update Product ")
    print("    5. Delete Product ")
    print("    0. Exit")
    print("************************************")
    print("Choice Options: [1/2/3/4/5/0]:")
    print("************************************")

    ch = int(input("Enter your Choice: "))
    if ch == 1:
        system("cls")
        Display_Product()
    elif ch == 2:
        system("cls")
        Search_Product()
    elif ch == 3:
        system("cls")
        Add_Product()
    elif ch == 4:
        system("cls")
        Update_Product()
    elif ch == 5:
        system("cls")
        Remove_Product()
    elif ch == 0:
        system("cls")
        exit()
    else:
        print("\nInvalid Choice!")
        press = input("\nPress Any key To Continue.")
        menu()

menu()
