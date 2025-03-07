class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # if right < 2:
        #     return [-1, -1]
    
        # limit = int(right ** 0.5) + 1
        # is_prime_small = [True] * (limit + 1)
        # is_prime_small[0] = is_prime_small[1] = False
    
        # for num in range(2, limit + 1):
        #     if is_prime_small[num]:
        #         for multiple in range(num * num, limit + 1, num):
        #             is_prime_small[multiple] = False
    
        # small_primes = [num for num in range(2, limit + 1) if is_prime_small[num]]
    
        # is_prime = [True] * (right - left + 1)
        # if left == 1:
        #     is_prime[0] = False
    
        # for prime in small_primes:
        #     start = max(prime * prime, left + (prime - left % prime) % prime)
        #     for multiple in range(start, right + 1, prime):
        #         is_prime[multiple - left] = False
    
        # primes = [num for num in range(left, right + 1) if is_prime[num - left]]
    
        # if len(primes) < 2:
        #     return [-1, -1]
    
        # min_gap = float('inf')
        # result = [-1, -1]
    
        # for i in range(len(primes) - 1):
        #     gap = primes[i + 1] - primes[i]
        #     if gap < min_gap:
        #         min_gap = gap
        #         result = [primes[i], primes[i + 1]]
    
        # return result
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
    
        for num in range(2, int(right ** 0.5) + 1):
            if is_prime[num]:
                
                for multiple in range(num * num, right + 1, num):
                    is_prime[multiple] = False
    
    # Collect primes in the given range
        primes = [num for num in range(left, right + 1) if is_prime[num]]
    
    # If there are less than two primes, return [-1, -1]
        if len(primes) < 2:
            return [-1, -1]
    
    # Find the closest pair
        min_gap = float('inf')
        result = [-1, -1]
    
        for i in range(len(primes) - 1):
            gap = primes[i + 1] - primes[i]

            if gap < min_gap:
                min_gap = gap

                result = [primes[i], primes[i + 1]]
    
        return result