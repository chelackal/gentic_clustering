# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 10:42:07 2020

@author: Alish Chelackal
"""

"""This module contains first part P1 of the project.
Last function ParseSeqfile is the main function .
"""

def checkIfvalid(seq):
    """looks for, if sequence contains  characters other than A,C,G,T
    """
    valid_seq = 'ACGT'
    for j in seq:
            if j not in valid_seq:
                raise RuntimeError('malformed')
    return


    
def Parseline(l):
    """Parses each line of file and creates a tuple of 2 strings and it 
    Returns a tuple 
    """
    if l[0] != '>' and l[0] != '\n':
        raise RuntimeError('malformed')

    if l[0] == '>':
        l_new = l[1:len(l)-1] #removes 1st(">") & last("\n") of the sequence 
        firstchar = len(l_new) - len(l_new.lstrip()) #index of first non-whitespace char

        # exception  handling if there is no space between label and sequence
        try:
            s_1,s_2 = l_new[firstchar:].split(' ',1) 
        except ValueError:
            raise RuntimeError('malformed')

        check_label(s_1)

        s2_mod = (s_2.replace(' ','')).upper()
        checkIfvalid(s2_mod)
        
        tup = tuple()
        tup = s_1,s2_mod
        return tup
def check_label(lab):
    """look for possible errors in the  label"""
    validSeq = 'ACGT'
    count = 0    
    for j in lab:
        if j in validSeq:
            count += 1
                
    #looks for if label is missing
    if count == len(lab):
        raise RuntimeError('malformed')

    #looks for, if no space between label and sequence
    if count >= .5 * len(lab) and lab[-1].isupper():
        raise RuntimeError('malformed')
    return    
    
def ParseSeqFile(file_name):
    """Parses the input file and creates a list of tuples 
    """
    my_list = []  
    f = open(file_name,'r')
    for line in f:
        t = Parseline(line)
        if t != None:
            my_list.append(t)
    return my_list
#################################testing##################################################        
#testing phase   outputed the following 
 #[('Mouse', 'ACCAAACATCCAAACACCAACCCCAGCCCTTACGCAATCATACAAAGAATATT'), ('Bovine', 'ACCAAACCTGTCCCCATCTAACACCAACCCACATATACAAGCTAAACCAAAAATACC'), ('Gibbon', 'ACTATACCCACCCAACTCGACCTACACCAATCCCCACATAGCACACAGACCAACAACCTC'), ('Orangutan', 'ACCCCACCCGTCTACACCAGCCAACACCAACCCCCACCTACTATACCAACCAATAACCTC'), ('Gorilla', 'ACCCCATTTATCCATAAAAACCAACACCAACCCCCATCTAACACACAAACTAATGACCCC'), ('Chimp', 'ACCCCATCCACCCATACAAACCAACATTACCCATCCAATATACAAACACCTC'), ('Human', 'ACCCCACTCACCCATACAAACCAACACCACTCTCCACCTAATATACAAATACCTC')]
#when this commented code was used with seq.txt file
#print(ParseSeqfile('seq.txt'))
