import numpy as np  

np.random.seed(42)  # Per riproducibilità
arr = np.random.rand(10, 3)  # Array 10x3 con valori casuali tra 0 e 1  

idx = np.abs(arr - 0.5).argmin(axis=1)  
closest_values = arr[np.arange(arr.shape[0]), idx]  

print(arr)  
print(closest_values)