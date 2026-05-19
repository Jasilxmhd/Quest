'Basic Level'

# 1. Student Class

# Create a class named Student.
# Add a class attribute school_name = "ABC School"
# Create two objects.
# Display the school name using both objects.

# class Student():
#     school_name = 'ABC School'

# member1 = Student()
# member2 = Student()

# print(member1.school_name)
# print(member2.school_name)

# 2. Mobile Class

# Create a class named Mobile.
# Add class attributes:
# brand = "Samsung"
# country = "Korea"
# Create an object and print both attributes.

# class Mobile():
#     brand = "Samsung"
#     country = "Korea"

# iphone = Mobile()
# print(iphone.brand)
# print(iphone.country)


    
# 3. Employee Class

# Create a class named Employee.
# Add a method show_company() that prints:
# "Company Name: TechSoft"
# Create an object and call the method.

# class Employee():
#     def show_company(self):
#         print('Company_Name: TechSoft')

# jasil = Employee()
# jasil.show_company()



# 4. Car Class

# Create a class named Car.
# Add class attribute wheels = 4
# Create two objects.
# Print the number of wheels using both objects.

# class Car():
#     wheel = '4'

# bmw = Car()
# audi = Car()

# print(bmw.wheel)
# print(audi.wheel)




# 5. College Class

# Create a class named College.
# Add a class attribute college_name = "Green Valley College"
# Add a method display() to print the college name.
# Create an object and call the method.
# Intermediate Level

# class College():
#     college_name = "Green Valley College"

#     def display(self):
#         print("Green Valley College")

# students = College()
# students.display()



# 6. Laptop Class Attribute Updation

# Create a class named Laptop.

# Add class attribute brand = "Dell"
# Print the brand.
# Update the class attribute to "HP"
# Print the updated value.

# class Laptop():
#     brand = 'Dell'
# # # print(Laptop.brand)

# Laptop.brand = "HP"
# print(Laptop.brand)

# 7. Hospital Class

# Create a class named Hospital.
# Add class attribute hospital_name = "City Hospital"
# Add method show() to display the hospital name.
# Create two objects and call the method using both objects.

# class Hospital():
#     hospital_name = "City Hospital"

#     def show(self):
#         print("hospital_name = City Hospital")

# docter = Hospital()
# nurse = Hospital()

# docter.show()
# nurse.show()

# 8. Bus Class

# Create a class named Bus.

# Add class attribute seats = 40
# Update the number of seats to 50
# Print the updated value.

# class Bus():
#     seats = 40

# Bus.seats = 50
# print(f'Updated Seats : {Bus.seats}')

# 9. Bank Class

# Create a class named Bank.

# Add class attribute bank_name = "Federal Bank"
# Add method display_bank() to print the bank name.
# Create an object and call the method.

# class Bank():
#     bank_name = "Federal Bank"

#     def display_bank(self):
#         print("Federal Bank")

# user = Bank()

# user.display_bank()
    


# 10. Movie Class

# Create a class named Movie.
# Add class attribute industry = "Mollywood"
# Delete the class attribute.
# Try printing the attribute after deletion.

# class Movile():
#     industry = "Mollywood"

# del Movile.industry
# print(Movile.industry)




'Advanced Level'

# 11. Book Class

# Create a class named Book.

# Add class attribute library = "Central Library"
# Add methods:
# show_library()
# update_library()
# Update the library name using the method and display the updated value.

# class Book():
#     library = "Central Library"

#     def show_library(self):
#         print(Book.library)

#     def update_library(self):
#         Book.library = "General Library"

# student = Book()

# student.show_library()

# student.update_library()
# student.show_library()

# 12. School Class Attribute Deletion

# Create a class named School.

# Add class attribute principal = "Ramesh"
# Print the attribute.
# Delete the attribute.
# Handle the error if the attribute is accessed after deletion.

# class School():
#     principal = "Ramesh"



# 13. TV Class

# Create a class named TV.

# Add class attribute company = "Sony"
# Create three objects.
# Update the class attribute to "LG"
# Show that the updated value is reflected in all objects.

# class Tv():
#     company = "Sony"

# obj = Tv()
# obj1 = Tv()
# obj2 = Tv()

# Tv.company = "LG"

# print(obj.company)
# print(obj1.company)
# print(obj2.company)

# 14. University Class

# Create a class named University.

# Add class attribute country = "India"
# Add method show_country()
# Create multiple objects and call the method.

# class University():
#     country = "India"

#     def show_country(self):
#         print(University.country)

# student = University()
# student1 = University()
# student2 = University()

# student.show_country()
# student1.show_country()
# student2.show_country()


# 15. Restaurant Class

# Create a class named Restaurant.

# Add class attribute type = "Veg"
# Update the attribute to "Multi Cuisine"
# Delete the attribute.
# Print suitable messages after each operation.

# class Restaurant():
#     type ="veg"

# Restaurant.type = "Multi Cuisine"
# print("Updated attributes :",Restaurant.type)

# del Restaurant.type
# print("Attribute 'type' deleted.")



'Challenge Questions'

# 16. Company Management

# Create a class named Company.

# Add class attribute company_name = "Infosys"
# Add methods to:
# Display company name
# Update company name
# Delete company name

# class Company():
#     company_name = "Infosys"

#     def get_display(self):
#         print('Company Name :',self.company_name)

    
#     def update(self):
#         self.company_name = "TCS"
#         print(f'updated name : {self.company_name}')

#     def delete(self):
#         del Company.company_name
#         print(f'company name has been deleted !')

# user = Company()

# user.get_display()
# user.update()
# user.delete()




# 17. Cricket Team

# Create a class named CricketTeam.

# Add class attribute team_name = "India"
# Create multiple objects.
# Change the team name to "Kerala"
# Display the updated value using all objects.

# class CricketTeam():
#     team_name = "India"

# player = CricketTeam()
# player1 = CricketTeam()

# CricketTeam.team_name = 'Kerala'

# print(player.team_name)
# print(player1.team_name)

# 18. ATM Machine

# Create a class named ATM.

# Add class attribute bank = "SBI"
# Add method show_bank()
# Delete the class attribute and check the output.

# class ATM():
#     bank = "SBI"

#     def show_bank(self):
#         print(f'Bank Name : {self.bank}')

# del ATM.bank
# print("class Attribute 'bank' deleted")
# print(ATM.show_bank)



# 19. Airline Class

# Create a class named Airline.

# Add class attribute airline_name = "Air India"
# Add methods to display and update the airline name.
# Create two objects and test the methods.

# class Airline():
#     airline_name = "Air India"

#     def get_display(self):
#         print(f'----------\n Airline Name : {self.airline_name}\n----------')


#     def update(self):
#         Airline.airline_name = 'Qatar airways'
#         print(f'----------\n Updated Name : {self.airline_name}\n----------')

# flight = Airline()
# flight1 = Airline()

# flight.get_display()
# flight.update()

# flight1.get_display()
# flight1.update()



# 20. Shopping Mall

# Create a class named Mall.

# Add class attribute mall_name = "Lulu Mall"
# Create objects.
# Update and delete the class attribute.
# Display outputs before and after each operation.

# class Mall():
#     mall_name = "Lulu Mall"

# hotel = Mall()

# Mall.mall_name = "Hilite Mall"
# print(f"updated mall : {Mall.mall_name}")

# del Mall.mall_name
# print(Mall.mall_name)
