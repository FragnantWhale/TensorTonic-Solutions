import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    x=np.array(x)
    p=np.array(p)
    return float(np.sum(np.dot(x,p)))
    # Write code here
    pass