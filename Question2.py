import sqlite3 as sql

#Making boilerplate for myself to come back to later

class PL_Product_Sales():
    def addProduct(self, name, price, id):
        print("Apple")
    def removeProduct(self, id):
        print("pear")
    def updateProduct(self, id, name, price, quantity):
        print("orange")
    def displayProduct(self):
        print("WOW")
    def sellProduct(self):
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



while userSelection:
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
        print("Product_ID/Product_Name/Product_Price/Product_Quantity\n")
        
    

    