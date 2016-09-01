#!/usr/bin/env python

"""
usage: ./04lunch2.py ~/data/results/stringtie/SRR072893/t_data.ctab ~/data/results/stringtie/SRR072915/t_data.ctab 
"""
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#loading the two data files in
df_ctab = pd.read_csv(sys.argv[1], sep="\t")
df2_ctab = pd.read_csv(sys.argv[2], sep="\t")



#selecting Sxl transcripts w FPKM > 1000 from the first file
df_roi = df_ctab[ "gene_name" ] == "Sxl"
df_sxl = df_ctab[df_roi]
df_temp = df_sxl[ "FPKM" ] > 0
df_sxl_exp = df_sxl[df_temp]

#selecting Sxl transcripts w FPKM > 1000 from the second file
df2_roi = df2_ctab[ "gene_name" ] == "Sxl"
df2_sxl = df2_ctab[df2_roi]
df2_temp = df2_sxl[ "FPKM" ] > 0
df2_sxl_exp = df2_sxl[df2_temp]
#merging the two files
df_overlapp = pd.merge( df_sxl_exp, df2_sxl_exp, on="gene_name")

#print out the table
#print df_overlapp


names = ["SRR072893", "SRR072915"]


# Extract the first feature from the dataset

plt.figure()                       # Open a blank canvas
plt.title("Sxl isoform expression") # Add a title to the top
plt.boxplot([df_sxl_exp["FPKM"], df2_sxl_exp["FPKM"]], labels=names)
plt.yscale("log")
plt.xlabel("Sample")              # Label the x-axis
plt.ylabel("log10(FPKM)")              # Label the y-axis with the first feature name
plt.savefig("day4ex1.png")   # Save the plot
plt.close()                        # Close the canvas




