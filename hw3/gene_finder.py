# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Nitya Dhanushkodi
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons
from random import shuffle

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output



def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    amino_acids = '';
    count_triple = range(0,len(dna),3)
    codon_search = range(0,len(codons))
    
    for i in count_triple:
        triplet = dna[i:i+3]
        for j in codon_search:
            if triplet in codons[j]:
                amino_acids += aa[j]
                
    return amino_acids    
        


def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
    input1 = 'ATCGTCAGT'
    eoutput1 = 'IVS'
    output1 = coding_strand_to_AA(input1)
    
    input2 = 'CTGATCGAT'
    eoutput2 = 'LID'
    output2 = coding_strand_to_AA(input2)
    
    
    input3 = 'CTGATCAGTCGAATGTAGCAGCATTGC'
    eoutput3 = 'LISRM|QHC'
    output3 = coding_strand_to_AA(input3)
    
    
    print "input: " + input1 + "\n" + "expected output: " + eoutput1 + "\n"+ "output: " + output1
    print "input: " + input2 + "\n" + "expected output: " + eoutput2 + "\n"+ "output: " + output2
    print "input: " + input3 + "\n" + "expected output: " + eoutput3 + "\n"+ "output: " + output3
    
    
    
def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    seqsize = len(dna)
    complement = ''
    for i in range(seqsize-1, -1, -1):
        if dna[i] == 'A':
            complement += 'T'
        elif dna[i] == 'T':
            complement += 'A'
        elif dna[i] == 'C':
            complement += 'G'
        elif dna[i] == 'G':
            complement += 'C'
            
    return complement    
    
    
    
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
        
    input1 = 'ATCGTCAGT'
    eoutput1 = 'ACTGACGAT' 
    output1 = get_reverse_complement(input1)
    
    input2 = 'CTGATCGAT'
    eoutput2 = 'ATCGATCAG'
    output2 = get_reverse_complement(input2)
    
    input3 = 'CTGATCAGTCGAATGTAGCAGCATTGC'
    eoutput3 = 'GCAATGCTGCTACATTCGACTGATCAG'
    output3 = get_reverse_complement(input3)
   
    print "input: " + input1 + "\n" + "expected output: " + eoutput1 + "\n"+ "output: " + output1
    print "input: " + input2 + "\n" + "expected output: " + eoutput2 + "\n"+ "output: " + output2
    print "input: " + input3 + "\n" + "expected output: " + eoutput3 + "\n"+ "output: " + output3



def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    count_triple = range(0,len(dna), 3)
    ORF = ''
    
    for i in count_triple:
        triplet = dna[i:i+3]
        if triplet == 'TAG' or triplet == 'TAA' or triplet == 'TGA':
            break
        else:
            ORF+= triplet

    return ORF
    
    

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
        
    input1 = 'ATGGTCAGT'
    eoutput1 = 'ATGGTCAGT' 
    output1 = rest_of_ORF(input1)
    
    input2 = 'ATGCTGATCTAA'
    eoutput2 = 'ATGCTGATC'
    output2 = rest_of_ORF(input2)
    
    input3 = 'ATGATCAGTCGAATGTAGCAGCATTGA'
    eoutput3 = 'ATGATCAGTCGAATG'
    output3 = rest_of_ORF(input3)
   
    print "input: " + input1 + "\n" + "expected output: " + eoutput1 + "\n"+ "output: " + output1
    print "input: " + input2 + "\n" + "expected output: " + eoutput2 + "\n"+ "output: " + output2
    print "input: " + input3 + "\n" + "expected output: " + eoutput3 + "\n"+ "output: " + output3
    
    
        
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    all_ORFs = []
    i = 0;
    
    #when the loop finds a starter codon, it stores the ORF 
    while i < len(dna)+3:
        triplet = dna[i:i+3]
        if triplet == 'ATG':
            ORF = rest_of_ORF(dna[i:len(dna)])
            advance = len(ORF)
            all_ORFs.append(ORF)
            i += advance #goes to the end of the ORF to continue looking through the segment
        else:
            i += 3
         
    return all_ORFs
     
            
     
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """

    input1 = 'ATGGTCAGTTAGGATATGCGC'
    eoutput1 = ['ATGGTCAGT' , 'ATGCGC']
    output1 = find_all_ORFs_oneframe(input1)
    
    input2 = 'ATGCTGATCTAA'
    eoutput2 = ['ATGCTGATC']
    output2 = find_all_ORFs_oneframe(input2)
    
    input3 = 'ATGATCAGTCGAATGTAGCAGCATTGAATGTAGATG'
    eoutput3 = ['ATGATCAGTCGAATG', 'ATG', 'ATG']
    output3 = find_all_ORFs_oneframe(input3)
   
    print "input: " + input1 + "\n" + "expected output: " + str(eoutput1) + "\n"+ "output: " + str(output1)
    print "input: " + input2 + "\n" + "expected output: " + str(eoutput2) + "\n"+ "output: " + str(output2)
    print "input: " + input3 + "\n" + "expected output: " + str(eoutput3) + "\n"+ "output: " + str(output3)
    
    

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """     
    all_ORFs = []
    
