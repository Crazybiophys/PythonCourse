with open('C://rosalind_subs (1).txt') as file:
    data=file.read().split('\n')
    dna=data[0]
    subdna=data[1]

points=''
for nucl in range(len(dna)-len(subdna)+1):
    if dna[nucl:].startswith(subdna)==True:
        points=points+'%s '%(nucl+1)
        continue
    else:
        continue
print (points)