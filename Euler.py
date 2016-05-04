# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 16:53:44 2016

@author: shams.daniel
"""

from __future__ import division
import numpy as np

#Set Parameters
N=1000
T=np.power(10,1)
dt=0.01
F_initial = -1
C_initial = 1
t = np.linspace(0,T,int(T/dt))
c_0 = -1.1
gamma = 0
f = np.ones((N,1))

F = F_initial*np.ones((N,len(t)))
C = C_initial*np.ones((N,len(t)))

def Flee(F,C,f):
    return F - (np.power(F,3))/3 - C + f

def Calm(F,C,c_0,gamma):
    return F - (gamma*C) + c_0
    
for n in range(1,len(t)):    
    for i in range(0,N):   
        F[i,n] = F[i,n-1] + Flee(F[i,n-1],C[i,n-1],f[i])*dt
        C[i,n] = C[i,n-1] + Calm(F[i,n-1],C[i,n-1],c_0,gamma)*dt
    


    