
'Encapsulation'


# class Bank():
#     bank_name = 'Federal'

#     def __init__(self,acc_no,name,ifsc,balance):
#         self.__ac_no = acc_no
#         self.name = name
#         self.ifsc = ifsc
#         self.__balance = balance

#     def get_details(self):
#         print(f'----------\n Account No : {self.__ac_no}\n Name : {self.name}\n IFSC code : {self.ifsc}\n Balance : {self.__balance}\n----------')

#     def get_balance(self):
#         print("Current Balance : ",self.__balance)

#     def deposit(self,amount):
#         self.__balance += amount
#         print(f"Deposit successfull , Current Balance : {self.__balance}")
    
#     def withdrow(self,amount):
#         if amount > self.__balance:
#             print('insufficient bank balance')
#         else:
#             self.__balance -= amount
#             print(f'Transaction succesfull, Current Balace is {self.__balance}')



# jasil = Bank(999012 ,'Jasil' , 'FDRL999' ,45000)
# jasil.get_details()


# jasil.get_balance()
# jasil.deposit(500)

# jasil.withdrow(1000)

# print(jasil.__ac_no)          # AttributeError: 'Bank' object has no attribute '__ac_no'
# print(jasil.__balance)          # AttributeError: 'Bank' object has no attribute '__balance'.


