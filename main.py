import os
from abstractions import *
from chemical_parser import *

def repl():
    '''The main loop that executes the entire program.
    '''
    while True:
        reaction = ChemicalReaction(input("Type out the chemical reaction below \n\n"))
        K = float(input("\nWhat is the equilibrium constant? \n\n"))
        while True:
            try:
                print(reaction.reaction_quotient)
                if abs(reaction.reaction_quotient - K) <= 1e-4:
                    print(reaction.reaction_quotient)
                    print(reaction.concentrations)
                    break
                else:
                    pre_error = abs(reaction.reaction_quotient - K)
                    if reaction.reaction_quotient <= K:
                        reaction.forward(calculate_change(reaction, K, pre_error))
                    else:
                        reaction.reverse(calculate_change(reaction, K, pre_error))
            except ZeroDivisionError:
                reaction.reverse(1e-3)
        if input("Calculate another equation? (Y/N) ") == 'N':
            print("Goodbye!")
            break

def calculate_change(reaction, K, previous):
    '''Calculates how much an equation should progress based on the difference
    between the reaction quotient and the equilibrium constant(P), and based
    on previous error (I).
    '''
    error = abs(reaction.reaction_quotient - K)
    return (error + previous) * 1e-5

repl()
os._exit(-1)
