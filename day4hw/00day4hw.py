#!/usr/bin/env python

"""
usage: ./00day4hw.py <metadata.csv> <ctab_dir> <replicates.csv>

"""
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_meta = pd.read_csv( sys.argv[1])
ctab_dir = sys.argv[2]
df_meta_rep = pd.read_csv( sys.argv[3])


fem_Sxl = []
male_Sxl = []
fem_Sxl_rep = [0,0,0,0]
male_Sxl_rep = [0,0,0,0]

df_roi = df_meta_rep["sex"] == "female"
for sample in  df_meta_rep[df_roi][ "sample" ]:
    filename = ctab_dir + "/" + sample +"/t_data.ctab"
    df = pd.read_table( filename )
    df_roi2 = df[ "t_name" ] == "FBtr0331261"    
    fem_Sxl_rep.append( df[df_roi2]["FPKM"].values )
    
df_roi = df_meta_rep["sex"] == "male"
for sample in  df_meta_rep[df_roi][ "sample" ]:
    filename = ctab_dir + "/" + sample +"/t_data.ctab"
    df = pd.read_table( filename )
    df_roi2 = df[ "t_name" ] == "FBtr0331261"    
    male_Sxl_rep.append( df[df_roi2]["FPKM"].values )

df_roi = df_meta["sex"] == "female"
for sample in  df_meta[df_roi][ "sample" ]:
    filename = ctab_dir + "/" + sample +"/t_data.ctab"
    df = pd.read_table( filename )
    df_roi2 = df[ "t_name" ] == "FBtr0331261"    
    fem_Sxl.append( df[df_roi2]["FPKM"].values )
    
df_roi = df_meta["sex"] == "male"
for sample in  df_meta[df_roi][ "sample" ]:
    filename = ctab_dir + "/" + sample +"/t_data.ctab"
    df = pd.read_table( filename )
    df_roi2 = df[ "t_name" ] == "FBtr0331261"    
    male_Sxl.append( df[df_roi2]["FPKM"].values )
    
#print male_sxl_rep
#placeholder = ["1", "2","3","4","5","6","7"]    
stage = ["10", "11", "12", "13", "14A", "14B", "14C", "14D"]

plt.figure()
plt.plot(fem_Sxl, color='red', linewidth=3)
plt.plot(male_Sxl,color='blue', linewidth=3)
plt.plot(fem_Sxl_rep, color='red', linewidth=3,linestyle='dashed', marker='o')
plt.plot(male_Sxl_rep,color='blue', linewidth=3,linestyle='dashed', marker='o')
plt.xticks([0,1,2,3,4,5,6,7], stage, rotation='vertical')
plt.legend(['female', 'male','female-replicate', 'male-replicate'], loc="upper left")
plt.savefig("D4HW.1scatterplot.png")
plt.title("Sxl expression (FBtr0331261)")
plt.xlabel("Developmental stage")
plt.ylabel("FPKM")
#plt.close()
plt.show()

print "All done"
