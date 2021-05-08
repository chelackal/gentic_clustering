# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 22:42:07 2020

@author: Alish Chelackal
"""
"""
This is a test module for PAD project
"""
# Import all modules
import P1
import P2
import P3
import P4


# Parsing the file
parsed_data= P1.ParseSeqFile("seq.txt")
# Aligning the sequences
aligned_seq= P2.AlignByDP(parsed_data)
# Computing the distance matrix
distance_matrix= P3.ComputeDistMatrix(aligned_seq)
# Extracting species list
species_list= P2.species
# Constructing the Phylogeny tree
phylogeny_tree= P4.Cluster(distance_matrix,species_list)
#DIsplaying the Phylogeny tree
#print(phylogeny_tree)


