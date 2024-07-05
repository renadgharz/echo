import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import lognorm

# Operation duration in minutes --> [inpatient, oupatient]
M = [60, 45]        # mean
S = [6.07, 6.87]    # standard deviation

# Calculate parameters of distribution
in_mu = np.log(M[0]**2 / np.sqrt(S[0]**2 + M[0]**2))
in_sigma = np.sqrt(np.log(S[0]**2 / M[0]**2 + 1))

ou_mu = np.log(M[1]**2 / np.sqrt(S[1]**2 + M[1]*2))
ou_sigma = np.sqrt(np.log(S[1]**2 / M[1]**2 + 1))

# Generate random samples for inpatient and outpatient groups
samples_inpatient = lognorm.rvs(in_sigma, scale=np.exp(in_mu), size=1000)
samples_outpatient = lognorm.rvs(ou_sigma, scale=np.exp(ou_mu), size=1000)
