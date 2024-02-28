def others_to_aed():
    z="y"
    while z=="y":
        choice3=int(input("Select the currency you want to convert AED to\n1.US DOLLAR to AED\n2.EURO to AED \n3.BRITISH POUND to AED\n4.EXIT\n\nEnter your choice: "))
        if choice3==1:
            aedvalue=int(input("Enter the amount:"))
            usd_aed(aedvalue)
       

        elif choice3==2:
            aedvalue=int(input("Enter the amount:"))
            eur_aed(aedvalue)
       
        elif choice3==3:
            aedvalue=int(input("Enter the amount:"))
            gbp_aed(aedvalue)
           
        elif choice3==4:
            break

        else:
            print("Invalid input. Try Again.")
            continue

        z=input("Do you still want to continue with aed to other currency conversion? y/n\n\nEnter your choice: ")
   
       



