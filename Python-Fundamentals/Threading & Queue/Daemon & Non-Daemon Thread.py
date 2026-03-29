"""
============================ Daemon vs Non-Daemon Threads ============================

▶ Non-daemon threads :
A non-daemon thread (the default type) is a regular thread. 
Python will not exit until all non-daemon threads have completed.
Keep the main program alive until they finish.
▶ Daemon threads :
A daemon thread runs in the background, performing tasks like monitoring, logging, or housekeeping.
It does not block the main program from exiting.
Killed automatically when the main thread exits.
How to set .daemon = True, check .isDaemon()
"""

import threading
import time

def daemon_task():
    while True:
        print("Daemon thread is running...")
        time.sleep(1)

def non_daemon_task():
    print("Non-daemon thread starting...")
    time.sleep(3)
    print("Non-daemon thread finished!")

# Daemon thread
daemon_thread = threading.Thread(target=daemon_task)
daemon_thread.daemon = True

# Non-daemon thread
non_daemon_thread = threading.Thread(target=non_daemon_task)
non_daemon_thread.daemon = False  # Default

daemon_thread.start()
non_daemon_thread.start()

# Main thread ends here but waits for non-daemon threads

