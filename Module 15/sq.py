import threading
import time

counter = 0
iterations = 20000

def increment():
    global counter
    for _ in range(iterations):
        # Introduce temporary variable to split the operation
        temp = counter
        # Simulate thread-switching delay
        time.sleep(0.001)  # Force context switch
        temp += 1
        counter = temp

threads = []
for _ in range(3):
    thread = threading.Thread(target=increment)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Expected: {5 * iterations}, Actual: {counter}")