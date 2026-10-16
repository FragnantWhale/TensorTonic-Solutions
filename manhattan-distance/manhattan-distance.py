import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    x=np.array(x)
    y=np.array(y)
    n=len(x)
    man_dist=0
    for i in range(n):
        dist=np.abs(x[i]-y[i])
        man_dist+=dist
    return float(man_dist)
    
    # Write code here
    pass