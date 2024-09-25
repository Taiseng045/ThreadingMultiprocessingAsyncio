import multiprocessing

def is_prime(n):
  # pass
  if n <= 1:
      return False
  for i in range(2, int(n**0.5) + 1):
      if n % i == 0:
        return False
  return True

def check_prime_chunk(numbers):
  # pass
  primes=[]
  for n in numbers:
        if is_prime(n):
            primes.append(n)
  return primes

def find_primes_in_range(numbers, chunk_size):
  # pass
  chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
    
    # Create a multiprocessing pool with the number of CPU cores
  with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
    # Apply the check_prime_chunk function to each chunk in parallel
    result = pool.map(check_prime_chunk, chunks)
    
    # Flatten the result, since pool.map returns a list of lists
  primes = [prime for Primelist in result for prime in Primelist]
  return primes
