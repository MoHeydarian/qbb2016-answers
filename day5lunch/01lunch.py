#!/usr/bin/env python
"""
usage 

"""
###for plotting PCA clusters??

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_table( sys.argv[1])

#removing unimportant chromosomes
df_chr = df.loc[df["chr"].isin(["2L", "2R", "3L", "3R", "4", "X"])]


#getting correct start and end positions - plus strand
df_roi = df_chr["strand"]== "+"
df_plus = df_chr[df_roi]
df_plus["start"] = df_plus["start"]-500
df_plus["end"] = df_plus["start"]+1000
selected = ["chr","start","end","t_name"]
df_plus_bed = pd.DataFrame(df_plus, columns=selected)


#getting correct start and end positions - minus strand
df_roi = df_chr["strand"]== "-"
df_minus = df_chr[df_roi]
df_minus["end"] = df_minus["end"]+500
df_minus["start"] = df_minus["end"]-1000
selected = ["chr","start","end","t_name"]
df_minus_bed = pd.DataFrame(df_minus, columns=selected)

#concatenating plus and minus stand bed entries
both = [df_plus_bed, df_minus_bed]
df_both_bed = pd.concat(both)



##makign a table with the t_name and FPKM
rolex = ["t_name","FPKM"]
df_fpkm_tab = pd.DataFrame(df_chr, columns=rolex)

df_fpkm_tab.to_csv("fpkm_table", index=False, index_label = False, sep = "\t", header=False)

df_both_bed.to_csv("promoters.bed", index=False, index_label = False, sep = "\t", header=False)