"""
===========================================
Python Threading - Race Condition Example
===========================================

▶ Race Condition → multiple threads write shared data unsafely → data corruption.
- What a race condition is.
- How multiple threads modify shared data unsafely.
- How the final result is unpredictable without synchronization.
"""

import threading

# Shared resource
counter = 0

def unsafe_increment():
    """
    Increment a shared counter without using a Lock.
    Causes race condition when multiple threads run this.
    """
    global counter
    for _ in range(100000):
        counter += 1  # Not atomic, not safe!

# Create threads
threads = []
for i in range(2):  # Two threads incrementing at the same time
    t = threading.Thread(target=unsafe_increment)
    threads.append(t)
    t.start()

# Wait for both threads to finish
for t in threads:
    t.join()

# Expected: 200000 (100000 * 2)
# Actual: Likely less due to race condition
print(f"[Race Condition] Expected: 200000, Actual: {counter}")

