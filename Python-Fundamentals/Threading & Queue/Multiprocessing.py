"""
▶ Multiprocessing :
Multiprocessing is a way to run multiple processes in parallel, so your program can use multiple CPU cores at the same time.
It great for CPU-bound tasks like data crunching or image processing.
Key point - Unlike threads, each process has its own memory space and Python interpreter, avoiding the GIL limit in CPython.
"""

# Example - Safe Counter Increment

import multiprocessing
import time

def worker(counter, lock):
    for _ in range(100000):
        with lock:  # Lock to avoid race condition between processes
            counter.value += 1

if __name__ == "__main__":
    # Shared integer (Value) between processes
    counter = multiprocessing.Value('i', 0)  # 'i' = signed int
    lock = multiprocessing.Lock()

    # Create two processes
    p1 = multiprocessing.Process(target=worker, args=(counter, lock))
    p2 = multiprocessing.Process(target=worker, args=(counter, lock))

    p1.start()
    p2.start()

    print(f"[Main] Process 1 alive? {p1.is_alive()}")
    print(f"[Main] Process 2 alive? {p2.is_alive()}")

    p1.join()
    p2.join()

    print(f"[Main] Process 1 alive after join? {p1.is_alive()}")
    print(f"[Main] Process 2 alive after join? {p2.is_alive()}")

    print(f"✅ Final Counter Value: {counter.value} (Expected: 200000)")
