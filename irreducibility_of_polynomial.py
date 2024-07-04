from sympy import symbols, gcd, Poly, GF  # import mod,div if needed
from sympy.ntheory.factor_ import factorint


x = symbols('x')

# Input field characteristic
field_value = int(input("Enter the characteristic of the finite field (e.g., 5 for F_5): "))
Fq = GF(field_value)

# Input the number of terms
num_terms = int(input("Enter the number of terms in the polynomial: "))

# Input coefficients and degrees
terms = []
for i in range(num_terms):
    term_input = input(f"Enter the coefficient and degree of term {i + 1} separated by a comma (e.g., 2,3 for 2*x^3): ")
    coeff, degree = map(int, term_input.split(','))
    terms.append((coeff, degree))

# Construct the polynomial
poly_expr = sum(coeff * x**degree for coeff, degree in terms)
poly = Poly(poly_expr, x, domain=Fq)
print("The polynomial is:",poly_expr)



def rabin_irreducibility_test(f, q):
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
            return "f is reducible"
    
    g = x**(q**n) - x
    g_mod_f = Poly(g, x, domain=f.domain).rem(f)
    if g_mod_f == 0:
        return "Irreducible"
    else:
        return "Reducible" 

# Compute the irreducibility test
result = rabin_irreducibility_test(poly, Fq.characteristic())
print(result)
