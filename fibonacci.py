def fibonacci(n):
    # Initialize the first two terms of the Fibonacci sequence: 0 and 1
    fib_sequence = [0, 1]

    # Loop to calculate subsequent Fibonacci numbers
    # The loop starts at 2 because the first two Fibonacci numbers (0, 1) are already in the list
    for i in range(2, n):
        # Calculate the next Fibonacci number as the sum of the last two numbers in the list
        next_term = fib_sequence[-1] + fib_sequence[-2]
        # The expression fib_sequence[-1] accesses the last element of the list fib_sequence.
        # In Python, negative indexing allows you to access elements from the end of a list.
        # So, [-1] refers to the most recent (last) Fibonacci number in the list.
        # Similarly, fib_sequence[-2] accesses the second-to-last element of the list. This is the Fibonacci number that came just before the last one.

        # Append the new Fibonacci number to the sequence
        fib_sequence.append(next_term)

    # Return the list containing the Fibonacci sequence up to the nth term
    return fib_sequence

# Print the Fibonacci sequence for n = 5; first 5
print(fibonacci(5))