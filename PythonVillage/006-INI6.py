# https://rosalind.info/problems/ini6/

with open('./rosalind_ini6.txt') as f:
    lines = f.readlines()

s = lines[0]


wordlist = s.split()

wordfreq = {}
for w in wordlist:
    wordfreq[w] = wordlist.count(w)


out = open('./005-INI6-result.txt', 'w')

for key, value in wordfreq.items():
    print(key, value, file=out)


out.close()
