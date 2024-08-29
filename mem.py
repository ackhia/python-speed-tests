import random
import time

def generate_large_list(size):
    """Generate a large list of random integers."""
    return [random.randint(0, size) for _ in range(size)]

def perform_operations(data):
    """Perform various memory-intensive operations on the list."""
    # Sort the list
    sorted_data = sorted(data)
    
    # Reverse the list
    reversed_data = sorted_data[::-1]
    
    # Find the maximum and minimum
    max_val = max(reversed_data)
    min_val = min(reversed_data)
    
    # Sum all the elements
    total_sum = sum(reversed_data)
    
    return max_val, min_val, total_sum

def run_memory_test(size):
    """Run the memory-intensive test and measure the time taken."""
    start_time = time.perf_counter()
    
    # Generate a large list
    large_list = generate_large_list(size)
    
    # Perform memory-intensive operations
    max_val, min_val, total_sum = perform_operations(large_list)
    
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    
    print(f"Processed a list of {size} elements in {elapsed_time:.2f} seconds.")
    print(f"Max: {max_val}, Min: {min_val}, Sum: {total_sum}")

if __name__ == "__main__":
    run_memory_test(10**7)  # 10 million elements
