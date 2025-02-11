import sqlite3 as sql
import pandas as pd
import datetime
import os.path

#Table structure for my own reference

#prodtable - ProdID ProdName    ProdPrice   PriceQuantity
#salestable -SalesID SalesDate   ProdName   SalesTotal

#If the file does not exist, we make the file
path = './PL-ProductSales.db'
if os.path.isfile(path) == False:
    connection = sql.connect(path)
    cursor = connection.cursor()

    creation_str_prod = """CREATE TABLE prodtable(ProdID INTEGER PRIMARY KEY, ProdName TEXT, ProdPrice REAL, ProdQuantity Int);"""
    creation_str_sale = """CREATE TABLE salestable(SalesID INTEGER PRIMARY KEY, SalesDate Blob, ProdName Text, SalesTotal Int);"""

    connection.execute(creation_str_prod)
    connection.execute(creation_str_sale)
    connection.commit()
    connection.close()


#simple commandline based system for this  OLD company PC in Python

current_date = datetime.datetime.today()

salesdate = current_date.strftime("%d/%m/%Yv%H:%M:%S")

#Just to let the marker know, I installed Pandas via a virtual environment.

#connection up and running
connection = sql.connect('PL-ProductSales.db')



class PL_Product_Sales():
    @staticmethod
    def addProduct(name, price, quantity):
        try: #Error handling, SQL is error prone
            connection.execute("INSERT INTO prodtable (ProdName, ProdPrice, ProdQuantity) values (?,?,?)", (name, price, quantity))
        except sql.Error as e:
            print(f"An error has happened: {e}")

        connection.commit()

    @staticmethod
    def removeProduct(id):
        try:
            connection.execute("DELETE FROM prodtable WHERE ProdID =(?)", (id,))
            print("\n Executed Sucessfully\n")
            connection.commit()
        except sql.Error as e:
            print(f"An error has happened: {e}")

    @staticmethod
    def updateProduct(name, price, quantity, id):
        
        try:
            connection.execute("UPDATE prodtable Set ProdName = ?, ProdPrice = ?, ProdQuantity = ? where ProdID = ?", (name, price, quantity, id))
            print("\n Executed Sucessfully\n")
            connection.commit()
        except sql.Error as e:
            print(f"An error has happened: {e}")

    @staticmethod    
    def displayProduct():
        print(pd.read_sql('SELECT * FROM prodtable', connection))

    @staticmethod
    def sellProduct(ID, quantity):
        try:
            #Select the item
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM prodtable where ProdID = ?", (ID,))
            #How many items are there?
            record = cursor.fetchone()

            quantity_remain = record[3] #quantity in stock
            item_name = record[1]

            new_quant = quantity_remain - quantity #Quantity that will be left over
            if new_quant < 0:
                print("We cannot proceed. There is not enough stock. Please try again with a lower purchase or select another item\n")
            
            else:
                cursor.execute("Update prodtable SET ProdQuantity = ? WHERE ProdID = ?", (new_quant, ID))
                connection.commit()

                cursor = connection.cursor()
                cursor.execute("INSERT INTO salestable (SalesDate, ProdName, SalesTotal) values (?,?,?)",(salesdate, item_name, quantity))
                connection.commit()
                print("This transaction was sucessful! The customer may take their items now!")

        except sql.Error as e:
            print(f"An error has happened: {e}")
        

def drawMenu():
    print(" Welcome to the Store Management System!")
    print ("""
            1. Add a product
            2. Remove a product
            3. Update a product
            4. Display all products
            5. Sell a product
            6. Exit
           """)
    
userSelection = -1



while userSelection: #Menu system
    drawMenu()
    userSelection = int(input("Select an option: "))

    if userSelection == 6:
        print("Thank you for using our program")
        connection.close()
        break
        #Selecting sql commands to use

    if userSelection == 1:

        productName = input("Enter a product name: ")
        productPrice = input("Enter a product price: ")
        productQuantity = input("Enter product quantity: ")

        PL_Product_Sales.addProduct(productName, productPrice, productQuantity)

    elif userSelection == 2:
        productID = input("Enter ID of product to remove: ")
        PL_Product_Sales.removeProduct(productID)

        print("Item deleted sucessfully!")

    elif userSelection == 3:
        productID = input("Enter ID of product to update: ")
        productName = input("Enter new product name: ")
        productPrice = input("Enter new product price: ")
        productQuantity = input("Enter new product quantity: ")

        PL_Product_Sales.updateProduct(productName, productPrice,productQuantity, productID)
    

        print("\nData updated sucessfully")
    elif userSelection == 4:
        print("\nProduct_ID/Product_Name/Product_Price/Product_Quantity\n")

        PL_Product_Sales.displayProduct()
    elif userSelection == 5:
        productID = int(input("Type a product ID you would like to buy: "))
        quantity = int(input("How much would you like to buy: "))

        PL_Product_Sales.sellProduct(productID, quantity)
        
    

    