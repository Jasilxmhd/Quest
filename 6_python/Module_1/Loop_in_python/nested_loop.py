

# 0
# 01
# 012

# for i in range(1,4):
#     for j in range(i):
#         print(j,end="")
#     print()










# * * * * * * 
# * * * * * * 
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *

# square patern 
# row = 6
# for i in range(row):
#     for j in range(row):
#         print("*",end=" ")
#     print()











# * * * 
# * * * 
# * * *
# * * *

# print  rectangle 
# length = 4
# width = 3
# for i in range(length):
#     for j in range(width):
#         print("*",end=" ")
#     print()












# * * * * * * 
# *         * 
# *         *
# *         *
# *         *
# * * * * * *


# n = 6
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         if row == 1 or row == n or col == 1 or col == n :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()












# 0000
# 1111
# 2222
# 3333

# row = 4
# col = 4
# for i in range(row):
#     for j in range(col):
#         print(i,end=" ")
#     print()





# 1234
# 1234
# 1234
# 1234

# row = 4
# col = 4
# for i in range(1,row+1):
#     for j in range(1,col+1):
#         print(j,end=" ")
        
#     print()






# 123
# 456
# 789

# row = 3
# col = 3
# n = 1
# for i in range(3):
#     for j in range(3):
#         print(n,end=" ")
#         n=n+1
#     print()





# 5  10 15
# 20 25 30
# 35 40 45

# row = 3
# col = 3
# n = 5
# for i in range(3):
#     for j in range(3):
#         print(n,end=" ")
#         n= n+5
#     print()











# * 
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * * * *
# * * * * * * * *
# * * * * * * * * *

# print right angle triangle
# row = 10
# for i in range(row):
#     for j in range(i):
#         print("*",end=" ")
        
#     print()










# 0 
# 0 1
# 0 1 2
# 0 1 2 3

# row = 4

# for i in range(row+1):
#     for j in range(i):
#         print(j,end=" ")

        
#     print()










# 1 
# 2 3
# 4 5 6
# 7 8 9 10


# row = 5

# n = 1
# for i in range(row):
#     for j in range(i):
#         print(n,end=" ")
#         n=n+1
#     print()










#  *   *   *   *   *   *   *   *  
#  *   *   *   *   *   *   *  
#  *   *   *   *   *   *  
#  *   *   *   *   *  
#  *   *   *   *  
#  *   *   *  
#  *   *
#  *


# row = 8


# for i in range(row,0,-1):
#     for j in range(i):
#         print(" * ",end=" ")
#     print()











# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 

# row = 5
# for i in range(row):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(i,row):
#         print("*",end=" ")
#     print()






#           * 
#         * *
#       * * *
#     * * * *
#   * * * * *

# row = 6
# for i in range(row,0,-1):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(i,row):
#         print("*",end=" ")
#     print()








#       * * * * * * * * * 
#       * *           * *
#       *   *       *   *
#       *     *   *     *
#       *       *       *
#       *     *   *     *
#       *   *       *   *
#       * *           * *
#       * * * * * * * * *


# n = 9
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or j==n-1 or i==n-1 or i==j or i+j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()










#                  * 
#                * * * 
#              * * * * *
#            * * * * * * *
#          * * * * * * * * *
#        * * * * * * * * * * *
#      * * * * * * * * * * * * *
#    * * * * * * * * * * * * * * *




# row = 8
# for i in range(row):
#     for j in range(row-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()










#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# n = 5

# for i in range(n):
#     print(" " * (n -i - 1) + "*" * (2 * i +1 ))

# for i in range(n - 2,-1,-1):
#     print(" " * (n - i - 1) + "*" * (2 * i +1 ))








# * * * * * 
# * * * * 
# * * *
# * *
# *
# * *
# * * *
# * * * *
# * * * * *

row = 5

for i in range(row, 0, -1):
    print("* " * i)

for i in range(2, row + 1):
    print("* " * i)