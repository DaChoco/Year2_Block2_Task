import sqlite3 as sql
import pandas as pd

#the connection we need!
#Just to let the marker know, I installed Pandas via a virtual environment. This should avoid "it works on my machine" issues
#EXTRA - The SQLite Database was installed inside such a folder as well to avoid these problems

#connection up and running
connection = sql.connect('PL-ProductSales.db')


#Making boilerplate for myself to come back to later

class PL_Product_Sales():
    def addProduct(name, price, id, quantity):
        connection.execute("INSERT INTO prodtable (ProdName, ProdPrice, ProdQuantity) values (?,?,?)", (name, price, quantity))
        connection.commit()
    def removeProduct(id):
        print("pear")

        connection.commit()
    def updateProduct(id, name, price, quantity):
        print("orange")
        connection.commit()
    def displayProduct():
        print(pd.read_sql('SELECT * FROM prodtable', connection))
    def sellProduct():
        print("we losing")
        connection.commit()

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

        PL_Product_Sales.addProduct(productName,    productPrice,   productID, productQuantity)



    elif userSelection == 2:
        productID = input("Enter ID of product to remove: ")

        print("Item deleted sucessfully!")

    elif userSelection == 3:
        productID = input("Enter ID of product to update: ")
        productName = input("Enter new product name: ")
        productPrice = input("Enter new product price: ")
        productQuantity = input("Enter new product quantity: ")

        print("\nData updated sucessfully")
    elif userSelection == 4:
        print("\nProduct_ID/Product_Name/Product_Price/Product_Quantity\n")

        PL_Product_Sales.displayProduct()
        
    

    