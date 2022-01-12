# https://rosalind.info/problems/ini3/

f = open('./rosalind_ini3.txt')

l = []
for line in f:
     l.append(list(line.strip('\n').split(' ')))


s = l[0][0]

a = int(l[1][0])
b = int(l[1][1])
c = int(l[1][2])
d = int(l[1][3])


res = s[a:b+1] + ' ' + s[c:d+1]

print(res)
