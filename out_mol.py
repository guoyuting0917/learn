#!/usr/bin/python3
import pandas as pd 
import numpy as np 
import scipy.constants as C
import os
import re

#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)
N=1
dim=3
select_atom=36504

out_dat="out_mol_deal"+str(select_atom)+".dat"
input_dat="ke.dat"

select_dat=("out_mol"+str(select_atom)+".dat")

df=pd.read_csv(select_dat,sep='\s+')
df['total']=df['c_ke_h_eth']+df['c_pe_h_eth']
df['temp']=2/dim*df['c_ke_h_eth']*4184/6.022140857e+23/(C.Boltzmann*N)
df.to_csv(out_dat,sep=' ',index=0)
print(df.mean())