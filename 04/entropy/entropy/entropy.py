import numbers
import numpy as np

def entropy(p):
    if any([not isinstance(p_i, numbers.Number) for p_i in p]):
        raise ValueError("At least one input is not a number")
    if any([(p_i < 0.0) or (p_i > 1.0) for p_i in p]):
        raise ValueError("At least one input is out of range [0...1]")
    else:
        pass
    if not np.isclose(1, np.sum(p), atol=1e-08):
        raise ValueError("The list of input probabilities does not sum to 1")
    else:
        pass
    
    items = []
    for p_i in p:
        if p_i > 0:
            interm = p_i * np.log2(p_i)
            items.append(interm)
    return np.abs(-np.sum(items))
