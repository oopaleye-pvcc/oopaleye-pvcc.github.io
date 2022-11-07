import datetime
import random

# pizza sizes + sales tax
SMALL_PIZZA = 9.99
MEDIUM_PIZZA = 12.99
LARGE_PIZZA = 14.99
EXTRA_LARGE_PIZZA = 17.99
SALES_TAX = .055


# calculations
pizzacost = 0 
salestaxamt = 0 
totalcost = 0
pizzatype = 0
randomname = 0
rand = 0 
sizelist = [SMALL_PIZZA, MEDIUM_PIZZA, LARGE_PIZZA, EXTRA_LARGE_PIZZA]

# program functions 

def main():
    new_order = True 
    while new_order:
        get_pizza_order()
        calculate_price()
        display_receipt()
        yesno = input("\nWould you like to place another order? Y/N")
        if yesno.upper() != "Y":
            new_order = False       



def get_pizza_order():
    global pizzacost, salestaxamt, totalcost, pizzatype, random, randomname
    inout =(input("\nWhat pizza size would you like? Enter S for Small, M for Medium, L for Large, X for Extra Large."))
    if inout == 'S' or inout == 's': 
        pizzacost = SMALL_PIZZA
        pizzatype = 'Small'
    elif inout == 'M' or inout == 'm':
        pizzacost = MEDIUM_PIZZA
        pizzatype = 'Medium'
    elif inout == 'L' or inout == 'l':
        pizzacost = LARGE_PIZZA
        pizzatype = 'Large'
    elif inout == 'X' or inout == 'x':
        pizzacost = EXTRA_LARGE_PIZZA
        pizzatype = 'Extra Large'
    else:
        random.shuffle(sizelist)
        rand = sizelist[0]
        print("\nInvalid response, random pizza size chosen.")
        if rand == SMALL_PIZZA:
            randomname = 'Small'
        elif rand == MEDIUM_PIZZA:
            randomname = 'Medium'
        elif rand == LARGE_PIZZA:
            randomname = 'Large'
        elif rand == EXTRA_LARGE_PIZZA:
            randomname = 'Extra Large'
        pizzatype = 'Random: '+str(randomname)
        pizzacost = rand
    
def calculate_price(): 
    global salestaxamt, totalcost, pizzacost, SALES_TAX
    salestaxamt = pizzacost * SALES_TAX
    totalcost = pizzacost + salestaxamt
    
def display_receipt():
    print('\n------------------------------')
    print('Pizza type selected:     ' +str(pizzatype))
    print('Price:                   $' +str(pizzacost))
    print('Sales Tax:               $',format(salestaxamt,'.2f'))
    print('\n------------------------------')
    print('Total Cost:              $',format(totalcost,'.2f'))
    print('\n------------------------------')
    print(str(datetime.datetime.now()))
    
    
main()
