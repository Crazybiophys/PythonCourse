with open('C://rosalind_hamm.txt') as file:
    dna=file.read()
dna=dna.split('\n')

def hamming(strand):
    dist=0
    for i in range(len(strand[0])):
        if strand[0][i]==strand[1][i]:
            continue
        elif strand[0][i]!=strand[1][i]:
            dist+=1
    return (dist)

if dna[0]>=dna[1]:
    hamming(dna)