#Constant values!
utilities = 0.05
Rent_or_Housing = 0.15
transportation = 0.3
healthcare = 0.03
groceries = 0.1
communication = 0.02

#THE CLASS

class taxCalculations():
    def __init__(self, before_tax):
          self.beforetax = before_tax

    def createEntry(self, pre_tax_income, post_tax_income):
        print(f"""          Monthly Budget\n
-----------------------------------------------------------------------\n
                Monthly Income
-----------------------------------------------------------------------\n
        Gross Montly Income (Before tax): {pre_tax_income}\n
        Gross Monthly Income (After tax): {post_tax_income}""")

    #Tax brackets from SARS
    def taxBrackets(self):
        if self.beforetax <237000:
            self.aftertax = round(self.beforetax * (1-0.18),3)

        elif self.beforetax>237101 and self.beforetax<370500:
                self.aftertax = round(42000+ ((self.beforetax-237100)*(1-0.26)), 3)

        elif self.beforetax>370501 and self.beforetax<512800:
                self.aftertax = round(77362+ ((self.beforetax-370500)*(1-0.31)), 3)

        elif self.beforetax>512801 and self.beforetax<673000:
                self.aftertax = round(121475+ ((self.beforetax-512800)*(1-0.36)), 3)

        elif self.beforetax>673001 and self.beforetax<857900:
                self.aftertax = round(179141+ ((self.beforetax-673000)*(1-0.39)), 3)

        elif self.beforetax>857901 and self.beforetax<1817000:
                self.aftertax = round(251258+ ((self.beforetax-857900)*(1-0.41)), 3)
        elif self.beforetax>1817000:
                self.aftertax = round(644489+ ((self.beforetax-18170001)*(1-0.45)), 3)
        
        return self.aftertax
    
    #Expenses per month
    def expenses(self):
          utility_fee = utilities * self.aftertax
          housing_fee = Rent_or_Housing * self.aftertax
          transport_fee = transportation * self.aftertax
          healthcare_fee = healthcare * self.aftertax
          grocery_fee = groceries * self.aftertax
          communication_fee = communication * self.aftertax
          #Draw it

          print(
                f"""    
                Utilities: R{utility_fee}  
                Rent: R{housing_fee} 
                Transport: R{transport_fee}    
                Health: R{healthcare_fee}    
                Groceries: R{grocery_fee}  
                Communication: R{communication_fee}""")
          print("-------------------------------------")
          total_fee = utility_fee + housing_fee + transport_fee + healthcare_fee + grocery_fee + communication_fee

          print(f"  Total Expenses: R{total_fee}")
          print("--------------------------------------------")

          net_income = self.aftertax - total_fee

          print(f"Net Income: R{net_income}")
          print("--------------------------------------------")

#END OF CLASS, ONTO THE FUNCTIONS

def drawMenu():
    print("""Budget Portal\n----------------------------\n
            1. Create New Entry\n
            0. Exit\n""")
    


#END OF FUNCTIONS, ONTO THE MAIN PROGRAM

menu_option = 1

while menu_option==1:
    drawMenu()
    menu_option = int(input("Select an option: "))
    if menu_option == 0:
        break
    entered_code = input("Enter User Code: ")
    gross_income_no_tax = int(input("Enter Gross Annual income before Tax: "))/12

    usertaxes = taxCalculations(gross_income_no_tax)

    usertaxes.createEntry(gross_income_no_tax, usertaxes.taxBrackets())

    usertaxes.expenses()
 



