import concurrent.futures
import time

def task(name):
    print(f"Task {name} is starting")
    time.sleep(3)
    print(f"Task {name} is complete")

# Using ThreadPoolExecutor
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(task, range(5))
