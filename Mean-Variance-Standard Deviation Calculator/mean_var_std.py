import numpy as np

def calculate(list):
    
    try:
      numpy_list = np.array(list).reshape((3, 3))
    except:
      raise ValueError("List must contain nine numbers.")
    
    calculations = {
        'mean': [np.mean(numpy_list, axis = 0).tolist(), np.mean(numpy_list, axis = 1).tolist(), np.mean(numpy_list).tolist()], 
        'variance': [np.var(numpy_list, axis = 0).tolist(), np.var(numpy_list, axis = 1).tolist(), np.var(numpy_list).tolist()], 
        'standard deviation': [np.std(numpy_list, axis = 0).tolist(), np.std(numpy_list, axis = 1).tolist(), np.std(numpy_list).tolist()], 
        'max': [np.max(numpy_list, axis = 0).tolist(), np.max(numpy_list, axis = 1).tolist(), np.max(numpy_list).tolist()], 
        'min': [np.min(numpy_list, axis = 0).tolist(), np.min(numpy_list, axis = 1).tolist(), np.min(numpy_list).tolist()], 
        'sum': [np.sum(numpy_list, axis = 0).tolist(), np.sum(numpy_list, axis = 1).tolist(), np.sum(numpy_list).tolist()], 
        }
    
    return calculations
