count = int(input("Enter the count of terms you need in the Fibonacci series: "))
fibonacci_series = [0, 1]  # Initialize with the first two Fibonacci numbers

if count <= 0:
    print("Please enter a positive number.")
elif count == 1:
    print([0])  # Only the first Fibonacci number


else:
    for i in range(2, count):
        # Add the sum of the last two numbers in the series
        fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])
    print(fibonacci_series)

