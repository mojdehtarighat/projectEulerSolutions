__author__ = 'mojdehtarighat'
"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?"""

def is_prime(x):
    n = 2
    if x<2:
        return False
    elif x==2:
        return True
    else:
        while n<=x-1:
            if x%n==0:
                return False
            else:
                n=n+1
    return True

def xth_prime(x):
    prime = 2
    count = 1
    iter = 3
    while count < x:
        if is_prime(iter):
            prime = iter
            count =count+ 1
        iter =iter+ 2
    return prime

print xth_prime(10001)
