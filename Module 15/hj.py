import threading
import time

counter = 0

def increment_counter():
    global counter
    for _ in range(40000000):
        # Explicitly break the increment operation into steps
        # to make the race condition more obvious
        local_value = counter
        # Slight pause to encourage thread switching
        
        counter = local_value + 1

# Create four threads
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)
thread3 = threading.Thread(target=increment_counter)
thread4 = threading.Thread(target=increment_counter)

print("Starting threads...")

# Start the threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()

# Wait for all threads to finish
thread1.join()
thread2.join()
thread3.join()
thread4.join()

print(f"Final counter value: {counter}")
print(f"Expected counter value: {4 * 100000}")
print(f"Missing increments: {(4 * 100000) - counter}")