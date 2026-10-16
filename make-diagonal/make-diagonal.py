import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, N).
    """
    v=np.array(v)
    n=v.shape[0]
    diag=np.zeros((n,n), dtype=float)
    for i in range(n):
            diag[i][i]=v[i]
    return diag
    # Write code here
    pass