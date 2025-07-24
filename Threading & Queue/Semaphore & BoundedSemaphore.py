"""
=====================================================================
Semaphore vs BoundedSemaphore Synchronization Mechanisms in Threading
=====================================================================
1️⃣ Semaphore → Limit how many threads can access a resource at once.
2️⃣ BoundedSemaphore → Same as Semaphore, but raises an error if you over-release (programming safety).
"""

import threading
import time

print("\n================= Semaphore Example =================")

# Semaphore: allows up to 2 threads in the critical section at the same time
semaphore = threading.Semaphore(2)

def sem_worker(i):
    print(f"[Semaphore] Thread-{i} waiting...")
    semaphore.acquire()
    print(f"[Semaphore] Thread-{i} inside critical section.")
    time.sleep(2)
    print(f"[Semaphore] Thread-{i} releasing.")
    semaphore.release()

# Start 4 threads → only 2 can run in critical section at once
for i in range(4):
    threading.Thread(target=sem_worker, args=(i,)).start()

time.sleep(5)

# ------------------------------------------------------------

print("\n================= BoundedSemaphore Example =================")

# BoundedSemaphore: same behavior, but checks over-release
bounded_semaphore = threading.BoundedSemaphore(2)

def bounded_worker(i):
    print(f"[BoundedSemaphore] Thread-{i} waiting...")
    bounded_semaphore.acquire()
    print(f"[BoundedSemaphore] Thread-{i} inside critical section.")
    time.sleep(1)
    print(f"[BoundedSemaphore] Thread-{i} releasing.")
    bounded_semaphore.release()

# Normal correct usage
for i in range(2):
    threading.Thread(target=bounded_worker, args=(i,)).start()

time.sleep(2)

# Intentionally cause an error by releasing more than acquired
print("\n[BoundedSemaphore] Trying to release too many times...")

try:
    bounded_semaphore.release()  # ❌ This should fail: nothing was acquired for this release
except ValueError as e:
    print(f"[BoundedSemaphore] Error caught: {e}")

print("\n✅ Combined Semaphore & BoundedSemaphore example done.")
