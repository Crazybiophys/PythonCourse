with open('C://rosalind_revc.txt') as file:
    dna=file.read()
    
def complementing(strand):
    complement='complementing a Strand of DNA: '
    for nucl in range(len(strand)):
        if dna[-nucl-1]=='A':
            complement+='T'
        elif dna[-nucl-1]=='T':
            complement+='A'
        elif dna[-nucl-1]=='C':
            complement+='G'
        elif dna[-nucl-1]=='G':
            complement+='C'
    return(complement)
    
complementing(dna)
        