import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%pylab inline

x=np.random.normal(size=1000)
fig,ax=plt.subplots()
H=ax.his(x,bins=50, alpha = 0.5, histtype='stepfilled')