import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    calculations = {}
    array = np.array(list)
    array = np.reshape(array, (3, 3))
    axes = (0, 1, None)
    funcs = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum
    }
    
    for key, f in funcs.items():
        calculations[key] = [f(array, axis=i).tolist() for i in axes]
    
    return calculations
