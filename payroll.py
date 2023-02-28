# Project: Payroll - Retroactive Salery
# Author:  Taylor Johnson
# Date:    8/20/2020

def main():

    #Introduction
    print()
    print("Retroactive Calculator!")
    print()
    print("This application will help you figure out the income")
    print("owed to an employee from the previous pay period!")
    print()

    #Output
    saleryinc = float(input("What is the percentage increase in salary?"))
    months_due = int(input("How many months is the increase retroactive?"))
    currentsal = float(input("What is the current annual salary?"))

    #Varriables
    monthly_sal = currentsal / 12
    monthly_inc = monthly_sal * (saleryinc / 100)
    payback =  months_due * monthly_inc
    new_monthly_sal = monthly_inc + monthly_sal
    new_yearly_sal = new_monthly_sal * 12 

    #Inputs
    print()
    print("Current Information:")
    print()
    print("Percentage increase in salery:", '  ', saleryinc, "%")
    print("Months increase is retroactive:", ' ', months_due)
    print("Current monthly salary:", '        $', ('{:.2f}'.format(monthly_sal)))
    print("Current annual salary:", '         $', ('{:.2f}'.format(currentsal)))
    print()
    print("New Information:")
    print()
    print("Monthy increase:", '               $', ('{:.2f}'.format(monthly_inc)))
    print("Amount of payback:", '             $', ('{:.2f}'.format(payback)))
    print("New monthly salary:", '            $', ('{:.2f}'.format(new_monthly_sal)))
    print("New annual salary:", '             $', ('{:.2f}'.format(new_yearly_sal)))

main()




