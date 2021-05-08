# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 21:30:05 2020

@author: Alish Chelackal
"""
"""This module contains P2 of the project,the function AlignByDP is the main function 
"""
import itertools

def checkInputType(in_list):
    """Makes sure input is indeed a list of tuples of two strings:
    a label and valid sequence
    """
    if type(in_list) != list:
        raise RuntimeError('malformed')
    for i in in_list:
        try:
            s_1,s_2 = i
            if type(s_1) != str or type(s_2) != str:
                raise RuntimeError('malformed')
        except ValueError:
            raise RuntimeError('malformed')
    return
        
def checkValidity(seq):
    """Checks the validity of sequences 
    """
    valid_seq = 'ACGT'
    for j in seq:
        if j not in valid_seq:
            raise RuntimeError('malformed')
    return

def init(input_list):
    """Initialisation: creates a dictionary of sequences and a list of possible pairwise sequence combinations 
    """
    dict_seq = dict()
    dict_label = dict()
    i =1
    for x in input_list:
        s_1,s_2 = x
        checkValidity(s_2)
        dict_seq[i] = s_2
        dict_label[i] = s_1
        i += 1
    n = len(input_list)    
    #to find all possible combinations for pairwise alignment of
    seq_combns = list(itertools.combinations(range(1,n+1),2))
    return dict_seq,seq_combns

def DPMatrix(sq1,sq2):
    """It makes  a Dynamic programming matrix for the sequence pair and
    Returns 2 alignments
    """
    M = len(sq1)
    N = len(sq2)
    Matr = [[0 for x in range(N+1)] for y in range(M+1)]
    match = 5
    mismatch = -2
    indel = -6

    #Boundary conditions in first row and first column
    Matr[0][0] = 0
    for i in range(1,M+1):
        Matr[i][0] = indel * i
    for j in range(1,N+1):
        Matr[0][j] = indel * j

    #Filling rest of matrix bottom-up according to the algorithm   
    for i in range(1,M+1):
        for j in range(1,N+1):
            if sq1[i-1] == sq2[j-1]:
                D = match
            else:
                D = mismatch
            score = max(Matr[i-1][j-1] + D, Matr[i-1][j]+indel, Matr[i][j-1]+indel)
            Matr[i][j] = score


    #Traceback to get optimal alignment
    sq1_list = []
    sq2_list = []
    i = M
    j = N
    
    while i > 0 and j > 0:
        if i > 0 and j > 0:
            if sq1[i-1] == sq2[j-1]:
                scr = Matr[i-1][j-1] + match
            else:
                scr = Matr[i-1][j-1] + mismatch
            if scr == Matr[i][j]:
                sq1_list.append(sq1[i-1])
                sq2_list.append(sq2[j-1])
                i -= 1
                j -= 1
                continue

        # Best score when x(i) aligned with '-'
        if i > 0:
            if Matr[i-1][j] + indel == Matr[i][j]:
                sq1_list.append(sq1[i-1])
                sq2_list.append('-')
                i -= 1
                continue

        # Best score when '-' aligned with y(j)
        if j > 0:
            if Matr[i][j-1] + indel == Matr[i][j]:
                sq1_list.append('-')
                sq2_list.append(sq2[j-1])
                j -= 1
                continue

    rev_sq1 = ''.join(sq1_list) #list to string conversion
    rev_sq2 = ''.join(sq2_list)
    Aligned_seq1 = rev_sq1[::-1] #string reversal to get aligned sequence
    Aligned_seq2 = rev_sq2[::-1]
    return Aligned_seq1,Aligned_seq2 
    
                
                

def AlignByDP(input_list):
    """Performs pairwise alignment on all combinations of input lists of sequences
    """
    # Collecting unique species labels
    global species
    species= CollectSpecies(input_list)
    checkInputType(input_list)
    if input_list == []:
        return {}
    
    output_dict = dict() 
    dict_seq,seq_combns = init(input_list)
    
    for x in seq_combns:
        a,b = x
        seq1,seq2 = dict_seq[a],dict_seq[b]
        Aligned_seq1,Aligned_seq2 = DPMatrix(seq1,seq2)
        output_dict[(a,b)] = (Aligned_seq1,Aligned_seq2)
    return output_dict
def CollectSpecies(species_data):
    """
    Returns the list of unique species label present in the input list.
    this function is mostly used in the last test.py   
    """ 
    species_list= []
    for item in range(len(species_data)):
       species_label= species_data[item][0]
       species_list.append(species_label)
    return species_list    
        
        
###############################testing################################################
#input
#input_list = [('Mouse', 'ACCAAACATCCAAACACCAACCCCAGCCCTTACGCAATCATACAAAGAATATT'), ('Bovine', 'ACCAAACCTGTCCCCATCTAACACCAACCCACATATACAAGCTAAACCAAAAATACC'),
#              ('Gibbon', 'ACTATACCCACCCAACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC'),
#              ('Orangutan', 'ACCCCACCCGTCTACACCAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC'),
#              ('Gorilla', 'ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACACAAACTAATGACCCC'),
#          ('Chimp', 'ACCCCATCCACCCATACAAACCAACATTACCCATCCAATATACAAACACCTC'), ('Human', 'ACCCCACTCACCCATACAAACCAACACCACTCTCCACCTAATATACAAATACCTC')]


#AlignByDP(input_list)
