import sys
import numpy as np
# from pymc import *
import Wavelets


def get_likelihood(residuals, sigma_w, sigma_r, gamma=1.0):
    like = 0.0
    # Arrays of zeros to be passed to the likelihood function
    aa, bb, M = Wavelets.getDWT(residuals)
    # Calculate the g(gamma) factor used in Carter & Winn...
    if(gamma == 1.0):
        g_gamma = 1.0 / (2.0 * np.log(2.0))  # (value assuming gamma=1)
    else:
        g_gamma = (2.0) - (2.0)**gamma
    # log-Likelihood of the aproximation coefficients
    sigmasq_S = (sigma_r**2) * g_gamma + (sigma_w)**2
    tau_a = 1.0 / sigmasq_S
    like += normal_like(bb[0], 0.0, tau_a)
    k = long(0)
    SS = range(M)
    for ii in SS:
        # log-Likelihood of the detail coefficients with m=i...
        if(ii == 0):
            sigmasq_W = (sigma_r**2) * \
                (2.0**(-gamma * np.double(1.0))) + (sigma_w)**2
            tau = 1.0 / sigmasq_W
            like += normal_like(bb[1], 0.0, tau)
        else:
            sigmasq_W = (sigma_r**2) * \
                (2.0**(-gamma * np.double(ii + 1))) + (sigma_w)**2
            tau = 1.0 / sigmasq_W
            for j in range(2**ii):
                like += normal_like(aa[k], 0.0, tau)
                k = k + 1
    return like
