'''
Real-World Example: Retry with Exception Handling
In this example, we'll create a simple function that attempts to connect to a database.
If the connection fails, it will retry up to 3 times with a 2-second delay between attempts.
'''

import time

for attempt in range(3):
    try:
        # risky operation
        1 / 0
    except ZeroDivisionError:
        print("Failed, retrying...")
        time.sleep(1)
    else:
        break
else:
    print("All retries failed.")
    