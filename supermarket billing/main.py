from checkoutregister import CheckOutRegister

checkout=CheckOutRegister()

def start():
    
    customer_decision='y'
    while customer_decision == 'y':
        checkout.clear_value()
        print("")
        
        while True:
            barcode= input("Please Enter the barcode of your item: ")
            #counting how many item are being buyed
            #passing barcode to find item
            checkout.get_prod_detail(barcode)

            #making decision either to scan more item or not
            addDecision=input("Would you want to scan more product? (Y/n) ")
            if(str(addDecision).lower()== 'n'):
                break
            elif(str(addDecision).lower()!='y'):
                print("You entered invalid option!")
                break;

        #receiving amount from the customer
        cost=checkout.total_payable()
        due=cost
        amt_rec=0.0
        while (cost>0):
            try:
                print("\nYour due amount = $"+str(cost))
                amt=float(input("Please enter amount to pay: "))
                if (amt<0):
                    print("We dont accept negative")
                else:
                    amt_rec+=float(amt)
                    cost=cost-amt
            except ValueError:
                print("\nplease enter valid amount")
        #===========printing receipt=======================
        print("\n======= Final Receipt======")
        checkout.total_item()
        return_money=amt_rec-due
        print('\n{:>12} {:>16}'.format("Total Cost: ","$"+str(due)))
        print('{:>12} {:>12}'.format("Amount Received:","$"+str(amt_rec)))
        print('{:>12} {:>12}'.format("Change Returned:","$"+str(return_money)))
        print("\n Thank you for shopping with us")
        customer_decision=input("\nNext customer or Quit? (y/q):")
        
    
start()

