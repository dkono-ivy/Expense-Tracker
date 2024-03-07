def validate_expense(name, amount):
    # Validates expense details, returning success status and error message.

    # Check if name is empty after removing whitespace
    if not name.strip():
        return False, "You must fill out all boxes."

    # Try converting amount to float and ensure it's positive
    try:
        amount = float(amount)
        if amount <= 0:
            return False, "The amount must be greater than 0."
    except ValueError:
        # Catch if amount isn't a number
        return False, "The amount must be a valid number."

    # If both checks pass, validation is successful
    return True, ""
