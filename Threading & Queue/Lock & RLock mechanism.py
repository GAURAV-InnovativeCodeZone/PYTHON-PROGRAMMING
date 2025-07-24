"""
=====================================================
Lock vs RLock Synchronization Mechanisms in Threading
======================================================

1️⃣ Lock → Simple mutual exclusion for shared data.
           It has two methods--- 1.acquire()-locked stage, 2.release()-unlocked  stage
2️⃣ RLock → Needed when the **same thread** must acquire the same lock multiple times (nested).
"""

import threading
import time

print("\n================= Lock Example =================")

# Shared resource
counter = 0
lock = threading.Lock()

def increment_with_lock():
    global counter
    for _ in range(100000):
        with lock:  # Normal Lock is fine here
            counter += 1

threads = []
for _ in range(2):
    t = threading.Thread(target=increment_with_lock)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"[Lock] Counter: {counter} (Expected: 200000)")

# ----------------------------------------------------

print("\n================= RLock Example =================")

# RLock lets the **same thread** acquire it multiple times.
rlock = threading.RLock()

def nested_task(level):
    with rlock:
        print(f"[RLock] Enter level {level}")
        if level > 0:
            nested_task(level - 1)
        print(f"[RLock] Exit level {level}")

# Run nested task in a thread
t = threading.Thread(target=nested_task, args=(3,))
t.start()
t.join()

print("\n✅ Example done.")
