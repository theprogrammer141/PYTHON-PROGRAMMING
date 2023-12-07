account_number=int(input("Enter account number (-1 to end):"))
    
while account_number!=-1:
        initial_balance=float(input("Enter initial balance:"))
        total_charges=float(input("Enter total charges:"))
        total_credits=float(input("Enter total credits:"))
        credit_limit=float(input("Enter credit limit:"))
        
        new_balance=initial_balance+total_charges-total_credits
        
        print("\nAccount:",account_number)
        print("Credit limit:",credit_limit)
        print("Balance:",format(new_balance, ".2f"))
        
        if new_balance>credit_limit:
            print("Credit Limit Exceeded\n")
        else:
            print("\n")
            
        account_number=int(input("Enter account number (-1 to end): "))