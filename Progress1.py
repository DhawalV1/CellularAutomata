from sympy import symbols, expand, Poly, GF


input_str = input("Enter numbers separated by spaces: ")
array = [int(num) for num in input_str.split()]


def GenerateCharacteristicsPoly(rule_vec):

        x = symbols('x')
        n = len(rule_vec)

        # helper function for polynomial over GF(2)
        convert_to_gf2 = lambda poly: sum(coeff * symbols('x')**i for i, coeff in enumerate(reversed(Poly(poly, symbols('x')).set_domain('GF(2)').all_coeffs())))

        p_array = [1, x + rule_vec[0]]

        for i in range(2,n+1):
            curr = expand((x+rule_vec[i-1])*p_array[-1])
            p_array.append(convert_to_gf2(curr + p_array[-2]))

        return p_array[-1]



def decideMaximality(rule_vector):

    generate_binary_strings = [format(i, f'0{3}b') for i in range(2**3)][::-1]
    
    # the index_set takes the rule vector by only including the index of cells following rule 90
    # for example index_set = {0,2,4} means [90,150,90,150,90], index_set = {1,3,4} means [150,90,150,90,90]
    n_input = len(rule_vector)
    rule_90 = {}
    rule_150  = {}
    r_90 = f'{90:0{8}b}'
    r_150 = f'{150:0{8}b}'
    for i,key in enumerate(generate_binary_strings):
        rule_90[key] = r_90[i]
        rule_150[key] = r_150[i]
    

    current = f'{1:0{n_input}b}'             #started with ...00001

    print("The rule vector is",rule_vector,"and the cell length is",n_input)
    
    have = current
    new = '0'*(n_input+1)
    periodicity = 0
    store = {}
    while have!=new:
        
        exec = '0' + current + '0'
        new = ''
        for i in range(len(exec)-2):
            if rule_vector[i] == 90:
                new += rule_90[exec[i:i+3]]
            else:
                new += rule_150[exec[i:i+3]]
        if new in store:
            
            if new!=f'{1:0{n_input}b}':
                return 'not cyclic thus not maximal'
                
        current = new
        store[new] = periodicity
        periodicity += 1
    else:
        if periodicity == 2**n_input-1:

            bin_rule_vec = [0 if 90 else 1 for i in rule_vector]

            print('The primitive characteristics polynomial is:')

            return GenerateCharacteristicsPoly(bin_rule_vec)

            
        else:
            return "Not a maximal_length CA"


print(decideMaximality(array))
