


# import threading
# import time


# def task1():
#     for i in range(5):
#         print('Task 1')
#         time.sleep(1)


# def task2():
#     for i in range(5):
#         print('Task 2')
#         time.sleep(1)



# t1 = threading.Thread(target=task1)
# t2 = threading.Thread(target=task2)

# t1.start()
# t2.start()





'...................................'



# import threading
# import time


# def task():
#     for i in range(5):
#         print("Running...")
#         time.sleep(1)


# start_time = time.time()

# t1 = threading.Thread(target=task)
# t2 = threading.Thread(target=task)

# t1.start()
# t2.start()

# t1.join()
# t2.join()


# end_time = time.time()

# print("Execute time :", end_time - start_time, "seconds")







'...................................'


import threading

counter = 0

def increment():
    global counter
    for i in range(100000):
        counter += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print(counter)