import tkinter as tk
from tkinter import messagebox
# Importing validation function to check expense inputs and data management functions for expenses
from validation import validate_expense
from data_management import add_expense, get_all_expenses

def open_details_window():
    # Open a window to add new expense details
    def submit_form():
        # Collects, validates, and submits the expense form
        name = expense_name_var.get()  # Fetches entered expense name
        amount = expense_amount_var.get()  # Fetches entered amount
        # Validates the entered expense details
        valid, error_message = validate_expense(name, amount)
        if not valid:  # If validation fails, show an error message
            messagebox.showerror("Validation Error", error_message)
            return
        # If validation passes, add the expense
        add_expense(name, float(amount))
        messagebox.showinfo("Success", "Expense added successfully.")
        details_window.destroy()  # Close the add expense window after submission

    details_window = tk.Toplevel(root)  # Creates a new window on top of the main window
    details_window.title('Add New Expense')
    details_window.geometry("500x300")  # Sets the geometry of the add expense window

    # Variables to hold user input from the form
    expense_name_var = tk.StringVar()  # For expense name input
    expense_amount_var = tk.StringVar()  # For expense amount input

    # Setting up UI elements for the add expense form
    tk.Label(details_window, text="Expense Name:").pack()
    tk.Entry(details_window, textvariable=expense_name_var).pack()
    tk.Label(details_window, text="Amount:").pack()
    tk.Entry(details_window, textvariable=expense_amount_var).pack()
    tk.Button(details_window, text="Submit", command=submit_form).pack()

def display_expenses():
    # Displays all the recorded expenses in a new window
    expenses = get_all_expenses()  # Retrieves all expenses
    total_expenses = sum(amount for _, amount in expenses)  # Calculates the total of all expenses

    expenses_window = tk.Toplevel(root)  # New window for displaying expenses
    expenses_window.title("All Expenses")
    expenses_window.geometry("400x300")  # Sets the geometry of the expenses window

    # Displaying total expenses and each expense item
    tk.Label(expenses_window, text=f"Total Expenses: ${total_expenses:.2f}").pack()
    for expense in expenses:
        tk.Label(expenses_window, text=f"{expense[0]}: ${expense[1]:.2f}").pack()


# Main window setup
root = tk.Tk()  # Main application window
root.title('Personal Expense Tracker')
root.geometry("600x400")  # Sets the main window size


# Main window buttons
tk.Button(root, text="Add Expense", command=open_details_window).pack(pady=10)
tk.Button(root, text="View Expenses", command=display_expenses).pack(pady=10)
tk.Button(root, text="Exit", command=root.quit).pack(pady=10)  # Exits the application

root.mainloop()  # Starts the Tkinter event loop
