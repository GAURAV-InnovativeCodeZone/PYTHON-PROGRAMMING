"""
============================================================
Event Class - Simple signaling, wait for an event to be set.
============================================================

Key Methods & Attributes:
- .wait(): Block until .set() is called.
- .set(): Set the event (all waiters continue).
- .clear(): Reset event to unset.
- .is_set(): True if event is set.

"""

import threading
import time

event = threading.Event()

def waiter():
    print("[Waiter] Waiting for event...")
    event.wait()  # Wait until event is set
    print("[Waiter] Event detected! Proceeding...")

def setter():
    print("[Setter] Doing work...")
    time.sleep(2)
    event.set()
    print("[Setter] Event is set.")

w = threading.Thread(target=waiter)
s = threading.Thread(target=setter)

w.start()
s.start()

w.join()
s.join()

print("✅ Event Example Done.")
