import multiprocessing

counter = 0


def increment():
    global counter
    for _ in range(20000000):
        # Ensures only one thread modifies counter at a time
            counter += 1


    print(counter)




if __name__ =="__main__":
    increment()

    # Create two threads
    thread1 = multiprocessing.Process(target=increment)
    thread2 = multiprocessing.Process(target=increment)
    thread3 = multiprocessing.Process(target=increment)

    # Start the threads
    thread1.start()
    thread2.start()
    thread3.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()
    thread3.join()

    print(f"Final counter value: {counter}")

