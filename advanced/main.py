def format_name():
    while True:
        name = input("Enter a name (Last, First): ").strip()

        if "," not in name:
            print("Please enter the name as: Last, First\n")
            continue

        last, first = name.split(",", 1)
        last = last.strip()
        first = first.strip()

        if last == "" or first == "":
            print("Please enter both a last name and first name.\n")
            continue

        print(f"{first.title()}  + {last.title()}\n")
        return


def format_title():
    while True:
        title = input("Enter a title: ").strip()

        if title == "":
            print("Input cannot be empty.\n")
            continue

        title = title.replace(",", " ")
        title = title.replace(":", " ")
        words = title.split()
        new_title = " ".join(words).title()

        print("\nProcessed String:")
        print(new_title + "\n")
        return


def format_list():
    while True:
        items = input("Enter a comma-separated list: ").strip()

        if items == "":
            print("Input cannot be empty.\n")
            continue

        item_list = items.split(",")
        new_list = []

        for item in item_list:
            item = item.strip()
            if item == "":
                new_list = []
                break
            new_list.append(item.upper())

        if new_list == []:
            print("Please enter items separated by commas.\n")
            continue

        print("\nProcessed String:")
        print(" | ".join(new_list) + "\n")
        return


def process_numbers():
    while True:
        numbers = input("Enter comma-separated numbers: ").strip()

        if numbers == "":
            print("Input cannot be empty.\n")
            continue

        try:
            number_list = []
            for value in numbers.split(","):
                number_list.append(int(value.strip()))
        except ValueError:
            print("Please enter whole numbers separated by commas.\n")
            continue

        total = sum(number_list)
        average = total / len(number_list)

        print("\nProcessed String:")
        print("Total: " + str(total))
        print("Average: " + str(average) + "\n")
        return


def main():
    while True:
        print("Choose how you would like to process a string:\n")
        print("1. Format a Name")
        print("2. Format a Title")
        print("3. Format a List")
        print("4. Process Numbers\n")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            format_name()
        elif choice == "2":
            format_title()
        elif choice == "3":
            format_list()
        elif choice == "4":
            process_numbers()
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.\n")
            continue

        again = input("Would you like to process another string? (yes/no): ").strip().lower()

        if again != "yes":
            print("Goodbye!")
            break


main()