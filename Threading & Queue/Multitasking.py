"""
▶ Multitasking : 
Multitasking allows multiple tasks to run concurrently, improving efficiency,
especially for I/O-bound or CPU-bound operations.

Types of multitasking in Python:
  1. Process-based multitasking using the multiprocessing module.
       Uses separate processes to run tasks concurrently. Suitable for CPU-bound tasks.
  2. Thread-based multitasking using the threading module.
       Uses threads within a single process to run tasks concurrently. Suitable for I/O-bound tasks.
"""

import threading
import multiprocessing
import time

# Process-based multitasking example
def process_task(name: str) -> None:
    for i in range(3):
        print(f"Process {name} - iteration {i+1}")
        time.sleep(1)

# Thread-based multitasking example
def thread_task(name: str) -> None:
    for i in range(3):
        print(f"Thread {name} - iteration {i+1}")
        time.sleep(1)

if __name__ == "__main__":
    print("Starting process-based multitasking:")
    process1 = multiprocessing.Process(target=process_task, args=("A",))
    process2 = multiprocessing.Process(target=process_task, args=("B",))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("\nStarting thread-based multitasking:")
    thread1 = threading.Thread(target=thread_task, args=("X",))
    thread2 = threading.Thread(target=thread_task, args=("Y",))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("\nAll multitasking tasks completed.")
