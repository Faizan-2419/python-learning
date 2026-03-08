#List to store expenses
expenses=[]
#Function to add expense
def add_expense():
    print("\n-Add Expense-")
    date=input("Enter date(DD-MM-YYYY):")
    category=input("Enter category (Food,Travel,etc...):")
    description=input("Enter description:")
    amount=input("Enter amount:")

    # Convert amount to float
    try:
        amount=float(amount)
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    # Create expense dictionary
    
    expense={
        "date":date,
        "category": category,
        "description":description,
        "amount":amount
    }

    expenses.append(expense)
    print("Expense added successfully!!!...")

# Function to view all expenses
def view_expenses():
    print("\n-All Expenses-")
    if len(expenses)==0:
        print("No expenses recorded yet")
        return

    total=0
    for i,exp in enumerate(expenses,start=1):
        print(f"{i}.Date:{exp['date']}\nCategory:{exp['category']}\nDescription:{exp['description']}\nAmount:{exp['amount']}")
        total+=exp['amount']

    print(f"Total Expenses:{total}")

# Function to delete expense
def delete_expense():
    print("\n-Delete Expense-")
    if len(expenses)==0:
        print("No expenses to delete.")
        return

    view_expenses()
    choice=input("Enter expense number to delete:")

    try:
        index=int(choice)-1
        if 0<=index<len(expenses):
            removed=expenses.pop(index)
            print(f"Removed expense:{removed['description']}of amount{removed['amount']}")
        else:
            print("Invalid number")
    except ValueError:
        print("Please enter a valid number.")

# Function to show summary by category
def show_summary():
    print("\n-Expense Summary-")
    if len(expenses)==0:
        print("No expenses recorded yet.")
        return

    summary={}
    for exp in expenses:
        cat=exp['category']
        if cat in summary:
            summary[cat]+=exp['amount']
        else:
            summary[cat]=exp['amount']

    print("Category-wise total:")
    for cat,amt in summary.items():
        print(f"{cat}:{amt}")

# Main program loop
while True:
    print("\n--Expense Tracker--")
    print("1--> Add Expense")
    print("2--> View Expenses")
    print("3--> Delete Expense")
    print("4--> Expense Summary")
    print("5--> Exit")

    choice=input("Enter your choice:")

    if choice=="1":
        add_expense()
    elif choice=="2":
        view_expenses()
    elif choice=="3":
        delete_expense()
    elif choice=="4":
        show_summary()
    elif choice=="5":
        print("Exiting program")
        break
    else:
        print("Invalid choice. Please try again.")