#!/usr/bin/env python3
import sys
import numpy as np

def parse_pdb(filename,chain):
	pdb_coords={}
	f=open(filename, 'r')
	for line in f:
		line=line.rstrip()
		if (line[:4]=='ATOM' or line[:6]=='HETATM') and line[21]==chain:
			pass
		else:
			continue
		resn=int(line[22:26].strip())
		res=line[17:20].strip()
		if res=='HOH': continue #get rid of water molecules
		atom=line[12:16].strip()
		x=float(line[30:38])
		y=float(line[38:46])
		z=float(line[46:54])
		coord=[x,y,z]
		pdb_coords[resn]=pdb_coords.get(resn,{})
		pdb_coords[resn][atom]=coord
		pdb_coords[resn]['name']=res
	return pdb_coords


def get_distance(coord1,coord2):
  return np.sqrt((coord1[0]-coord2[0])**2+\
	(coord1[1]-coord2[1])**2+\
	(coord1[2]-coord2[2])**2)


def get_min_dist(res_coords1, res_coords2, th=4.0):
	atm_dists=[]
	keys1=list(res_coords1.keys())
	keys1.remove('name')
	keys2=list(res_coords2.keys())
	keys2.remove('name')
	for k1 in keys1:
		for k2 in keys2:
			dist=get_distance(res_coords1[k1],res_coords2[k2])
			#print(res_coords1['name'],k1,res_coords2['name'],k2,dist)
			if dist<=th: atm_dists.append([res_coords1['name'],k1,res_coords2['name'],k2,dist])
	return atm_dists

	 

def get_het_dist(pdb_coords,chain,heme,oxy):
	keys=list(pdb_coords.keys())
	keys.remove(heme)
	keys.remove(oxy)
	keys.sort()
	for k in keys:
		atm_dists=get_min_dist(pdb_coords[k],pdb_coords[heme])
		for l in atm_dists:
			print(str(k)+ '\t'+'\t'.join([str(j) for j in l]))
		atm_dists=get_min_dist(pdb_coords[k],pdb_coords[oxy])
		for l in atm_dists:
			print(str(k)+ '\t'+'\t'.join([str(j) for j in l]))



def get_chain_dist(pdb_coords1,pdb_coords2,chain1,chain2):
    keys1=list(pdb_coords1.keys())
    keys2=list(pdb_coords2.keys())
    keys1.sort()
    keys2.sort()
    for k1 in keys1:
        name1=pdb_coords1[k1]['name']
        if name1=='OXY' or name1=='HEM': continue
        for k2 in keys2:
            name2=pdb_coords2[k2]['name']
            if name2=='OXY' or name2=='HEM': continue
            atm_dists=get_min_dist(pdb_coords1[k1],pdb_coords2[k2])
            for l in atm_dists:
                print(chain1+str(k1)+'\t'+chain2+str(k2)+'\t'+'\t'.join([str(j) for j in l]))
		
		
		
if __name__ == '__main__':
  filename=sys.argv[1]
  chain1=sys.argv[2]
  chain2=sys.argv[3]
  pdb_coords1=parse_pdb(filename,chain1)
  pdb_coords2=parse_pdb(filename,chain2)
  get_chain_dist(pdb_coords1,pdb_coords2, chain1,chain2)
  #atm_dists=get_min_dist(pdb_coords[2],pdb_coords[4],)
  #print(atm_dists)
  #get_het_dist(pdb_coords, chain, 1142, 1143)
  #for i in range(1,142):
	  #atm_dists=get_min_dist(pdb_coords[i],pdb_coords[1143])
	  #if len(atm_dists)>0:
		  #for k in atm_dists:
			  #print(i,k)
 
  
