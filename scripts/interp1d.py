# -*- coding: utf-8 -*-
"""
Script for interpolating between two points
Created on Wed Aug 26 22:50:17 2015

@author: Andre
"""
import numpy as np
#from scipy.interpolate import interp1d

T1 = 950. #Celsius
T2 = 54. #Celsius

# temperature
t = np.array([900.,1000.])

# Seebeck coefficient
alpha = np.array([40.,38.9])

alpha1 = np.interp(T1,t,alpha)

# Second interpolation
# temperature
t = np.array([0.,100.])

# Seebeck coefficient
alpha = np.array([39.4,41.4])

alpha2 = np.interp(T2,t,alpha)


print alpha1, alpha2

emf1 = alpha1*T1
emf2 = alpha2*T2

print emf1- emf2

