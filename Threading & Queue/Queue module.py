"""
============================ Queue Module ============================

It handles synchronization automatically, so you don't have to manage locks yourself.
The queue module provides multi-producer, multi-consumer FIFO queues for safe inter-thread communication.
It handles thread-safe operations, so multiple threads can add or remove items safely.

It supports different queue types:
FIFO Queue (Queue)
LIFO Queue (LifoQueue)
Priority Queue (PriorityQueue)
Simple Queue (SimpleQueue — simpler, unbounded, Python 3.7+)
"""

# Example : Used with Threads

import threading
import queue
import time

q = queue.Queue()

def producer():
    for i in range(5):
        print(f"Producing {i}")
        q.put(i)
        time.sleep(1)

def consumer():
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consuming {item}")
        q.task_done()

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

t1.join()
q.put(None)  # Signal consumer to exit
t2.join()
