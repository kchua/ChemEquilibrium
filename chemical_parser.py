"""
This file contains all the necessary functions to read an equation from user
input.

Parse equation: the main function that reads an equation from a string.
Read coefficient: reads the coefficient before a string.
Read chemical: reads a chemical after read coefficient reads a coefficient.

The parse equation function returns two dictionaries in a list:
(I)  A dictionary containing the reactants mapped to their respective
     coefficients
(II) A dictionary containing the products mapped to their respective
     coefficients

Rules to ensure proper parsing:
1) Within each section of the equation, there must be +'s between each
   chemical.
2) Between the two sections of the equation, there must be the symbol '<=>'
   (Cannot be separated by spaces).
3) There can be an arbitrary number of spaces between chemicals and +'s.
"""

import re

def parse_equation(equation):
    ''' See documentation above.

    >>> Reaction = parse_equation("1H2CO3 <=> 1H+ + 1HC03-")
    >>> Reaction == [{"H2CO3": 1}, {"H+": 1; "HCO3-": 1}]
    True
    '''
    i, max_index = 0, len(equation)
    reactants, products = {}, {}
    current = reactants              # current changing dictionary
    new_chemical = True
    while i < max_index:
        if equation[i] == ' ':
            i += 1
        elif equation[i] == '<':     # Shift over to product dictionary
            if equation[i + 1] != '=' or equation[i + 2] != '>':
                raise Exception("Malformed equation.")
            i += 3
            current, new_chemical = products, True
        elif equation[i] == '+':
            new_chemical = True
            i += 1
        else:
            if new_chemical:
                coeff, i = read_coefficient(equation, i)
                chemical, i = read_chemical(equation, i)
                current[chemical] = coeff
                new_chemical = False
            else:
                raise Exception("Malformed equation.")
    return (reactants, products)

def strip(side):
    '''This function combines the functionality of read_coefficient and
    read_chemical. However, it does not return the index; instead, it returns
    what remains after stripping a chemical from a side with the chemical and
    its corresponding coefficient. (Note: assumes that side has no trailing or
    leading whitespace.)
    '''
    if re.search(r' ', side) not None:
        chemical, remainder = side, None
    else:
        match = re.search(r'() +\+ +()', side)
        chemical = match.group(1).strip()
        remainder = chemical.group(2).strip()
    match = re.search(r'(\d*)()', chemical)
    coefficient = 1 if match.group(1) == "" else eval(match.group(1))
    return coefficient, match.group(2), remainder
