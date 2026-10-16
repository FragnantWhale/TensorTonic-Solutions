from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    if not x:
        return {"mean": 0.0, "median": 0.0, "mode": 0.0}
    x=np.sort(np.array(x))
    y=set(x)
    n=len(x)
    mean=np.mean(x)
    median=np.median(x)
    max_count=0
    modes=[]
    for i in y:
        count=0
        for j in x:
            if j==i:
                count+=1   
        if count>max_count:
            max_count=count
            modes=[i]
        elif count==max_count:
            modes.append(i)
    mode=min(modes)
    return {"mean":float(mean), "median":float(median), "mode":float(mode)}
    pass