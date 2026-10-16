import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    x=np.array(x)
    y=np.array(y)
    n=len(x)
    euclid_dist=0
    for i in range (n):
        sqrd_dist=(x[i]-y[i])**2
        euclid_dist+=sqrd_dist
    return float(np.sqrt(euclid_dist))
        
        
    # Write code here
    pass