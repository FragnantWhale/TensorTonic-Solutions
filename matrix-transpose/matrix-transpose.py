import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    x=np.array(A)
    r=x.shape[0]
    c=x.shape[1]
    transpose=np.zeros((c,r) , dtype=float)
    for i in range(r):
        for j in range(c):
            transpose[j][i]=x[i][j]
    transpose=np.array(transpose)
    return transpose
            
    pass
