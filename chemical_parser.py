"""
This module allows for the parsing of chemical equations.

A chemical equation is composed of two sides separated by the '<=>' marker.

----------------------------------Functions-------------------------------------
1. parse_equation
    Takes an equation in the form of a string and returns two dictionaries
    contained in a list. The first dictionary contains the reactants of the
    reaction mapped to their coefficients, and the second dictionary contains
    the products mapped to their coefficients.
2. parse_side
    This equation takes a side and returns a dictionary containing the chemicals
    in that side mapped to their respective coefficients.
3. strip
    This function takes a side and removes the first chemical. It then returns
    the coefficient, the chemical, and the rest of the side (or None) if nothing
    remains after the chemical.
--------------------------------------------------------------------------------
"""

def parse_equation(eqn):
    ''' See documentation above for description.

    >>> Reaction = parse_equation("1H2CO3 <=> 1H+ + 1HCO3-")
    >>> Reaction == [{'H2CO3': 1}, {'H+': 1, 'HCO3-': 1}]
    True
    '''
    match = re.search(r'([\s\S]+)<=>([\s\S]+)', eqn)
    if match is None:
        raise Exception('Malformed equation')
    else:
        reactants_side = match.group(1).strip()
        products_side = match.group(2).strip()
    return [parse_side(reactants_side), parse_side(products_side)]

def parse_side(side):
    '''See documentation above for description.
    '''
    curr_coeff, chem, side = strip(side)
    side_dict = {chem: curr_coeff}
    while side is not None:
        curr_coeff, chem, side = strip(side)
        side_dict[chem] = curr_coeff
    return side_dict

def strip(side):
    '''See documentation above for description.
    '''
    if re.search(r' ', side) is None:
        chemical, remainder = side, None
    else:
        match = re.search(r'(.+?)[ ]+\+[ ]+(.+)', side)
        chemical = match.group(1).strip()
        remainder = match.group(2).strip()
    match = re.search(r'(\d*)(.+)', chemical)
    coefficient = 1 if match.group(1) == "" else eval(match.group(1))
    return coefficient, match.group(2), remainder
