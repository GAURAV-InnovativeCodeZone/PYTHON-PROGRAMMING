from multiprocessing import Process
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {letter}")
        time.sleep(1)

if __name__ == "__main__":
    # Create processes
    p1 = Process(target=print_numbers)
    p2 = Process(target=print_letters)

    # Start processes
    p1.start()
    p2.start()

    # Wait for both to finish
    p1.join()
    p2.join()

    print("Done with process-based multitasking!")
