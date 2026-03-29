"""
▶ Thread-Based Multitasking: (Need threading module)
Thread-based multitasking means multiple threads within the same process perform different tasks simultaneously.
Threads share the same memory space and resources of the parent process, so context switching between threads is faster.

Use Case:
Useful when tasks are lightweight and share data — for example, a web server handling multiple requests at once.
"""

import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {letter}")
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start threads
t1.start()
t2.start()

# Wait for both to finish
t1.join()
t2.join()

print("Done with thread-based multitasking!")
