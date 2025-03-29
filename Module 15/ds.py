import threading

counter = 0  # Shared variable (no lock)

def print_counter():
    global counter
    temp = counter  # Read the value (simulating more race conditions)
    for _ in range(20000000):
        temp += 1  # Modify a local copy before writing back
    counter = temp  # Write back (this introduces more inconsistency)

# Creating multiple threads
threads = [threading.Thread(target=print_counter) for _ in range(4)]

# Starting threads
for thread in threads:
    thread.start()

# Waiting for threads to finish
for thread in threads:
    thread.join()

print("Final counter value:", counter)

