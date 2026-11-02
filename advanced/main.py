def format_name():
    """Prompts the user for a name, validates the format, and formats it."""
    while True:
        user_input = input("Enter a name (format: Last, First): ").strip()

        if not user_input:
            print("Input cannot be empty. Please try again.\n")
            continue

        if "," not in user_input:
            print("Please put a comma separating the last and first name (e.g., Smith, Alex).\n")
            continue



