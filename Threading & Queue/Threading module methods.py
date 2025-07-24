'''
==========================================================
Python Threading Module - Complete Example with Methods
==========================================================
'''

import threading
import time

# Shared resource
counter = 0

# Lock for synchronization to prevent race conditions
lock = threading.Lock()

def worker(name, loops):
    """
    Worker function that increments a shared counter safely.
    Shows usage of current_thread(), get_ident(), get_native_id().
    """
    global counter

    print(f"Started: {threading.current_thread().name}")  # current_thread()
    print(f"Thread ident: {threading.get_ident()}")       # get_ident()
    print(f"Native ID: {threading.get_native_id()}")      # get_native_id()

    for _ in range(loops):
        with lock:  # Synchronization using Lock
            counter += 1
            time.sleep(0.1)  # Simulate work

    print(f"Finished: {name}")

# Create a NON-daemon thread (default)
t1 = threading.Thread(target=worker, name="NonDaemonWorker", args=("Worker-1", 5))

# Create a DAEMON thread (background)
t2 = threading.Thread(target=worker, name="DaemonWorker", args=("Worker-2", 5))
t2.daemon = True  # Modern way to mark as daemon

# Show daemon status (modern way)
print(f"Is t1 daemon? {t1.daemon}")
print(f"Is t2 daemon? {t2.daemon}")

# Start threads
t1.start()
t2.start()

# Show active thread count
print("Active thread count:", threading.active_count())

# List all running threads
print("All active threads:")
for t in threading.enumerate():
    print(f"- {t.name}")

# Show the main thread
print("Main thread:", threading.main_thread().name)

# Wait for non-daemon thread to finish (the program won't exit until this is done)
t1.join()

# Check if threads are alive
print(f"Is t1 alive? {t1.is_alive()}")
print(f"Is t2 alive? {t2.is_alive()}")  # Might still be alive if main hasn't exited yet

# Show final counter value
print("Final counter value:", counter)

print("Main thread exiting...")
