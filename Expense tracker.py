

def main():
    total = 0  # the accumulator, starts at zero

    print("----- DecodeLabs Expense Tracker -----")
    print("Enter each expense amount one at a time.")
    print("Type 'done' when you're finished.\n")

    while True:
        entry = input("Enter expense amount (or 'done' to finish): ").strip()

        if entry.lower() == "done":
            break

        try:
            expense = float(entry)
        except ValueError:
            print(" -> Please enter a valid number (e.g., 100, 50, 20).\n")
            continue

        if expense < 0:
            print(" -> Expense cannot be negative.\n")
            continue

        total = total + expense  # accumulator in action
        print(f" -> Added {expense:.2f}. Running total: {total:.2f}\n")

    print("----------------------------------------")
    print(f"Total Spent: {total:.2f}")
    print("----------------------------------------")


if __name__ == "__main__":
    main()