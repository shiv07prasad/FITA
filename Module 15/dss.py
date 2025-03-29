import threading
import time

counter = 0
lock = threading.Lock()
def print_counter():
    global counter
    with lock:
        for _ in range(2000000):
            temp = counter
            # Force context switch
            counter = temp + 1
        print(counter)

# Create threads
thread1 = threading.Thread(target=print_counter)
thread2 = threading.Thread(target=print_counter)
thread3 = threading.Thread(target=print_counter)

# Start threads
thread1.start()
thread2.start()
thread3.start()

# Wait for completion
thread1.join()
thread2.join()
thread3.join()

print(f"final : {counter}")