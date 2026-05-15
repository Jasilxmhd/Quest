
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










class Empolyee():
    company_name = "TCS"
    Branch_name = "Kochi"


    def __init__(self,e_id, e_name, e_salary, e_email):
        self.employee_id=e_id
        self.employee_name=e_name
        self.employee_salary=e_salary
        self.employee_email=e_email

    
    def get_details(self):
        print(f'---------- \nid : {self.employee_id}\nName : {self.employee_name}\nSalary : {self.employee_salary}\nEmail : {self.employee_email}\n----------')


    def update_salary(self):

        if self.employee_salary > 50000:
            increment = self.employee_salary * 0.15
            self.employee_salary += increment
            print(f'Updated Salary : {self.employee_salary}')
    

    def update_company(self):
        self.company_name = "Google"
        print(self.company_name)






jasil = Empolyee(e_id=102, e_name='Muhammed Jasil', e_salary=51000, e_email="jasilmuhammed25@gmail.com")
jasil.get_details()
# jasil.update_salary()

jasil.update_company()