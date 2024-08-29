
import time

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_primes(limit):
    """Count the number of prime numbers up to a given limit."""
    count = 0
    for i in range(2, limit):
        if is_prime(i):
            count += 1
    return count

def run_test(limit):
    """Run the prime counting test and measure the time taken."""
    start_time = time.perf_counter()
    prime_count = count_primes(limit)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Found {prime_count} primes up to {limit} in {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    run_test(3_000_000)

