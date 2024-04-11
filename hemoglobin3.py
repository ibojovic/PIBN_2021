#!/usr/bin/env python2
import sys
import networkx as nx
import matplotlib.pyplot as plt


def parse_mitab(filename,org,id1=0,id2=1):
	gi={}
	f=open(filename,'r')
	for line in f:
		if line[0]=='#': continue
		line=line.rstrip()
		v=line.split('\t')
		if v[id1].find('uniprotkb:')==-1 or v[id2].find('uniprotkb:')==-1: continue
		if v[9].find('taxid:'+org)==-1 or v[10].find('taxid:'+org)==-1: continue
		gid1=v[id1].split('|')[0].split(':')[1].split('-')[0] #to remove isoforms 
		gid2=v[id2].split('|')[0].split(':')[1].split('-')[0]
		gids=[gid1,gid2]		
		# sort gene identifiers to generate undirected edges
		gids.sort()
		gi[tuple(gids)]=True
	return list(gi.keys())
	
if __name__=='__main__':
	filename=sys.argv[1]
	org=sys.argv[2]
	gis=parse_mitab(filename,org)
	#for gi in gis:
		#print gi
	g=nx.Graph()
	g.add_edges_from(gis)
	#nx.draw(g)
	#plt.show()
	#print (len(list(g.node)))
	for i in nx.connected_components(g):
		nlist=list(i)
		if ('P69905' in nlist) or ('P68871' in nlist): 
			sg=g.subgraph(nlist)
		nx.draw(sg)
		plt.show()
			
	print('degree:',sg.degree('P69905'), sg.degree('P68871'))
	print('edges;', sg.edges('P69905'), sg.edges('P68871'))
	clust=nx.clustering(sg)
	print('Clustering:', clust['P69905'], clust['P68871'])
	betweenness=nx.betweenness_centrality(sg,normalized=False)
	#print(betweenness['P69905'], betweenness['P68871'])
	nodes=list(sg.nodes())
	nodes.remove('P68871')
	g1=sg.subgraph(nodes)
	nodes=list(sg.nodes())
	nodes.remove('P69905')
	g2=sg.subgraph(nodes)
	betweenness1=nx.betweenness_centrality(g1,normalized=False)
	betweenness2=nx.betweenness_centrality(g2,normalized=False)
	print (betweenness1['P69905'],betweenness2['P68871'])
	
	
	
	'''gx=nx.Graph()
	gx.add_edges_from(sg.edges('P69905') + sg.edges('P68871'))
	nx.draw(gx,with_labels=True)
	plt.show()
	#or gi in gis:
			print (gi[0],gi[1]) '''
