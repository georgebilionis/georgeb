import numpy as np

def expansion(universe, num_spaces):
    
    spacer = " " * num_spaces
    
    expanded_universe = np.array([spacer.join(word) for word in universe])
    return expanded_universe

