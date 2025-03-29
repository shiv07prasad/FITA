import threading

lock = threading.Lock()
counter = 0
def print_counter():
    #global counter
    # with lock:
    for i in range(20000000):
        
            counter += 1

    print(counter)

# Creating a thread
thread1 = threading.Thread(target=print_counter)
thread2 = threading.Thread(target=print_counter)
thread3 = threading.Thread(target=print_counter)
thread4 = threading.Thread(target=print_counter)



# Starting the thread
thread1.start()
thread2.start()
thread3.start()
thread4.start()


# Waiting for the thread to finish
thread1.join()
thread2.join()
thread3.join()
thread4.join()

# print(counter)


# import concurrent.futures
# import time

# def task(name):
#     print(f"Task {name} is starting")
#     time.sleep(3)
#     print(f"Task {name} is complete")

# # Using ThreadPoolExecutor
# with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
#     executor.map(task, range(5))


# import multiprocessing

# counter = 0
# def print_numbers():
#     global counter
#     for i in range(200000000):
#             counter += 1
#     print(counter)

# def main():
#     # Creating a process
#     process1 = multiprocessing.Process(target=print_numbers)
#     process2 = multiprocessing.Process(target=print_numbers)
#     process3 = multiprocessing.Process(target=print_numbers)
#     process4 = multiprocessing.Process(target=print_numbers)

#     # Starting the process
#     process1.start()
#     process2.start()
#     process3.start()
#     process4.start()


#     # Waiting for the process to finish
#     process1.join()
#     process2.join()
#     process3.join()
#     process4.join()


# if __name__ == "__main__":
#       main()