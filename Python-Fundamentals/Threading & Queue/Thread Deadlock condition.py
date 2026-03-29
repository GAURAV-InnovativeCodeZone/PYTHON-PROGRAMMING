"""
=====================================
Python Threading - Deadlock Example
=====================================

▶ Deadlock → multiple threads wait for each other's locks forever → program freeze.
- How deadlock happens when threads acquire locks in different orders.
- Both threads wait forever for each other to release a lock.
- Why consistent locking order matters.
"""

import threading
import time

# Two locks
lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1_task():
    """
    Thread 1 acquires lock1, then tries to acquire lock2.
    """
    print("[Thread-1] Acquiring lock1...")
    lock1.acquire()
    print("[Thread-1] Acquired lock1")
    time.sleep(1)

    print("[Thread-1] Trying to acquire lock2...")
    lock2.acquire()
    print("[Thread-1] Acquired lock2")

    lock2.release()
    lock1.release()
    print("[Thread-1] Released both locks")

def thread2_task():
    """
    Thread 2 acquires lock2 first, then tries to acquire lock1.
    This creates potential for deadlock if Thread-1 holds lock1.
    """
    print("[Thread-2] Acquiring lock2...")
    lock2.acquire()
    print("[Thread-2] Acquired lock2")
    time.sleep(1)

    print("[Thread-2] Trying to acquire lock1...")
    lock1.acquire()
    print("[Thread-2] Acquired lock1")

    lock1.release()
    lock2.release()
    print("[Thread-2] Released both locks")

# Start both threads
t1 = threading.Thread(target=thread1_task)
t2 = threading.Thread(target=thread2_task)

t1.start()
t2.start()

# Wait for threads (with timeout to avoid hanging forever)
t1.join(timeout=5)
t2.join(timeout=5)

print("[Deadlock Example] If program hangs or partial output, deadlock occurred.")
