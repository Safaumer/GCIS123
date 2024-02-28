"""
Group2 activity- Safa Umer and Joud Abed
This program codes a currency converter. The main function prompts the user for different choices 
such as the currency type, the amount to be converted and gives an output of a converted currency.

"""




def aed_usd(amount):
    exchange_rate=0.27
    money=exchange_rate*amount
    print("AED", amount," is equal to USD",money,"\n")

def aed_eur(amount):
    exchange_rate=0.25
    money=exchange_rate*amount
    print("AED",amount," is equal to EUR",money,"\n")

def aed_gbp(amount):
    exchange_rate=0.21
    money=exchange_rate*amount
    print("AED", amount," is equal to GBP",money,"\n")

def usd_aed(amount):
    exchange_rate=3.67
    money=exchange_rate*amount
    print("USD", amount," is equal to AED",money,"\n")

def eur_aed(amount):
    exchange_rate=3.98
    money=exchange_rate*amount
    print("EUR", amount," is equal to AED",money,"\n")

def gbp_aed(amount):
    exchange_rate=4.66
    money=exchange_rate*amount
    print("USD", amount," is equal to AED",money,"\n")

#the above functions does the actual calculations for the conversions.   


def aed_to_others():
    y="y"
    while y=='y':
        choice3=int(input("\nSelect the currency you want to convert AED to\n1.AED to US DOLLAR\n2.AED to EURO \n3.AED to BRITISH POUND\n4.EXIT\n\nEnter your choice: "))

        if choice3==1:
            aedvalue=int(input("Enter the amount:"))
            aed_usd(aedvalue)
       
        elif choice3==2:
            aedvalue=int(input("Enter the amount:"))
            aed_eur(aedvalue)
       
        elif choice3==3:
            aedvalue=int(input("Enter the amount:"))
            aed_gbp(aedvalue)
           
        elif choice3==4:
            y="n"

        else:
            print("Invalid input. Try Again.")
            continue
        y=input("Do you still want to continue with aed to other currency conversion? y/n\n\nEnter your choice: ")
        
            


def main():
    print("************** Currency Converter ******************")
    print("\t\tMAIN MENU")
    print("_____________________________________________")
    x="y"  
    while x=="y":
        choice1=int(input("\nSelection the conversion direction: \n\n1.AED to Other currencies\n2.Other Currencies to AED\n3.Exit\n\nEnter your choice: "))
        if choice1==1:
            print("\nYou selected conversion from AED TO OTHER CURRENCY \n\n")
            choice2=int(input("To confirm your choice enter '0'\nTo go back to previous menu enter '1'\n\nEnter your choice:  "))
            if choice2==0:
                aed_to_others()
                x=input("Do you want to continue with converter program y/n?\n\nEnter your choice: ")

            else:
                continue
        elif choice1==2:
            print("\nYou selected conversion from OTHER CURRENCY TO AED \n\n")
            choice2=int(input("To confirm your choice enter '0'\nTo go back to previous menu enter '1'\n\nEnter your choice: "))
            if choice2==0:
                #others_to_aed()
                x=input("Do you want to continue with converter program y/n?\n\nEnter your choice: ")
            else:
                continue

        elif choice1==3:
            print("\nYou selected to exit from the program\n\n")
            choice2=int(input("To confirm your choice enter '0'\nTo go back to previous menu enter '1'\n\nEnter your choice: "))
            if choice2==0:
                x=False
                break
            else:
                continue
           
        else:
            print("You've given an invalid input. Please try again")
            continue
    print("Thank You")
           
if __name__=="__main__" :
    main()