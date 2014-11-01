# Program to compute primes
#
# usage:
# python primes.py <N>
#
# input:
# N: compute all primes up to N
#
# output:
# list containing all primes up to N
#
# By Anthony Baca 


import sys

N = int(sys.argv[1])

nums = range(2,N) #numbers we're going to test
for i in range(2, N):
    nums = filter(lambda x: x==i or x % i, nums) #filter out those that are divisble

print nums