
# class Student():
#     school_name = 'QIS'                   # attributes
#     course = "Python Full Stack"          # attributes




#     def __init__(self):                    # constructor method
#         print("constructor created ...")



# jasil = Student() 
# yaseen = Student()









# class Student():
#     school_name = 'QIS'                   # attributes
#     course = "Python Full Stack"          # attributes


# # instance Attributes
#     def __init__(self,s_id, name, age, email):                    # constructor method

#         self.Student_id = s_id
#         self.Student_name = name
#         self.Student_age = age
#         self.Student_email = email


    
#     def get_details(self):
#         print(f'---------- \n Student id : {self.Student_id}\n Student Name : {self.Student_name}\n Student Age: {self.Student_age}\n Student email : {self.Student_email} \n----------')


# jasil = Student(s_id= 107 , name= "jasil", age= 21, email='jasilmuahmmed25@gmail.com')
# jasil.get_details()


# niyas = Student(s_id= 100 , name= "niyas", age= 20, email='niyas@icloud.com')
# niyas.get_details()










# class Empolyee():
#     company_name = "TCS"
#     Branch_name = "Kochi"


#     def __init__(self,e_id, e_name, e_salary, e_email):
#         self.employee_id=e_id
#         self.employee_name=e_name
#         self.employee_salary=e_salary
#         self.employee_email=e_email

    
#     def get_details(self):
#         print(f'---------- \nid : {self.employee_id}\nName : {self.employee_name}\nSalary : {self.employee_salary}\nEmail : {self.employee_email}\n----------')


#     def update_salary(self):

#         if self.employee_salary > 50000:
#             increment = self.employee_salary * 0.15
#             self.employee_salary += increment
#             print(f'Updated Salary : {self.employee_salary}')
    

#     def update_company(self):
#         self.company_name = "Google"
#         print(self.company_name)


#     # def __del__(self):
#     #     print("constructor deleted ...")





# jasil = Empolyee(e_id=102, e_name='Muhammed Jasil', e_salary=51000, e_email="jasilmuhammed25@gmail.com")
# yaseen = Empolyee(e_id=100, e_name='yaseen', e_salary=41000, e_email="yaseen45@gmail.com")

# # jasil.get_details()
# # # jasil.update_salary()

# # jasil.update_company()






















# class
#     BANK NAME
# isinstance 
# ACCOUNT NO, NAME, IFSC, BALANCE 
# METHODS
# GET DETAILS, GET BALANCE, WITHDROW ,DEPOSIT

# class Bank():
#     bank_name = 'Federal'

#     def __init__(self,acc_no,name,ifsc,balance):
#         self.ac_no = acc_no
#         self.name = name
#         self.ifsc = ifsc
#         self.balance = balance

#     def get_details(self):
#         print(f'----------\n Account No : {self.ac_no}\n Name : {self.name}\n IFSC code : {self.ifsc}\n Balance : {self.balance}\n----------')

#     def get_balance(self):
#         print("Current Balance : ",self.balance)

#     def deposit(self,amount):
#         self.balance += amount
#         print(f"Deposit successfull , Current Balance : {self.balance}")
    
#     def withdrow(self,amount):
#         if amount > self.balance:
#             print('insufficient bank balance')
#         else:
#             self.balance -= amount
#             print(f'Transaction succesfull, Current Balace is {self.balance}')



# jasil = Bank(999012 ,'Jasil' , 'FDRL999' ,45000)
# jasil.get_details()

# jasil.get_balance()
# jasil.deposit(500)

# jasil.withdrow(1000)
