

# 'Class' 

# class student:            # class
#     pass




# 'object'

# Jasil = student()         # object
# print(id(Jasil))


# 'object'

# Yaseen = student()        # object
# print(id(Yaseen))










# class Student:                                              # class

#     '''Methods'''
#     def exam(self):                                         # method                  
#         print("Exam conducted on 08/05/2026")
    

# jasil = Student()                                           # object
# yaseen = Student()                                          # object


# jasil.exam()                                                # Exam conducted on 08/05/2026
# yaseen.exam()                                               # Exam conducted on 08/05/2026















# class Student:
#     school_name = "Quest innovative solution"  # Class Attributes

# jasil = Student()
# yaseen = Student()

# print(Student.school_name)                     # class name vech access
# print(jasil.school_name)                       # object vech access


# 'Reassign'
# Student.school_name = "Qis"
# print(Student.school_name)                     # Qis      
# print(jasil.school_name)                       # Qis


# 'Object nte value maatram change aakkan (jasil nte)'
# jasil.school_name = "ALP School Adivaram"
# print(jasil.school_name)                      # ALP School Adivaram
# print(yaseen.school_name)                     # Qis















# class Human():
#     no_of_leg = 2
#     no_of_hand = 2

# x=Human()
# y=Human()

# y.no_of_leg = 1
# print(x.no_of_leg)         # 2
# print(y.no_of_leg)         # 1











'Delete'

# class Student:
#     school_name = "Quest innovative solution"  # Class Attributes

# jasil = Student()
# yaseen = Student()

# # print(Student.school_name)                     # class name vech access
# # print(jasil.school_name)                       # object vech access


# 'Reassign'
# Student.school_name = "Qis"
# # print(Student.school_name)                     # Qis      
# # print(jasil.school_name)                       # Qis


# 'Object nte value maatram change aakkan (jasil nte)'
# jasil.school_name = "ALP School Adivaram"
# # print(jasil.school_name)                      # ALP School Adivaram
# # print(yaseen.school_name)                     # Qis



# 'Delete'
# del Student.school_name
# del jasil.school_name

# # print(jasil.school_name)                   # error
# # print(yaseen.school_name)                    # error

# # print(Student.school_name)

