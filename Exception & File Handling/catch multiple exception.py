
# Example: Handling Multiple Exceptions with List and Dictionary

data = [10, 20, 30]
info = {'name': 'Gaurav'}

try:
    # IndexError example
    print("Element:", data[3])
    # KeyError example
    print("Age:", info['age'])
except IndexError:
    print("Error: List index out of range.")
except KeyError:
    print("Error: Key not found in dictionary.")
except Exception as e:
    print("An unexpected error occurred:", e)

