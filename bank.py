# Simple Banking Project (Procedural)

print("===================================")
print("     Welcome to Python Bank")
print("===================================")

name = input("Enter your name: ")
balance = 0

print("\nAccount created successfully!")
print("Account Holder:", name)
print("Current Balance:", balance)

while True:
    print("\n========== MENU ==========")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        
        if amount > 0:
            balance = balance + amount
            print("Deposit successful!")
            print("Updated Balance:", balance)
        else:
            print("Invalid amount!")

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))

        if amount <= balance:
            balance = balance - amount
            print("Withdrawal successful!")
            print("Updated Balance:", balance)
        else:
            print("Insufficient balance!")

    elif choice == "3":
        print("Your current balance is:", balance)

    elif choice == "4":
        print("Thank you for banking with us!")
        break

    else:
        print("Invalid choice! Please try again.")