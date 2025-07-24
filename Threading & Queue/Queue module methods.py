"""
====================== Python 'queue' Module Methods ======================

1. put(item) → Adds item, blocks if queue is full.
2. put_nowait(item) → Adds without blocking, raises queue.Full if full.
3. get() → Removes item, blocks if queue is empty.
4. get_nowait() → Removes without blocking, raises queue.Empty if empty.
5. qsize() → Returns current size.
6. empty() → Checks if queue is empty.
7. full() → Checks if queue is full.
8. task_done() → Used by consumer threads to signal that a task fetched with get() is done.
9. join() → Blocks until all items in the queue have been marked as done using task_done().
"""

# Complete Example with All Common Methods of queue module

import queue
import threading
import time

# Create a FIFO Queue with max size 2
q = queue.Queue(maxsize=2)

# Worker function for a consumer thread
def worker():
    while True:
        item = q.get()
        print(f"[Consumer] Processing item: {item}")
        time.sleep(1)  # Simulate work
        q.task_done()  # Mark the task as done

# Start a background consumer thread (daemon)
threading.Thread(target=worker, daemon=True).start()

print("Is queue empty?", q.empty())  # True

# Producer adds items
q.put(1)
print("[Producer] Added 1")
q.put(2)
print("[Producer] Added 2")

print("Queue size now:", q.qsize())  # 2

# Try to put another item using put_nowait() - should raise queue.Full
try:
    q.put_nowait(3)
except queue.Full:
    print("[Producer] Queue is full! Cannot add using put_nowait()")

# Wait a bit to let consumer process
time.sleep(3)

# Now there is space again
q.put_nowait(3)
print("[Producer] Added 3 with put_nowait()")

# Wait for all tasks to be marked done
print("Waiting for all tasks to complete...")
q.join()  # Blocks until all items have been processed and task_done() called
print("All tasks completed!")

print("Is queue empty now?", q.empty())  # Should be True
