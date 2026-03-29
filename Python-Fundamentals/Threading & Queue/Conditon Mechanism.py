"""
=========================================================================
Condition Class - Advanced wait/notify for producer-consumer style tasks.
=========================================================================

Key Methods:
- .wait(): Thread waits until notified.
- .notify(): Wake one waiting thread.
- .notify_all(): Wake all waiting threads.
- .acquire() & .release(): Use with `with` for auto acquire/release.

"""

import threading
import time

condition = threading.Condition()
queue = []

def producer():
    with condition:
        print("[Producer] Producing item...")
        queue.append("🍔")
        time.sleep(1)
        condition.notify()  # Notify one waiting consumer
        print("[Producer] Notified consumer.")

def consumer():
    with condition:
        print("[Consumer] Waiting for item...")
        while not queue:
            condition.wait()  # Wait for producer to notify
        item = queue.pop()
        print(f"[Consumer] Got item: {item}")

c = threading.Thread(target=consumer)
p = threading.Thread(target=producer)

c.start()
time.sleep(0.5)  # Ensure consumer waits first
p.start()

c.join()
p.join()

print("✅ Condition Example Done.")
