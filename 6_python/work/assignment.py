# File Operation Program

while True:

    print("\n----- MENU -----")
    print("1. Enter Name")
    print("2. Enter Email")
    print("3. Enter Phone Number")
    print("4. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        name = input("Enter Name : ")

        file = open("userdata.txt", "a")
        file.write("Name : " + name + "\n")
        file.close()

        print("Name saved successfully")

    elif choice == "2":
        email = input("Enter Email : ")

        file = open("userdata.txt", "a")
        file.write("Email : " + email + "\n")
        file.close()

        print("Email saved successfully")

    elif choice == "3":
        phone = input("Enter Phone Number : ")

        file = open("userdata.txt", "a")
        file.write("Phone : " + phone + "\n")
        file.close()

        print("Phone Number saved successfully")

    elif choice == "4":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")