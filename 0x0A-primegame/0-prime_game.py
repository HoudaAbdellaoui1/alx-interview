#!/usr/bin/python3
"""Determines the winner of the game played between Maria and Ben."""


def isWinner(x, nums):
    """
    Determines the winner of the game played between Maria and Ben.
    :param x: Number of rounds
    :param nums: List of integers representing the upper limit for each round
    :return: Name of the player with the most wins or None if it's a tie
    """
    def sieve(n):
        """
        Uses the Sieve of Eratosthenes to determine prime numbers up to n.
        :param n: The upper limit
        :return: List where index is True if the number is prime,
        False otherwise
        """
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not primes
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for multiple in range(i * i, n + 1, i):
                    primes[multiple] = False
        return primes

    if x < 1 or not nums:
        return None

    max_n = max(nums)
    primes = sieve(max_n)
    prime_count = [0] * (max_n + 1)

    # Precompute the cumulative count of primes up to each number
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Number of primes determines the number of valid moves
        if prime_count[n] % 2 == 1:
            maria_wins += 1  # Maria wins if the number of moves is odd
        else:
            ben_wins += 1  # Ben wins if the number of moves is even

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
