#!/usr/bin/python3
"""
prime game 
"""
def is_prime(num):
    """ Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def optimal_move(nums):
    """ Find the optimal move for a player."""
    for i in range(len(nums)):
        if is_prime(nums[i]):
            return nums[i]

def isWinner(x, nums):
    """ Determine the winner of the game."""
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        primes_remaining = sum(1 for num in range(1, n + 1) if is_prime(num))
        if primes_remaining % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
