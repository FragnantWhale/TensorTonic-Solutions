import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    # Write code here
    x=np.array(x)
    n=len(x)
    mean=np.mean(x)
    y=np.sum((x-mean)**2)
    s=np.sqrt( ( 1/ (n - 1) ) * y )
    if s==0 and mean==mu0:
        return float(0)
    if s==0 and mean!=mu0:
        return float(np.inf) if mean>mu0 else float(-np.inf)
    else:
        return float( (mean - mu0)*(np.sqrt(n)) / s )
    
    pass