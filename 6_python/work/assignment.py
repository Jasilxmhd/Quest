
while True:

    print("\n----- MENU -----")
    print("1. List all records")
    print("2. Add records")
    print("3. Edit Record")
    print("4. Delete Record")
    print("5. Exit")
 

    choice = input("Enter your choice : ")

    if choice == "1":

        file = open('userdata.txt', 'r')

        print('\n------ Display Records ------')
        print(file.read())

        file.close()
        
        break

    elif choice == "2":

        print('\n------ Add Records ------')

    name = input('Enter Name : ')

    phones = []
    emails = []


    while True:

        phone = input("Enter Phone Number : ")

        if phone.startswith("+91 ") and len(phone) == 14:
            phones.append(phone)
        else:
            print("Invalid Phone Number")
            continue

        more = input("Add Another Phone Number? (yes/no) : ")

        if more.lower() != "yes":
            break


    while True:

        email = input("Enter Email : ")

        if email.endswith("@gmail.com"):
            emails.append(email)
        else:
            print("Invalid Email")
            continue

        more = input("Add Another Email? (yes/no) : ")

        if more.lower() != "yes":
            break


    file = open("userdata.txt", "a")

    file.write("\nName : " + name + "\n")

    file.write("Phone Numbers :\n")

    for p in phones:
        file.write("- " + p + "\n")

    file.write("Emails :\n")

    for e in emails:
        file.write("- " + e + "\n")

    file.write("----------------------\n")

    file.close()

    print("Records Added Successfully")