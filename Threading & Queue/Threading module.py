'''
▶ threading module:
Threading in Python allows multiple threads to run concurrently within a single process, enabling efficient multitasking especially for I/O-bound tasks.
Threads share the same memory space, which makes communication between them easier.
'''

import threading
import time

def thread_task(name: str) -> None:
    for i in range(3):
        print(f"Thread {name} - iteration {i+1}")
        time.sleep(1)

if __name__ == "__main__":
    print("Starting thread-based multitasking:")
    thread1 = threading.Thread(target=thread_task, args=("X",))
    thread2 = threading.Thread(target=thread_task, args=("Y",))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("All threading tasks completed.")
