import sqlite3 as sql
import pandas as pd

#the connection we need!
#Just to let the marker know, I installed Pandas via a virtual environment. This should avoid "it works on my machine" issues

#connection up and running
connection = sql.connect('PL-ProductSales.db')


#Making boilerplate for myself to come back to later

class PL_Product_Sales():
    def addProduct(name, price, id):
        print("Apple")
    def removeProduct(id):
        print("pear")
    def updateProduct(id, name, price, quantity):
        print("orange")
    def displayProduct(id):
        print(pd.read_sql(f'SELECT * FROM prodtable WHERE ProdID ={id}', connection))
    def sellProduct():
        print("we losing")

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
        break
        #Selecting sql commands to use
    if userSelection == 1:
        productName = input("Enter a product name: ")
        productPrice = input("Enter a product price: ")
        productQuantity = input("Enter product quantity: ")



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
        selectedID = int(input("Select the ID of the record you want to display (Num): "))
        print("\nProduct_ID/Product_Name/Product_Price/Product_Quantity\n")

        PL_Product_Sales.displayProduct(selectedID)
        
    

    