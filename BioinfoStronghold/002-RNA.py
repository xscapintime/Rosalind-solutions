# https://rosalind.info/problems/rna/

with open('rosalind_rna.txt') as f:
    lines = f.readlines()

DNA = lines[0]

RNA = DNA.replace('T', 'U')
print(RNA)
