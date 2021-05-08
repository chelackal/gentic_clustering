# -*- coding: utf-8 -*-
"""
Created on Thu 19 19:45:01 2020

@author: Alish Chelackal
"""
"""This module contains P3 of the project.Last function ComputeDistMatrix(alignment) is the main function .
"""
import math
import itertools

def checkInput(input_d):
    """ error handllîng """
    if not input_d:
        raise RuntimeError('malformed')
    if type(input_d) != dict:
        raise RuntimeError('malformed')
        
    for key in input_d:
        try:
            s1,s2 = input_d.get(key)
            i,j = key
        except ValueError:
            raise RuntimeError('malformed')
        CheckIfValid(i,j,s1,s2)
    return
def initMatrix(d):
    """Initialises the matrix with dimensions according to the input"""
    l = []
    if d:
        for k in d:
            i,j = k
            l.append(i)
            l.append(j)
    checkCombinations(l,d)
    
    #looks for, if combinations with 0 
    if 0 in l:
        startIndex = 0
    else:
        startIndex = 1
        
    w = h = max(l) #width and height of matrix
    Mat = [[0 for i in range(w)] for j in range(h)]
    return Mat,startIndex

def checkCombinations(list_in,dict_in):
    """looks if all possible combinations that are present in the input
    dictionary
    """
    list1 = []
    N = max(list_in)
    
    #if key(tuples) start from index(0,0)
    if 0 not in list_in:
        all_combn = list(itertools.combinations(range(1,N+1),2))
        for key in dict_in:
            i,j = key
            list1.append((i,j))
        if set(all_combn) != set(list1):
            raise RuntimeError('malformed')
            
    # if key(tuples) start from index(1,1)        
    elif 0 in list_in:
        all_combn = list(itertools.combinations(range(0,N+1),2))
        if set(all_combn) != set(list1):
            raise RuntimeError('malformed')
        
def CheckIfValid(i,j,sq1,sq2):
    """looks for, i,j are integers and sq1,sq2 contain only valid characters
    """
    valid_seq = 'ACGT--'    
    
    if type(i) != int or type(j) != int:
        raise RuntimeError('malformed')
    if type(sq1) != str or type(sq2) != str:
        raise RuntimeError('malformed')
        
    if len(sq1) != len(sq2):
            raise RuntimeError('malformed')
    for a,b in zip(sq1,sq2):
        if (a not in valid_seq) or (b not in valid_seq):
            raise RuntimeError('malformed')
    return
    


def seqDistance(sq1,sq2):
    """Computes the pairwise distance between seq1 & seq2"""
    count = 0
    denom = 0
    for a,b in zip(sq1,sq2):
        #to exclude all empty spaces 
        if a == '-' or b == '-':
            pass
        elif a != b:
            count += 1
            denom += 1
        elif a == b:
            denom += 1
    if denom == 0:
        d = 30
        return d 
                
    p = count / denom
    
    if p >= 3/4:
        d = 30
    else:
        d = (-3/4) * math.log(1 - (4/3)*p)

    return float(d)
    
def ComputeDistMatrix(alignment):
    """Creates a symmetrical matrix with zeros along the diagonal of the matrix.
    """
    checkInput(alignment)

    Matrix,start_pos = initMatrix(alignment)
    
    for key in alignment:
        s1,s2 = alignment.get(key)
        i,j = key
        #filling in matrix ,also considering starting index of combinations(i,j)
        
        if start_pos == 0:
            Matrix[i][j] = Matrix[j][i] = seqDistance(s1,s2)
        else:
            Matrix[i-1][j-1] = Matrix[j-1][i-1] = seqDistance(s1,s2)

    return Matrix
        
 #########################################testing##################################################  
