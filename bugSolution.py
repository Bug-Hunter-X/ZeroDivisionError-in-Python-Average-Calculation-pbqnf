def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list gracefully
    return sum(numbers) / len(numbers)

# Example usage that handles the empty list case:
average1 = calculate_average([1, 2, 3, 4, 5])
average2 = calculate_average([]) #this will return 0
print(average1) # Output: 3.0
print(average2) # Output: 0