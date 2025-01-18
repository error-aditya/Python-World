import re

# Function to parse the equation string and extract coefficients
def parse_equation(equation):
    pattern = r'([+-]?\d*)(x|y|z|w)'
    terms = re.findall(pattern, equation)
    coeffs = {'x': 0, 'y': 0, 'z': 0, 'w': 0}
    
    for coeff, var in terms:
        if coeff == '' or coeff == '+':
            coeff = 1
        elif coeff == '-':
            coeff = -1
        else:
            coeff = int(coeff)
        
        coeffs[var] = coeff
    
    upper_bound = int(equation.split('<=')[-1].strip())
    
    return coeffs, upper_bound

# Function to count the number of valid solutions
def count_valid_solutions(eq1, eq2, R):
    coeffs1, N1 = parse_equation(eq1)
    coeffs2, N2 = parse_equation(eq2)
    
    valid_results = set()
    
    for x in range(R + 1):
        for y in range(R + 1 - x):
            for z in range(R + 1 - x - y):
                for w in range(R + 1 - x - y - z):
                    if x + y + z + w > R:
                        continue
                    
                    result1 = coeffs1['x'] * x + coeffs1['y'] * y + coeffs1['z'] * z + coeffs1['w'] * w
                    result2 = coeffs2['x'] * x + coeffs2['y'] * y + coeffs2['z'] * z + coeffs2['w'] * w
                    
                    if result1 <= N1 and result2 <= N2 and result1 == result2:
                        valid_results.add(result1)
    
    return len(valid_results)

# Read the input
eq1 = input().strip()  # First equation string
eq2 = input().strip()  # Second equation string
R = int(input().strip())  # Sum constraint R

# Call the function and output the result
result = count_valid_solutions(eq1, eq2, R)
print(result)

