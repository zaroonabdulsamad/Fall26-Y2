balance=50000
while True:
    print("1.Check Balance")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Exit\n")
    choice=int(input("Enter Your Selected Desire: "))

    if choice==1:
        print("Your Balance is: ",balance)
    elif choice==2:
        amount=int(input("Enter the Amount: "))
        balance+=amount
        print(f"You successfuly Deposit,{amount} rupeees, and now your total Balnce is {balance}")
    elif choice==3:
        while True:
            amount = int(input("Enter the Amount: "))
            if amount>=0 and amount<=balance:
                break
            if amount>balance:
                print("Your Balnce is not sufficient for this transaction, Try Again with little amount")
            elif amount<0:
                print("Amount cannot be in negative.Please Try Again!")
            else:
                print("Amount must be greater then Zaro.")
        balance -= amount
        print(f"You have Successfuly Withdraw {amount} rupees and now yout total balance is {balance}")
    elif choice==4:
        print("Please Take your Card")
        break
    else:
        print("Invalid Choice, Try Again and choose correct from below, Thanks")
