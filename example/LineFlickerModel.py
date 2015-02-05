import sys
sys.path.append("../WaveletCode")
sys.path.append("../")
import FlickerLikelihood
import numpy as np
from pymc import *
import Wavelets
 
#  Functions  #
def model(t,a,b):
    return a*t+b
 
# Get the data #
 
t,data = np.loadtxt('flicker_dataset.dat',unpack=True)
 
# Priors #
 
b = Uniform('b',-10,10)
a = Uniform('a',-1,1)
sigma_w = Uniform('sigma_w',0,100)
sigma_r = Uniform('sigma_r',0,100)
 
# Likelihood #
@observed
def likelihood(value=data,t=t,a=a,b=b,sigma_w=sigma_w,sigma_r=sigma_r):
    residuals=data-model(t,a,b)
    return FlickerLikelihood.get_likelihood(residuals,sigma_w,sigma_r)
