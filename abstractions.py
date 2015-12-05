from chemical_parser import *

class ChemicalReaction:
    '''Stores all the information related to the chemical reaction at hand.
    '''

    def __init__(self, reaction):
        self.reactants, self.products = parse_equation(reaction)
        self.concentrations = {}
        for chemical, _ in self.reactants.items():
            self.concentrations[chemical] = (
                float(input("Initial concentration of " + chemical + "? ")))
        for chemical, _ in self.products.items():
            self.concentrations[chemical] = (
                float(input("Initial concentration of " + chemical + "? ")))

    def __str__(self):
        reactants_str, products_str = '', ''
        for chemical, coeff in self.reactants.items():
            reactants_str += (str(coeff) + chemical if reactants_str == '' else
                              ' + ' + str(coeff) + chemical)
        for chemical, coeff in self.products.items():
            products_str += (str(coeff) + chemical if products_str == '' else
                             ' + ' + str(coeff) + chemical)
        return reactants_str + ' <=> ' + products_str

    def __repr__(self):
        return "ChemicalReaction('{0}')".format(self.__str__())

    def forward(self, change):
        for chemical, coeff in self.reactants.items():
            self.concentrations[chemical] -= coeff * change
        for chemical, coeff in self.products.items():
            self.concentrations[chemical] += coeff * change

    def reverse(self, change):
        self.forward(-change)

    @property
    def reaction_quotient(self):
        numer, denom = 1, 1
        for chemical, coeff in self.products.items():
            numer *= pow(self.concentrations[chemical], coeff)
        for chemical, coeff in self.reactants.items():
            denom *= pow(self.concentrations[chemical], coeff)
        return numer / denom
