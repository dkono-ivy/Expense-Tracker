# data_management.py

def add_expense(name, amount):
    """Add an expense to a simple text file."""
    with open("expenses.txt", "a") as file:
        file.write(f"{name}, {amount}\n")

def get_all_expenses():
    """Retrieve all expenses from the text file."""
    expenses = []
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                name, amount = line.strip().split(", ")
                expenses.append((name, float(amount)))
    except FileNotFoundError:
        print("Expenses file not found. No expenses to load.")
    return expenses
