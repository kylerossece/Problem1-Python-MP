import matplotlib.pyplot as plt
import numpy as np
f=np.arange(0,100)
for n in range(0,100):
 if f[n]<=9:
   f[n]=(f[n]**2)-7
 elif f[n]>=10:
     f[n]=f[n-10]
     plt.stem(f,use_line_collection=True)
     plt.show()
     plt.figure()
     plt.xlabel('x-axis')
     plt.ylabel('y-axis')
     plt.title('Problem 1')
               
               