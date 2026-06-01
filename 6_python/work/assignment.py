# while True:

#     print("\n----- MENU -----")
#     print("1. List all records")
#     print("2. Add records")
#     print("3. Edit Record")
#     print("4. Delete Record")
#     print("5. Exit")

#     choice = input("Enter your choice : ")

#     if choice == "1":

#         file = open("userdata.txt", "r")

#         print("\n------ Display Records ------")
#         print(file.read())

#         file.close()

#     elif choice == "2":

#         print("\n------ Add Records ------")

#         name = input("Enter Name : ")

#         phones = []
#         emails = []

#         while True:

#             phone = input("Enter Phone Number : ")

#             if phone.startswith("+91 ") and len(phone) == 14:
#                 phones.append(phone)
#             else:
#                 print("Invalid Phone Number")
#                 continue

#             more = input("Add Another Phone Number? (yes/no) : ")

#             if more.lower() != "yes":
#                 break

#         while True:

#             email = input("Enter Email : ")

#             if email.endswith("@gmail.com"):
#                 emails.append(email)
#             else:
#                 print("Invalid Email")
#                 continue

#             more = input("Add Another Email? (yes/no) : ")

#             if more.lower() != "yes":
#                 break

#         file = open("userdata.txt", "a")

#         file.write("\nName : " + name + "\n")

#         file.write("Phone Numbers :\n")

#         for p in phones:
#             file.write("- " + p + "\n")

#         file.write("Emails :\n")

#         for e in emails:
#             file.write("- " + e + "\n")

#         file.write("----------------------\n")

#         file.close()

#         print("Records Added Successfully")

#     elif choice == "3":

#         print("\n------ Edit Records ------")

#         search_name = input("Enter Name To Edit : ")

#         file = open("userdata.txt", "r")
#         lines = file.readlines()
#         file.close()

#         found = False
#         new_data = []

#         i = 0

#         while i < len(lines):

#             if lines[i].strip() == "Name : " + search_name:

#                 found = True

#                 print("Record Found")

#                 change_name = input("Do You Want To Change Name? (yes/no) : ")

#                 if change_name.lower() == "yes":
#                     new_name = input("Enter New Name : ")
#                 else:
#                     new_name = search_name

#                 old_phones = []
#                 old_emails = []

#                 j = i + 2

#                 while not lines[j].startswith("Emails"):
#                     old_phones.append(lines[j].replace("- ", "").strip())
#                     j += 1

#                 j += 1

#                 while lines[j].strip() != "----------------------":
#                     old_emails.append(lines[j].replace("- ", "").strip())
#                     j += 1

#                 phones = []

#                 change_phone = input("Do You Want To Change Phone Numbers? (yes/no) : ")

#                 if change_phone.lower() == "yes":

#                     while True:

#                         phone = input("Enter New Phone Number : ")

#                         if phone.startswith("+91 ") and len(phone) == 14:
#                             phones.append(phone)
#                         else:
#                             print("Invalid Phone Number")
#                             continue

#                         more = input("Add Another Phone Number? (yes/no) : ")

#                         if more.lower() != "yes":
#                             break

#                 else:
#                     phones = old_phones

#                 emails = []

#                 change_email = input("Do You Want To Change Emails? (yes/no) : ")

#                 if change_email.lower() == "yes":

#                     while True:

#                         email = input("Enter New Email : ")

#                         if email.endswith("@gmail.com"):
#                             emails.append(email)
#                         else:
#                             print("Invalid Email")
#                             continue

#                         more = input("Add Another Email? (yes/no) : ")

#                         if more.lower() != "yes":
#                             break

#                 else:
#                     emails = old_emails

#                 new_data.append("Name : " + new_name + "\n")
#                 new_data.append("Phone Numbers :\n")

#                 for p in phones:
#                     new_data.append("- " + p + "\n")

#                 new_data.append("Emails :\n")

#                 for e in emails:
#                     new_data.append("- " + e + "\n")

#                 new_data.append("----------------------\n")

#                 i = j

#             else:
#                 new_data.append(lines[i])

#             i += 1

#         if found:

#             file = open("userdata.txt", "w")

#             for line in new_data:
#                 file.write(line)

#             file.close()

#             print("Record Modified Successfully")

#         else:
#             print("Record Not Found")

#     elif choice == "4":

#         print("\n------ Delete Record ------")

#         search_name = input("Enter Name To Delete : ")

#         file = open("userdata.txt", "r")
#         lines = file.readlines()
#         file.close()

#         found = False
#         new_data = []

#         i = 0

#         while i < len(lines):

#             if lines[i].strip() == "Name : " + search_name:

#                 found = True

#                 print("Record Deleted Successfully")

#                 i += 1

#                 while i < len(lines) and lines[i].strip() != "----------------------":
#                     i += 1

#             else:
#                 new_data.append(lines[i])

#             i += 1

#         if found:

#             file = open("userdata.txt", "w")

#             for line in new_data:
#                 file.write(line)

#             file.close()

#         else:
#             print("Record Not Found")


#     elif choice == "5":

#         print("Program Closed")
#         break

#     else:
#         print("Invalid Choice")