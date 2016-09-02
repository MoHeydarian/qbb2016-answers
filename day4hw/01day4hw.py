#!/usr/bin/env python

"""
Plots a histogram with expression values of a Stringtie t_data.ctab file


usage: ./01day4hw.py <input_data>
"""
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_data = pd.read_csv( sys.argv[1], sep="\t")


df_roi = df_data[ "FPKM" ] > 0
df_nonzero = df_data[df_roi]


df_nonzero_log = np.log10(df_nonzero["FPKM"])


plt.figure()
plt.hist(df_nonzero_log,bins=100)
plt.savefig("D4HW.2.histogram.png")
plt.title("Distribution of SRR072893 expression levels")
plt.xlabel("log10(FPKM)")
plt.ylabel("Counts")
plt.savefig("D4HW.2.histogram.png")
#plt.close()
plt.show()


print "All done"