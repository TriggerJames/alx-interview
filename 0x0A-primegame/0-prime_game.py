#!/usr/bin/python3
"""Prime Game"""


def sieve_of_eratosthenes(n):
    """Helper function to generate primes up to n using Sieve of Eratosthenes"""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    primes = [i for i in range(2, n + 1) if sieve[i]]
    return primes


def isWinner(x, nums):
    """
    Determines the winner of the prime game after x rounds.
    Maria and Ben take turns picking primes.
    Maria starts first in every round.
    """
    if x < 1 or not nums:
        return None

    # Precompute primes up to the largest number in nums using sieve of Eratosthenes
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    
    # Track the number of wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Play each round
    for n in nums:
        primes_in_game = [p for p in primes if p <= n]
        moves = 0

        while primes_in_game:
            # Maria starts, removes a prime and all its multiples
            prime = primes_in_game.pop(0)
            primes_in_game = [p for p in primes_in_game if p % prime != 0]
            moves += 1
        
        # If the number of moves is odd, Maria wins (she made the last move)
        if moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
