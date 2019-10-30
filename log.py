#!/usr/bin/python3
import pandas as pd 
import numpy as np 
import os
import re



out_dat="thermal.dat"
input_dat="log.lammps"

def first_word(text: str) -> str:
    return re.search("([\w']+)", text).group(1)

def thermal(input_dat,out_dat):
	f=open(out_dat,'w')
	with open(input_dat,'r') as file:
		data=file.readlines()
	n=0
	for line in data:

		if "Loop" in line:
			n=0 
			break
		if(n==1):       
			f.write(line)
		if"Per" in line:       
			n=1		
	return()	


thermal(input_dat,out_dat)
