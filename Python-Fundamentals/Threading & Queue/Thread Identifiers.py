"""
============================ Thread & Native Identifiers ============================

assign custom names, and print their `ident` (Python internal ID)
and `native_id` (OS-level thread ID, available in Python 3.8+).
"""

import threading
import time

# Function that the thread will run
def worker():
    current_thread = threading.current_thread()  # Get current thread object
    print(f"[{current_thread.name}] ident: {current_thread.ident}, native_id: {current_thread.native_id}")
    for i in range(3):
        print(f"[{current_thread.name}] Working... {i}")
        time.sleep(1)

if __name__ == "__main__":
    # Create two threads with custom names
    t1 = threading.Thread(target=worker, name="Worker-1")
    t2 = threading.Thread(target=worker, name="Worker-2")

    # Start threads
    t1.start()
    t2.start()

    # Print main thread info
    main_thread = threading.current_thread()
    print(f"[{main_thread.name}] ident: {main_thread.ident}, native_id: {main_thread.native_id}")

    # Wait for both threads to finish
    t1.join()
    t2.join()

    print("✅ All threads have finished execution.")
