import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    x=np.array(X)
    n,d=x.shape
    mu=np.mean(x, axis=0)
    x_c=x-mu
    x_ct=x_c.T
    return (np.dot(x_ct,x_c))/(n-1)
    

    
    pass