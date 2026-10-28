expenses = []
while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Search Expense")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter expense name: ")
        try:
            amount = float(input("Enter expense amount: Rs. "))
            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                expenses.append([name, amount])
                print("Expense added successfully!")
        except ValueError:
            print("Please enter a valid amount.")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            print("\n--- Your Expenses ---")

            for i, expense in enumerate(expenses, start=1):
                print(
                    f"{i}. {expense[0]} - Rs. {expense[1]:.2f}"
                )

    elif choice == "3":
        total = 0
        for expense in expenses:
            total += expense[1]
        print(f"Total Expenses: Rs. {total:.2f}")

    elif choice == "4":
        search_name = input("Enter expense name to search: ").lower()
        found = False
        for expense in expenses:
            if search_name in expense[0].lower():
                print(f"{expense[0]} - Rs. {expense[1]:.2f}")
                found = True
        if not found:
            print("Expense not found.")

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
