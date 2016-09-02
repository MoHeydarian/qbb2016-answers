#!/usr/bin/env python

"""
usage: ./03day4hw.py <input1> <input2>
"""
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df_ctab = pd.read_table(sys.argv[1])
df2_ctab = pd.read_table(sys.argv[2])


#df_log = np.log10(df_ctab)
#df_log = np.log10(df2_ctab)

df_overlapp = pd.merge( df_ctab, df2_ctab, on="t_name")


df_M_plot = np.log2((df_overlapp["FPKM_y"]+1)/(df_overlapp["FPKM_x"]+1)) 
df_A_plot = (np.log2((df_overlapp["FPKM_y"]+1)*(df_overlapp["FPKM_x"]+1))/2)



plt.figure()
plt.scatter( df_A_plot, df_M_plot, alpha = 0.1, c='black')
plt.title("MA plot comparing SRR072893 and SRR072915")
plt.xlabel("A")
plt.ylabel("M")
plt.savefig( "D4HW.3MAplot.png" )
plt.show()

print "All done!!! Boom baby, BOOM!"

