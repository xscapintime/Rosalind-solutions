# https://rosalind.info/problems/dna/


with open('rosalind_dna.txt') as f:
    lines = f.readlines()

string = lines[0]


base = ['A', 'C', 'G', 'T']


DNA_freq = dict([(key, 0) for key in base])

for b in string:
    if b == 'A':
        DNA_freq[b] += 1
    elif b == 'C':
        DNA_freq[b] += 1
    elif b == 'G':
        DNA_freq[b] += 1
    elif b == 'T':
        DNA_freq[b] += 1


[ print(value) for key, value in DNA_freq.items() ]

#for key,value in DNA_freq.items():
#    print(value)