#the test phaese has run with the 'input' and the following outut was given 
#[[0, 0.4522470626742357, 0.4522470626742357, 0.3641308618362756, 0.3641308618362756, 0.30409883108112323, 0.31925086156926286], [0.4522470626742357, 0, 0.3681187177944908, 0.3802009262047681, 0.4197118409515671, 0.4408399986765892, 0.30409883108112323], [0.4522470626742357, 0.3681187177944908, 0, 0.36360138775851414, 0.5033762053808775, 0.28235817842618405, 0.31811793084023765], [0.3641308618362756, 0.3802009262047681, 0.36360138775851414, 0, 0.35584348469633686, 0.30409883108112323, 0.2326161962278796], [0.3641308618362756, 0.4197118409515671, 0.5033762053808775, 0.35584348469633686, 0, 0.22219936210737928, 0.2326161962278796], [0.30409883108112323, 0.4408399986765892, 0.28235817842618405, 0.30409883108112323, 0.22219936210737928, 0, 0.14836930749743993], [0.31925086156926286, 0.30409883108112323, 0.31811793084023765, 0.2326161962278796, 0.2326161962278796, 0.14836930749743993, 0]]    
#input={(1, 2): ('ACCAAACATCCAAACA-CCAAC-CCCAGCC-CTTACGCAATC-ATACAAAGAATATT', 'ACCAAACCTGTCCCCATCTAACACCAACCCACATATACAAGCTAAACCAAAAATACC'), (1, 3): ('ACCA-A-ACATCCAA-AC-ACCAAC-CCCA-GCCCTTA-CGCAATCATACAAAGAATATT', 'ACTATACCCACCCAACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC'), (1, 4): ('A--CCAAACATCCA-AACA-CCAACCCCAGCCCTTACGCAATCATA-CAAAGAAT-A--TT', 'ACCCCACCCGTCTACACCAGCCAACACCAACCCCCAC-CTACTATACCAACCAATAACCTC'), (1, 5): ('A--CCAAACATCC--AAACACCAACCCCAGCCCTTACGCAATCATACAAA-GAAT-A--TT', 'ACCCCATTTATCCATAAAAACCAACACCAACCCCCA-TCTAACACACAAACTAATGACCCC'), (1, 6): ('A--CCAAACATCCA-A-ACACCAACCCCAGCCCTTACGCAATCATACAAAGAATATT', 'ACCCCATCCACCCATACAAACCAACATTA-CCCAT-C-CAAT-ATACAAA-CACCTC'), (1, 7): ('A--CCAAACATCCA-A-ACACCAACCCCAGCCCT-TACGCAATCATACAAAGAATATT', 'ACCCCACTCACCCATACAAACCAACACCA-CTCTCCACCTAAT-ATACAAA-TACCTC'), (2, 3): ('ACCAAACCTGTCC--C-C-ATCTAACACCAACCCACATATA-CAAGCTAAACCAAAAATACC', 'ACTATACCCACCCAACTCGACCT-ACACCAATCCCCACATAGCACAC-AGACCAACAACCTC'), (2, 4): ('ACCAAACCTGTC--C-CCATCTAACACCAACCCACATATACAAGCTAAACCAAAAATACC', 'ACCCCACCCGTCTACACCAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC'), (2, 5): ('ACCAAACCTGTCC---CCATCTAACACCAACCCACATAT-ACAAGCTAAACCAAAAATACC', 'ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACAC-AAACTAATGACCCC'), (2, 6): ('ACCAAACCTGTCCCCATCTAACACCAAC-CCACATATACAAGCTAAACCAAAAATACC', 'ACC--CCATCCACCCATACAA-ACCAACATTACCCATCCAA--TATA-CAAACACCTC'), (2, 7): ('ACCAAACCTGTCCCCATCTAACACCAAC-CCACATATACAAGCTAAACCAAAAATA-C-C', 'ACCCCA-CT-CACCCATACAA-ACCAACACCAC-TCT-CCACCTAATATACAAATACCTC'), (3, 4): ('ACTATACCCACCCA-ACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC', 'ACCCCACCCGTCTACAC-CAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC'), (3, 5): ('ACTATACCCACCCAACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC', 'ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACACAAACTAATGACCCC'), (3, 6): ('ACTATACCCACCCA-ACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC', 'ACCCCATCCACCCATAC-AAACC-A-A-C-ATTACC-CAT-CCA-ATATACAAAC-ACCTC'), (3, 7): ('ACTATACCCACCCA-ACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC', 'ACCCCACTCACCCATAC-AAACCAACACCACTCTCCACCT---A-ATATA-CAAATACCTC'), (4, 5): ('ACCCCACCCGTCTACACCAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC', 'ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACACAAACTAATGACCCC'), (4, 6): ('ACCCCACCCGTCTACACCAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC', 'ACCCCATCCACCCATACAAACCAACA-TTA--CCCATCCAATATA-C-A--AA-CACCTC'), (4, 7): ('ACCCCACCCGTCTACACCAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC', 'ACCCCACTCACCCATACAAACCAACACCACTCTCCACCTAATATA-C-A--AAT-ACCTC'), (5, 6): ('ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACACAAACTAATGACCCC', 'ACCCCATCCACCCATACAAACCAACA-TTA--CCCATCCAATATACAAAC-----ACCTC'), (5, 7): ('ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACACAAACTAATGACCCC', 'ACCCCACTCACCCATACAAACCAACACCACTCTCCACCTAATATAC--A--AAT-ACCTC'), (6, 7): ('ACCCCATCCACCCATACAAACCAACATTA--C-CCATCCAATATACAAACACCTC', 'ACCCCACTCACCCATACAAACCAACACCACTCTCCACCTAATATACAAATACCTC')}
#ComputeDistMatrix(input)


