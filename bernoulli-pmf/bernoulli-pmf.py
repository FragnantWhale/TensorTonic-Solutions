import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    x=np.array(x)
    n=len(x)
    pmf=np.zeros((n), dtype=float)
    mean=float(p)
    variance=float(p*(1-p))
    for i in range(n):
        if x[i]==0:
            pmf[i]=1-p
        if x[i]==1:
            pmf[i]=p
    return {"pmf": pmf, "mean": mean, "variance": variance}
        
    pass