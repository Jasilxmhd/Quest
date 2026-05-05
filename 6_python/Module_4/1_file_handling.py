'File operation'

'read'
# f = open("sample.txt")
# print(f.read())
# f.close()

'write'
# f = open("sample.txt",'r+')
# print(f.read())
# f.write("\n Muhammed Jasil")
# f.close()







# jasil = open("test.py",'r+')
# print(jasil.read())
# jasil.write("\nprint(add(40,10))")
# jasil.close()



'-------------------------------------------------'



'Read'

# with open("sample.txt")as f :
#     print(f.read())



'write'

# with open("sample.txt",'w')as f :
#     # print(f.read())
#     f.write("\nHilite calicut")
#     f.write("\npython")


# with open("sample.txt",'w')as f :
#     # print(f.read())
#     print(f.write("\ncalicut"))



'write il ilaatha file name adichaal new file create aavum'

# with open("one.txt",'w') as newfile:
#     pass
    



# with open("sample.txt","r+") as f2:

#     # read
#     # data = f2.read()
#     # print(data)

#     # write
#     # f2.write(" Amazon")
#     # f2.seek(0)
#     # f2.read()
#     f2.seek(0)
#     f2.write("jasil")







# with open("sample.txt","a+")as f:
#     print(f.tell())
#     f.seek(0)
#     data = f.readlines()
#     print(data)

# data[0]= "kabeer"
# print(data)

# with open("write_sample.txt","w+")as file:
#     file.writelines(data)









'append ( a )'
# Last ileek append aavum

# with open("sample.txt",'a') as f :
#     f.write("\njasil Parakkottu Valathu")









# with open("sample.txt",'a') as f :
#     f.write("\njasil Parakkottu Valathu")
#     f.write("\nAdivaram")
#     f.write("\nKaithapoyil")
#     f.write("\nPuthuppadi")
#     f.write("\nEngapuzha")
#     f.write("\nThamarassery")
#     f.write("\nKoduvallu")





'r +   ( Read + Write )'

# with open('sample.txt','r+')as f :
#     print(f.read())
#     f.write("\nPadanilam")
    






'w +   ( write + Read )'
with open('sample.txt','w+')as f:
    f.write('\nBattery')  
