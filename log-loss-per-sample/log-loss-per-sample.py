import numpy as np

def log_loss(y_true: list, y_pred: list, eps: float = 1e-15) -> list:
    """
    Returns a list of loss values.
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    # 1. Clip predictions between eps and 1 - eps safely using np.clip
    p_hat = np.clip(y_pred, eps, 1 - eps)
    
    # 2. Use element-wise operations and np.log instead of the standard math library
    loss = -(y_true * np.log(p_hat) + (1 - y_true) * np.log(1 - p_hat))
    
    # 3. Convert back to a list since the type hint requests -> list
    return loss.tolist()