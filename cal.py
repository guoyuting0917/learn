#!/usr/bin/python3
import pandas as pd 
import numpy as np 

pd.set_option('display.max_columns', None)

keyword="c24"
read_dat="thermal.dat"
out_dat="see.dat"

df=pd.read_csv(read_dat,sep='\s+')


df['vdw+coul+long']=df['E_vdwl']+df['E_coul']+df['E_long']
df['E_pair+mol']=df['E_pair']+df['E_mol']
#df.to_csv(out_dat,sep=' ',index=0,float_format='%.8f',columns=['Time','E_pair','vdw+coul+long','PotEng','E_pair+mol'])
#print(df['TotEng'].describe(include='all'))
print(df.describe(include='all'))
	#Ncotemp_ave=df.Ncotemp[(df['Coord1']>a)&(df['Coord1']<b)].mean()
	#Ncount_ave=df.Ncount[(df['Coord1']>a)&(df['Coord1']<b)].sum()
	#temp_ave=Ncotemp_ave/Ncount_ave

#	print(df.temp[(df['Coord1']>a)&(df['Coord1']<b)].mean()) #simple average temp 
	#print(c,temp_ave,file=result_temp)
	



#print(df)
