import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x=np.array(x)
    n=len(x)
    m=np.mean(x)
    squared_diff=np.sum((x-m)**2)
    variance=float((1/(n-1))*squared_diff)
    std_dev=float(np.sqrt(variance))
    return{"variance": variance, "standard_deviation": std_dev}
    pass