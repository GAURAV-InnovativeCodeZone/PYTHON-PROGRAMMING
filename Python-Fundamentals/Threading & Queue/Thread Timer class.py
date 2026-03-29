"""
========================================================================================
Timer Class - Delayed Execution, Run a function later, after a delay, in its own thread.
=========================================================================================

Key Methods & Attributes:
- .start(): Start countdown.
- .cancel(): Cancel timer if not fired yet.
- .is_alive(): Check if the timer thread is still running.

"""

import threading
import time

def say_hello():
    print("[Timer] Hello! Fired after delay.")

timer = threading.Timer(3.0, say_hello)

print("[Timer] Starting 3-second timer...")
timer.start()

print(f"[Timer] Timer alive? {timer.is_alive()}")

time.sleep(1)
print(f"[Timer] Timer alive after 1 sec? {timer.is_alive()}")

# Cancel example: Uncomment below to cancel
# timer.cancel()
# print("[Timer] Timer canceled!")

time.sleep(4)  # Wait to see if timer fires

print(f"[Timer] Timer alive after done? {timer.is_alive()}")
print("✅ Timer Example Done.")
