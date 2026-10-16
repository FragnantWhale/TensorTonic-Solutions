import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    # Write code here
    x=np.array(A)
    n=x.shape[0]
    sum=0
    for i in range(n):
        sum+=x[i][i]
    return float(sum)
    pass