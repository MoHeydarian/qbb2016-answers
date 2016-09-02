#!/usr/bin/env python
"""
usage 

"""


import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
chip = pd.read_table( sys.argv[1], header=None)
fpkm= pd.read_table( sys.argv[2], header=None)


#chip.columns = ["name", "size","covered", "sum","mean0", "mean"]
#fpkm.columns = ["transcript", "FPKM"]

df_joined = fpkm.merge( chip, left_on=0, right_on=0)



model = sm.OLS(df_joined[5], df_joined[2])
results = model.fit()
print(results.summary())



#print df_joined