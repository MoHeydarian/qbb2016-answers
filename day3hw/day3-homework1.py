#!/usr/bin/env python


"""
Read sequences from a fasta file, count the 
number of times each k-mer occurs across all 
sequences and print kmers and counts.

usage: 01-kmer-counter.py k < fasta_file
"""

import sys, fasta


k = 11
kmer_counts = {}
target = sys.argv[1]
query = sys.argv[2]

for ident, sequence in fasta.FASTAReader ( open(target) ):
    sequence = sequence.upper()
    for i in range ( 0, len( sequence) - k ):
        kmer = sequence [ i:i+k ]
        if kmer not in kmer_counts:
            kmer_position[ kmer ] = []
        kmer_position[ kmer ].append(i)
    
    for i, kmer in enumerate(sorted(kmer_counts, key=kmer_counts.get, reverse=True)):
        print kmer, kmer_position[kmer]


for ident, sequence in fasta.FASTAReader ( open(query) ):
    sequence = sequence.upper()
    for i in range ( 0, len( sequence) - k ):
        kmer = sequence [ i:i+k ]
        if kmer not in kmer_counts:
            kmer_position[ kmer ] = []
        kmer_position[ kmer ].append(i)
    
    for i, kmer in enumerate(sorted(kmer_counts, key=kmer_counts.get, reverse=True)):
        print kmer, kmer_position[kmer]
        