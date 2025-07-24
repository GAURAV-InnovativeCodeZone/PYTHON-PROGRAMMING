"""
▶ Thread Synchronization
==========================
Thread synchronization is used to prevent race condition & deadlock.
It means coordinating multiple threads so they safely access shared resources without conflicts or corruption.
It making sure shared data stays safe when many threads want to use it at the same time.

Synchronization Mechanisms -
1️⃣ Lock
2️⃣ RLock
3️⃣ Semaphore
4️⃣ BoundedSemaphore
5️⃣ Event
6️⃣ Condition
7️⃣ Barrier
8️⃣ Timer
"""

import threading

counter = 0
lock = threading.Lock()

def safe_increment():
    global counter
    for _ in range(100000):
        with lock:          # 🔒 Synchronization: only one thread at a time!
            counter += 1

threads = []
for _ in range(2):
    t = threading.Thread(target=safe_increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Counter with Lock: {counter} (Expected: 200000)")
