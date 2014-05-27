__author__ = 'mojdehtarighat'
"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

"""20 is a small enough number that originally, I was able to write out the correct prime factorization 2*2*2*2*3*3*5*7*11*13*17*19 of the desired number in about a minute.
However, I wrote this code afterwards and got the same result."""

def gcd(a,b):
    if a==b:
        return a
    elif a<b:
        for check in range(a,0,-1):
            if b%check==0 and a%check==0:
                return check
    else:
        for check in range(b,0,-1):
            if a%check==0 and b%check==0:
                return check

def lcm(a,b):
    return a*b/gcd(a,b)

n=1
for i in range(1,21):
    n=lcm(n,i)

print n