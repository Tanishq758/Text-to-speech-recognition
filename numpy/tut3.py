import numpy as np

arr=np.arange(0,20)
indices=[2,3,4,5]
print(arr[indices])
print("\n")
mask=arr>7
print(arr[mask])