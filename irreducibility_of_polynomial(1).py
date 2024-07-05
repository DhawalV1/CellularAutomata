from sympy import symbols, Poly, factorint, gcd, GF
import numpy

input_str = input("Enter the rules separated by spaces (keep it 90 or 150): ")
array = [int(num) for num in input_str.split()]
prime = int(input("Enter the Galois Field value,p: "))

def CharacteristicsPoly(rule_vec, field_value):

    def irreducibility_test(f, q):
        x = symbols('x')
        n = f.degree()
        
        # Find all distinct prime divisors of n
        prime_divisors = list(factorint(n).keys())
        
        for p in prime_divisors:
            n_j = n // p
            h = x**(q**n_j) - x
            h_mod_f = Poly(h, x, domain=f.domain).rem(f)
            g = gcd(f, h_mod_f)
            if g != 1:
                return "Poly is reducible"
        
        g = x**(q**n) - x
        g_mod_f = Poly(g, x, domain=f.domain).rem(f)
        if g_mod_f == 0:
            return "Poly is Irreducible"
        else:
            return "Poly is Reducible" 
        
    x = symbols('x')
    n = len(rule_vec)
    Fq = GF(field_value)
    
    # the coefficients d based on rule vector, 0 for 90 and 1 for 150
    rule_vec = [int((i - 90) / 60) for i in rule_vec]

    # Initialize the polynomial array with the first two polynomials
    p_array = [1, [ 1 , rule_vec[0]]]

    # Apply the recurrence relation to find the characteristic polynomial
    for i in range(2, n + 1):
        curr = numpy.polymul([1 , rule_vec[i - 1]],p_array[-1])
        p_array.append(numpy.polyadd(curr,p_array[-2]) % field_value)              # operations in GF(2)

    char_poly = Poly(p_array[-1],x,domain=Fq)
    print('The characteristic polynomial is', char_poly)

    print(irreducibility_test(char_poly,Fq.characteristic()))
    
CharacteristicsPoly(array,prime)

