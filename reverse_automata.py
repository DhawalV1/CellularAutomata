import numpy
from sympy import Poly, symbols, GF

def test1(rule_vec):

    def test(rule_vec1):

        x = symbols('x')
        
        rule_vec = [int(i) for i in rule_vec1]

        n = len(rule_vec)

        # Initialize the polynomial array with the first two polynomials
        p_array = [1, [ 1 , rule_vec[0]]]

        # Apply the recurrence relation to find the characteristic polynomial
        for i in range(2, n + 1):
            curr = numpy.polymul([1 , rule_vec[i - 1]],p_array[-1])
            p_array.append(numpy.polyadd(curr,p_array[-2]) % 2)              # operations in GF(2)

        return Poly(p_array[-1],x)
    
    
        
    return test(rule_vec)==test(rule_vec[::-1])

n = 3      # checked for all the cellular automata of length 1 to 17

for k in range(1,n):

    rules_vectors = [bin(i)[2:].zfill(k) for i in range(2**k) if bin(i)[2:].zfill(k) != bin(i)[2:].zfill(k)[::-1]]   # generate all the cellular automata

    for i in rules_vectors:
        if test1(i)==False:
            print('failed')

# As we see, no 'failed' is printed, thus the hypothesis is true

# the runtime of this code is 4 minutes
