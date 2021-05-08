# -*- coding: utf-8 -*-
"""
Created on Sat Dec 5 22:42:07 2020

@author: Alish Chelackal
"""

"""This module contains P4 of the project.Last function Cluster(DistMatrix,list_labels)
is the main function.
"""
def createdict(Matrix,List):
    """creates a 2D dictionary corresponding to the distance matrix and list of labels
    """
    n = len(List)
    #to get all possible combinations
    input_combns = list(itertools.combinations(range(0,n),2))
    d = defaultdict(dict)
    for x in input_combns:
        i,j = x
        p,q = List[i],List[j]
        d[p][q] = Matrix[i][j]
    return d



from collections import defaultdict
import itertools

def checkInput(Matrix,List):
    """ checking on input to make sure that input is the required input format
    """
    
    if type(Matrix) != list or type(List) != list:
       
        raise RuntimeError('malformed')
    for k in Matrix:
        if type(k) != list:
           
            raise RuntimeError('malformed')
        if len(k) != len(List):
         
            raise RuntimeError('malformed')
        for j in k:
            if type(j) != int and type(j) != float:
               
                raise RuntimeError('malformed')
            if j > 30:
             
                raise RuntimeError('malformed')
    for p in List:
        if type(p) != str:
            
            raise RuntimeError('malformed')

    if len(Matrix) != len(List):
        
        raise RuntimeError('malformed')
    return
            

    

def CreateTree(d,list_L):
    """Recursive function to create a binary tree
    """
  
    d_new = defaultdict(dict)
    
    #labels corresponding to minimum evolutionary distance in Matrix
    a,b = minInDict(d)

    n = ['(',a,',',b,')']
    new_cluster = ''.join(n)
    
    #remove the entries in newly formed cluster from our list
    for k in list_L:
        if k == a:
            list_L.remove(k)
            break
    for p in list_L:
        if p == b:
            list_L.remove(p)
            break

    #to remove an existing cluster with those entries
    for j in list_L:
        if a in j or b in j:
            list_L.remove(j)

    #Base case of our recursive function   
    if len(d) == 1:
        return new_cluster

    #calculating distances from our new cluster(eg: (a,b))to other labels/clusters
    for q in list_L:
            
        if b in d:
            if q in d[a] and q in d[b]:
                d_new[new_cluster][q] = (d[a][q] + d[b][q])/2
                continue
        if q in d:
            if b in d[q] and q in d[a]:
                d_new[new_cluster][q] = (d[a][q] + d[q][b])/2
                continue
            if b in d:
                if a in d[q] and q in d[b]:
                    d_new[new_cluster][q] = (d[q][a] + d[b][q])/2
                    continue
            if a in d[q] and b in d[q]:
                d_new[new_cluster][q] = (d[q][a] + d[q][b])/2
    
    list_L.insert(0,new_cluster)
    
    #deleting row and column corresponding to a and b
    del d[a]
    if b in d:
        del d[b]
        
    for p in d:
        for q in d[p]:
            if q != b and q != a:
                d_new[p][q] = d[p][q]

    return CreateTree(d_new,list_L)


def minInDict(dist):
    """to find the minimum value/distance in our dictionary and returning
    the  corresponding to this minimum value
    """
    m = float('inf')
    for p in dist:
        for q in dist[p]:
            if dist[p][q] < m:
                m = dist[p][q]
                a,b = p,q
    return a,b


def Cluster(Dist_Matrix,list_labels):
    """Cluster the labels according to the distance matrix andoutputs a binary tree 
    """
    checkInput(Dist_Matrix,list_labels)
    dict_distMatrix = defaultdict(dict)
    dict_distMatrix = createdict(Dist_Matrix,list_labels)

    tree = CreateTree(dict_distMatrix,list_labels)
    return print(tree)
#################################testing##############################################################
  # this  testing  with the follwoing label and matirx   and gave the following result
  #((Bovine,Gibbon),((((Chimp,Human),Gorilla),Orangutan),Mouse))
#marix=[[0.0, 0.4522470626742357, 0.4522470626742357, 0.3641308618362756, 0.3641308618362756, 0.30409883108112323, 0.31925086156926286], [0.4522470626742357, 0.0, 0.3681187177944908, 0.3802009262047681, 0.4197118409515671, 0.4408399986765892, 0.30409883108112323], [0.4522470626742357, 0.3681187177944908, 0.0, 0.36360138775851414, 0.5033762053808775, 0.28235817842618405, 0.31811793084023765], [0.3641308618362756, 0.3802009262047681, 0.36360138775851414, 0.0, 0.35584348469633686, 0.30409883108112323, 0.2326161962278796], [0.3641308618362756, 0.4197118409515671, 0.5033762053808775, 0.35584348469633686, 0.0, 0.22219936210737928, 0.2326161962278796], [0.30409883108112323, 0.4408399986765892, 0.28235817842618405, 0.30409883108112323, 0.22219936210737928, 0.0, 0.14836930749743993], [0.31925086156926286, 0.30409883108112323, 0.31811793084023765, 0.2326161962278796, 0.2326161962278796, 0.14836930749743993, 0.0]]
#lable1=[('Mouse'), ('Bovine'), ('Gibbon'), ('Orangutan'), ('Gorilla'), ('Chimp'), ('Human')]
#print(Cluster(marix,lable1))    
#print(type(marix))
