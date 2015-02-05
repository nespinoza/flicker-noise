import numpy as np
import matplotlib.pyplot as plt
import pymc
import LineFlickerModel
 
# Set the number of iterations and burnins:
niterations = 1e4
nburn = 1e3
 
# Set MAP estimates as starting point of MCMC. First, calculate MAP estimates:
M = pymc.MAP(LineFlickerModel)
M.fit()
# Now set this as starting point for the MCMC:
mc=pymc.MCMC(M.variables)
 
# And start the sample!
mc.sample(iter=niterations+nburn,burn=nburn)
 
# Plot the final samples (posterior samples):
pymc.Matplot.plot(mc)
plt.show()
