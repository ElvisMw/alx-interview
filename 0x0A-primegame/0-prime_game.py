#!/usr/bin/python3
"""Module that contains functions to generate primes using
the Sieve of Eratosthenes and to determine the winner of a
game between Maria and Ben based on the number
of prime numbers up to a given number.
"""


def sieve(n):
    """Generate list of primes up to n using the Sieve of Eratosthenes.

    Args:
        n (int): The upper limit for the prime numbers.

    Returns:
        list: A list of prime numbers up to n.
    """
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if is_prime[p]:
            """ For each prime number, mark its multiples as not prime """
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    """ Return the list of primes """
    return [p for p in range(2, n + 1) if is_prime[p]]


def isWinner(x, nums):
    """Determine the winner of a game between Maria and Ben based on the number
    of prime numbers up to a given number.

    Args:
        x (int): The upper limit for the prime numbers.
        nums (list): A list of numbers.

    Returns:
        str: The name of the winner ("Maria" or "Ben"), or
        None if the game is a tie.
    """

    if not nums or x < 1:
        return None

    """ Find the maximum number in the input """
    max_num = max(nums)
    """ Generate a list of primes up to the maximum number """
    primes = sieve(max_num)

    def count_primes_up_to(n):
        """Count the number of prime numbers up to a given number.

        Args:
            n (int): The upper limit for the prime numbers.

        Returns:
            int: The number of prime numbers up to n.
        """
        count = 0
        for prime in primes:
            if prime <= n:
                count += 1
            else:
                break
        return count

    """ Count the number of wins for Maria and Ben """
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        prime_count = count_primes_up_to(n)
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    """ Determine the winner """
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
