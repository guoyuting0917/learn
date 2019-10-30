#!/usr/bin/python3
import pandas as pd 
import numpy as np 



read_dat="temp_silanol_ave1.dat"
result_temp=open("temp_silanol_ave2.dat",'w')

df=pd.read_csv(read_dat,sep='\s+')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df['Ntemp']=df['temp']/5*6

print(df,file=result_temp)

	#Ncotemp_ave=df.Ncotemp[(df['Coord1']>a)&(df['Coord1']<b)].mean()
	#Ncount_ave=df.Ncount[(df['Coord1']>a)&(df['Coord1']<b)].sum()
	#temp_ave=Ncotemp_ave/Ncount_ave

#	print(df.temp[(df['Coord1']>a)&(df['Coord1']<b)].mean()) #simple average temp 
#	print(c,temp_ave,file=result_temp)
	



#print(df)
