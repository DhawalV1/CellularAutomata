

# input_str = input("Enter the rules separated by spaces (keep it 90 or 150): ")
# array = [int(num) for num in input_str.split()]
# prime = int(input("Enter the Galois Field value,p: "))

from sympy import symbols, Poly
import galois
import numpy

def CharacteristicsPoly(rule_vec, p):
    x = symbols('x')
    n = len(rule_vec)
    
    # the coefficients d based on rule vector, 0 for 90 and 1 for 150
    rule_vec = [int((i - 90) / 60) for i in rule_vec]

    # Initialize the polynomial array with the first two polynomials
    p_array = [1, [ 1 , rule_vec[0]]]

    # Apply the recurrence relation to find the characteristic polynomial
    for i in range(2, n + 1):
        curr = numpy.polymul([1 , rule_vec[i - 1]],p_array[-1])
        p_array.append(numpy.polyadd(curr,p_array[-2]) % p)              # operations in GF(2)

    char_poly = Poly(p_array[-1],x)
    print('The characteristic polynomial is', char_poly)

    GF = galois.GF(p)
    poly = galois.Poly(p_array[-1], field=GF)

    # Use galois methods to check the type of characteristic polynomial
    if poly.is_primitive():
        return 'primitive, thus rule vector produce MLCA'
    elif poly.is_irreducible():
        return 'irreducible and thus not MLCA'
    else:
        return 'reducible and thus not MLCA'
    
print(CharacteristicsPoly([150, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90],2))

# Cal