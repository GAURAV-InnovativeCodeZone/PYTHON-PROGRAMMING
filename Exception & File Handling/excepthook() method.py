# sys.excepthook() Method Example
# sys.excepthook is a function in the sys module that handles uncaught exceptions.
# You can override it to customize how uncaught exceptions are displayed.

import sys
import traceback
def custom_excepthook(exc_type, exc_value, exc_traceback):
    print("Custom Exception Handler:")
    print(f"Type: {exc_type.__name__}")
    print(f"Value: {exc_value}")
    print(f"traceback")
    traceback.print_tb(exc_traceback)

# Set the custom excepthook
sys.excepthook = custom_excepthook

# Example: This will trigger the custom excepthook because the exception is uncaught
raise RuntimeError("This is an uncaught exception!")
