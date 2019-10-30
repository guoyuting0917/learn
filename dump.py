#!/usr/bin/python3
import pandas as pd 
import numpy as np 
import os
import re



out_dat="out_mol.dat"
input_dat="keall.dat"
select_atom=36504
select_dat=("out_mol"+str(select_atom)+".dat")

def first_word(text: str) -> str:
    return re.search("([\w']+)", text).group(1)

def title(input_dat,out_dat):
	f=open(out_dat,'w')
	ff=open(select_dat,'w')
	with open(input_dat,'r') as file:
		data=file.readlines()
	n=0
	for line in data:
		n=n+1
		if "NUMBER OF ATOMS" in line:       
			N_atom=int(data[n])
		if "ITEM: ATOMS" in line:       
			f.write(line.split(' ',2)[2])
			ff.write(line.split(' ',2)[2])
			break
	return(N_atom)	


def number_of_atoms(input_dat,out_dat,select_dat,N_atom,select_atom):
	
	f=open(out_dat,'a')
	ff=open(select_dat,'a')
	with open(input_dat,'r') as file:
		data=file.readlines()
		n=0

	for line in data:
		n=n+1
		m=0
		if "ITEM: ATOMS" in line: 
			while m<N_atom:
				f.write(data[n+m])
				if (int(first_word(data[n+m]))==select_atom):
					ff.write(data[n+m])
				m=m+1
		

#            line_input=line_start.split() 
	return 

N_atom=title(input_dat,out_dat)
number_of_atoms(input_dat,out_dat,select_dat,N_atom,select_atom)
