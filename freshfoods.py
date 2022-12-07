# Name: Oladunni Opaleye 
# Prog Purpose: Find the gross pay, deductions, and net pay for an employee 
# based on the number of hours they worked and their job category.

''' Make a tuple for job categories and deduction rates (payrates & taxrates)
Ask for job category code (jobcat) + number of hours worked (hours).
Make a different variable (occupation) for the name of the profression chosen 
"If input = blank: occupation = 'blank'"
input = payrate & hours 
grosspay = hours * payrate

Then multiply the gross pay by all deduction rates 
grosspay * deductrate = deduct (add a number to the end of each deduction)

Make the program go through each value in the tuple. (Make sure to save deduction rates as the percentages, not the names)
Make the variable dr, and append the new rate every time
Then add all deductions together to get totaldeduct.
deduct1 + deduct2 + deduct3 + deduct4 = totaldeduct

After that, calculate the netpay
netpay = grosspay - totaldecut

Then make a fancy list of everything 

Occupation: 
Hours Worked: hours
Pay before deductions: grosspay
Total deductions: totaldeduct
Take home pay: netpay

'''
import datetime

jobcat = ('Cashier', 'Stocker', 'Janitor', 'Maintanence')
deductrates = (.12, .03, .062,.0145)

hours = 0 
jobinput = 0
payrate = 0
grosspay = 0

deduct_calc = []
dr = 0

deduct1 = 0 
deduct2 = 0 
deduct3 = 0 
deduct4 = 0


totaldeduct = 0 
netpay = 0 

def main():
    new_paycheck = True 
    while new_paycheck:
        get_gross_pay()
        calculate_deductions()
        display_paycheck()
        yesno = input("\nWould you like to make another calculation? Y/N")
        if yesno.upper() != "Y":
            new_paycheck = False
            
# First, get the jobcat and hours from the user.

def get_gross_pay():
    global hours, occupation, jobinput, payrate, grosspay
    job_calc = True
    occupation = 0
    while job_calc:
        jobinput = input("\nWhat is your job? Type C for Cashier, S for Stocker, J for Janitor, and M for Maintanence.")
        if jobinput == 'C' or jobinput == 'c':
            occupation = "Cashier"
            payrate = 16.50
        elif jobinput == 'S' or jobinput == 's':
            occupation = "Stocker"
            payrate = 16.50
        elif jobinput == 'J' or jobinput == 'j':
            occupation = "Janitor"
            payrate = 16.50    
        elif jobinput == 'M' or jobinput == 'm':
            occupation = "Maintanence"
            payrate = 16.50
        else:
            print("\nInvalid response. Please reenter information")
        if occupation == "Cashier" or occupation == "Stocker" or occupation == "Janitor" or occupation == "Maintanence":
            job_calc = False    
    hours = int(input("\nHow many hours do you work a week?"))
    grosspay = hours * payrate


def calculate_deductions():
    global totaldeduct, netpay, deduct_calc
    for deduction in deductrates:
        dr = grosspay * deduction
        deduct_calc.append(dr)
    for deduct in deduct_calc:
        totaldeduct += deduct
    netpay = grosspay - totaldeduct

    
def display_paycheck():
    print('\nFresh Food Marketplace Store Employee Weekly Pay')
    print('\n---------------------------------------------------')
    print('Occupation:                      ' +str(occupation))
    print('Hours Worked:                    ' +str(hours))
    print('Total Deductions:               $',format(totaldeduct,'.2f'))
    print('\n---------------------------------------------------')
    print('Take Home Pay                  $',format(netpay,'.2f'))
    print('\n---------------------------------------------------')
    print(str(datetime.datetime.now()))

main()
