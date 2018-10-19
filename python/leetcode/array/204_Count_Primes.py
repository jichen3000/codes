class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # from math import sqrt
        if n <= 2: return 0
        primes = []
        def check(num, limit):
            # s = int(sqrt(num))
            for j in primes:
                if num % j == 0:
                    return False
                if j > limit:
                    break
            return True
        limit = 2
        for i in range(3, n, 2):
            if limit ** 2 < i:
                limit += 1
            if check(i, limit):
                primes += i,
        return 1 + len(primes)
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [1] * n
        primes[0] = primes[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [0] * len(primes[i * i: n: i])
        return sum(primes)    
        