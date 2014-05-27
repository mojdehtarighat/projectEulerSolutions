__author__ = 'mojdehtarighat'
"""A palindromic number reads the same both ways.

The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

def is_pal_product(num_1, num_2):
    num_3=num_1*num_2
    num_3=str(num_3)
    x=0
    while x!=len(num_3)+1:
        if num_3[x]==num_3[len(num_3)-x-1] and x!=len(num_3)-1:
            x=x+1
        elif num_3[x]!=num_3[len(num_3)-x-1]:
            return False
        else:
            return num_3

pal_list=[]

for num_1 in range(999,0,-1):
    for num_2 in range(999,0,-1):
        if is_pal_product(num_1,num_2):
            pal_list.append(int(is_pal_product(num_1,num_2)))

print max(pal_list)