import numpy as np
import matplotlib.pyplot as pyt

sales_data=np.array([
    [1,150000,180000,220000,250000], #paradise biryani
    [2,120000,140000,160000,190000], #beijing bitess
    [3,200000,230000,260000,300000], #pizza hub
    [4,180000,210000,240000,270000], #burger point
    [5,160000,185000,205000,230000]  #chai point
])

# print(sales_data.shape)
# print(sales_data[:3,1:])
# # print(sales_data[1:3])

# sum=np.sum(sales_data,axis=0)
# print(sum[1:])


# print(np.min(sales_data[:,1:],axis=1))

# print(np.max(sales_data[:,1:],axis=0))


# print(np.mean(sales_data[:,1:],axis=1))




cumsum=np.cumsum(sales_data[:,1:],axis=1)
print(cumsum)

pyt.figure(figsize=(10,6))
pyt.plot(np.mean(cumsum,axis=0))
pyt.title("Average cumalative sales across all restaurant")
pyt.xlabel("years")
pyt.ylabel("sales")
pyt.grid(True)
pyt.show()


