import numpy as np

def safe_divide(x,y):
    return np.where(y != 0, x / y, 0)
    
def l1_norm(x,Axis):
    x=np.array(x)
    l1_norm=np.sum((np.abs(x)),axis=Axis)
    if Axis==0 or Axis==None:
        return safe_divide(x,l1_norm)
    if Axis==1:
        return safe_divide(x,l1_norm[:, np.newaxis])

def l2_norm(x,Axis):
    x=np.array(x)
    l2_norm=np.sqrt(np.sum((x**2),axis=Axis))
    if Axis==0 or Axis==None:
        return safe_divide(x,l2_norm)
    if Axis==1:
        return safe_divide(x,l2_norm[:, np.newaxis])
def max_norm(x,Axis):
    x=np.array(x)
    max_norm=np.max((np.abs(x)),axis=Axis)
    if Axis==0 or Axis==None:
        return safe_divide(x,max_norm)
    if Axis==1:
        return safe_divide(x,max_norm[:, np.newaxis])
    

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    # Write code here
    x=np.array(matrix)
    if norm_type=="l1":
        return(l1_norm(x,axis))
    if norm_type=="l2":
        return(l2_norm(x,axis))
    if norm_type=="max":
        return(max_norm(x, axis))
    pass