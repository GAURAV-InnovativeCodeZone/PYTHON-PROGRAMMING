"""
=================================================================================================
Barrier Class - Synchronize Threads, Wait until all threads reach a point, then proceed together.
=================================================================================================

Key Methods & Attributes:
- .wait(): Wait at the barrier until all parties arrive.
- .parties: Total number of threads to wait for.
- .n_waiting: How many threads are currently waiting.
- .reset(): Reset the barrier.
- .abort(): Abort barrier if broken.

"""

import threading
import time

barrier = threading.Barrier(3)

def worker(n):
    print(f"[Worker-{n}] Working...")
    time.sleep(n)
    print(f"[Worker-{n}] Waiting at barrier. Waiting count: {barrier.n_waiting}")
    barrier.wait()
    print(f"[Worker-{n}] Passed barrier together!")

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("✅ Barrier Example Done.")
