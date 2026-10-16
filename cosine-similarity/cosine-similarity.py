import numpy as np
def euclidean_norm (x):
    x=np.array(x)
    return np.sqrt(np.sum(x**2))
    
    
def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a=np.array(a)
    b=np.array(b)
    numerator=np.dot(a,b)
    norm_a=np.linalg.norm(a)
    norm_b=np.linalg.norm(b)
    if norm_a==0 or norm_b==0:
        return float(0)
    return float(numerator/(norm_a*norm_b))

    
    
    pass