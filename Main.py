from Module.Operation import (datetime_timeop, math_operation, random_data, uuid_operation, module_attribute)
from Module.file_operation import file_op


def main():
    print("----------------------------")
    print("----------------------------")
    print("Welcome to Multi-Utility Toolkit")
    print("----------------------------")
    print("----------------------------")

    while True:
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operation (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        print("----------------------------")
        print("----------------------------")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            datetime_timeop()
        elif choice == 2:
            math_operation()
        elif choice == 3:
            random_data()
        elif choice == 4:
            uuid_operation()
        elif choice == 5:
            file_op()
        elif choice == 6:
            module_attribute()
        elif choice == 7:
            print("------------------------------")
            print("Thank you for using the Multi-Utility Toolkit!")
            print("------------------------------")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()

