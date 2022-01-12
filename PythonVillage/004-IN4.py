# https://rosalind.info/problems/ini4/

f = open('./rosalind_ini4.txt')

l = []
for line in f:
     l.append(list(line.strip('\n').split(' ')))


a = int(l[0][0])
b = int(l[0][1])


odds = []
for n in range(a,b+1):
    if n % 2 == 1:
        odds.append(n)

res = sum(odds)
print(res)
