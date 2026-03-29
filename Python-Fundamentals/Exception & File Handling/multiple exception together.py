try:
    x = int(input("Enter a number: "))
    y = 10 / x                          # Perform division (may raise ZeroDivisionError if x is 0)
    print("Result is", y)

# catch multiple exceptions together
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")
    
# Executes if no exception occurs
else:
    print("No exceptions occurred.")
    
# Always executes, regardless of exceptions
finally:
    print("Execution completed.")
