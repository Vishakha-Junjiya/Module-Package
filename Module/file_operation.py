def create_file():
    name=input("\nEnter file name: ")
    f=open(name,"x")
    f.close()
    print("File created succesfully!")
    print("-----------------------------")
    print("-----------------------------")
def write_file():
    name=input("\nEnter file name: ")
    data=input("Enter data to write:")
    f=open(name,"w")
    f.write(f"{data}\n")
    f.close()
    print("Data written successfully!")
    print("-----------------------------")
    print("-----------------------------")
def read_file():
    name=input("\nEnter file name: ")
    with open(name,"r") as f:
        print("File Content: \n")
        print(f.read())
        print("-----------------------------")
        print("-----------------------------")
def append_file():
    name=input("\nEnter file name: ")
    data=input("Enter data to append:")
    f=open(name,"a")
    f.write(f"{data}\n")
    f.close()
    print("Data Append successfully!")
    print("-----------------------------")
    print("-----------------------------")

def file_op():
    print("File Operations:")
    while True:
        print("\n1.Create a new file")
        print("2.Write to a file")
        print("3.Read from a file")
        print("4.Append to a file")
        print("5.Back to Main Menu")
        choice=int(input("\nEnter your choice:"))

        if choice == 1:
            create_file()
        elif choice == 2:
            write_file()
        elif choice == 3:
            read_file()
        elif choice == 4:
           append_file()
        elif choice == 5:
            break