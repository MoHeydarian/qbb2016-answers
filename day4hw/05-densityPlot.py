#!/usr/bin/env python

""""
Code borrowed from Kiara... Posting for my own reference. 
Function: reate a histogram of the FPKM values for a ctab file

usage: ./05-density.py <datafile.ctab>


"""

#imports
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

#import data
df = pd.read_table( sys.argv[1])

#Plot data
data = df[ "FPKM" ]
density = gaussian_kde(data)
xs = np.linspace( np.min(data), np.max(data) , 1000)
density.covariance_factor = lambda : .5
density._compute_covariance()
plt.figure()
plt.plot(xs,density(xs))
plt.title( "Density plot of the FPKM values for SRR072893")
#plt.yscale("log")
plt.xscale("log")
plt.ylabel( "Density" )
plt.savefig( "04densityPlot.png" )
plt.show()
#plt.close()



