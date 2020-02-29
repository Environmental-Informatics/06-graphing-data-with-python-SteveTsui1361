#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:32:48 2020

@author: xu1361
"""
# using unmpy
import matplotlib.pyplot as plt
import numpy as np
t = np.arange(0., 6., 0.2)
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
plt.show()