#    all_ORFs.append(find_all_ORFs_oneframe(dna[0:len(dna)])[0])
#    all_ORFs.append(find_all_ORFs_oneframe(dna[1:len(dna)])[0]) #offset by 1
#    all_ORFs.append(find_all_ORFs_oneframe(dna[2:len(dna)])[0]) #offset by 2

    all_ORFs += (find_all_ORFs_oneframe(dna[0:len(dna)]))
    all_ORFs += (find_all_ORFs_oneframe(dna[1:len(dna)])) #offset by 1
    all_ORFs += (find_all_ORFs_oneframe(dna[2:len(dna)])) #offset by 2
    
    return all_ORFs



def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
        
    input1 = 'ATGGATGGTTAGGATATAAGC'
    eoutput1 = ['ATGGATGGT' , 'ATGGTTAGGATA']
    output1 = find_all_ORFs(input1)
    
    input2 = 'AAATGCTGATCTAA'
    eoutput2 = ['ATGCTGATC']
    output2 = find_all_ORFs(input2)
    
    input3 = 'ATGATCAGTCGAATGTAGCAATGTTGAATGTAG'
    eoutput3 = ['ATGATCAGTCGAATG', 'ATG', 'ATGTTGAATGTAG']
    output3 = find_all_ORFs(input3)
   
    print "input: " + input1 + "\n" + "expected output: " + str(eoutput1) + "\n"+ "output: " + str(output1)
    print "input: " + input2 + "\n" + "expected output: " + str(eoutput2) + "\n"+ "output: " + str(output2)
    print "input: " + input3 + "\n" + "expected output: " + str(eoutput3) + "\n"+ "output: " + str(output3)



def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    all_ORFs = [] 
    reverse_complement = get_reverse_complement(dna)
    #APPEND FOR DEBUGGING TO SEE IF DNA AND REVERSE COMPLEMENT GIVE THE RIGHT STUFF
    
    all_ORFs += (find_all_ORFs(dna)) #Finds ORFs for first strand
    all_ORFs += (find_all_ORFs(reverse_complement)) #Finds ORFs for reverse complement
    
    return all_ORFs



def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """
       
    input1 = 'ATGGATGGTTAGGATATACAT'
    eoutput1 = ['ATGGATGGT' , 'ATGGTTAGGATA', 'ATGTATATCCTAACCATCCAT']
    output1 = find_all_ORFs_both_strands(input1)
    
    input2 = 'AAATGCTCATCTAA'
    eoutput2 = ['ATGCTCATC', 'ATGAGCATTT']
    output2 = find_all_ORFs_both_strands(input2)
    
    input3 = 'ATGATCAGTCGAATGTAGCATTGTTGAATGTAG'
    eoutput3 = ['ATGATCAGTCGAATG', 'ATG', 'ATGCTACATTCGACTGATCAT']
    output3 = find_all_ORFs_both_strands(input3)
   
    print "input: " + input1 + "\n" + "expected output: " + str(eoutput1) + "\n"+ "output: " + str(output1)
    print "input: " + input2 + "\n" + "expected output: " + str(eoutput2) + "\n"+ "output: " + str(output2)
    print "input: " + input3 + "\n" + "expected output: " + str(eoutput3) + "\n"+ "output: " + str(output3)



def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""

    all_ORFs = find_all_ORFs_both_strands(dna)
    long_ORF = max(all_ORFs, key=len)
    return long_ORF



def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    input1 = 'ATGGATGGTTAGGATATACAT'
    eoutput1 = 'ATGTATATCCTAACCATCCAT'
    output1 = longest_ORF(input1)
    
    input2 = 'AAATGCTCATCTAA'
    eoutput2 = 'ATGAGCATTT'
    output2 = longest_ORF(input2)
    
    input3 = 'ATGATCAGTCGAATGTAGCATTGTTGAATGTAG'
    eoutput3 = 'ATGCTACATTCGACTGATCAT'
    output3 = longest_ORF(input3)
   
    print "input: " + input1 + "\n" + "expected output: " + eoutput1 + "\n"+ "output: " + output1
    print "input: " + input2 + "\n" + "expected output: " + eoutput2 + "\n"+ "output: " + output2
    print "input: " + input3 + "\n" + "expected output: " + eoutput3 + "\n"+ "output: " + output3



def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    longest_ORFs = []
    s = list(dna)
    for i in range(0,num_trials):
        shuffle(s)
        collapse(s)
        longest_ORFs.append(longest_ORF(s))
    
    long_ORF = max(longest_ORFs, key=len)
    return long_ORF
        
        

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """

    all_ORFs = find_all_ORFs_both_strands(dna)
    amino_acids = []
    for i in range(0,len(all_ORFs)):
        if all_ORFs[i]> threshold:
            aa = coding_strand_to_aa(all_ORFs[i])
            amino_acids.append(aa)
            
            
            