# https://rosalind.info/problems/revc/

with open('rosalind_revc.txt') as f:
    lines = f.readlines()

string = lines[0]

com = []
for b in string:
    if b == 'A':
        com.append('T')
    elif b == 'C':
        com.append('G')
    elif b == 'T':
        com.append('A')
    elif b == 'G':
        com.append('C')

revc = list(reversed(com))

rev_string = ''.join(revc)

#[ += str(b) for b in revc ] 

print(rev_string)




        
