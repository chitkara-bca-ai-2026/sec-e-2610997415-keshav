import os

FILENAME = "daily_log.txt"


if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as f:
        f.write("09:00 - Office opened\n")
        f.write("10:30 - Team meeting held\n")
        f.write("13:00 - Lunch break\n") 

def append_entry(filename, entry):
    with open(filename, "a") as f:
        f.write(entry + "\n")
    print("Log entry added successfully.")

def display_log(filename):
    with open(filename, "r") as f:
        entries = f.read().splitlines()
    print(f"\n--- Daily Log ({len(entries)} entries) ---")
    for i, entry in enumerate(entries, 1):
        print(f"{i}. {entry}")

while True:
    print("\n1. Add Log Entry")
    print("2. Display Complete Log")
    print("3. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        entry = input("Enter log message: ")
        append_entry(FILENAME, entry)

    elif choice == "2":
        display_log(FILENAME)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1 to 3.")