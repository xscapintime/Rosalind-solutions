# https://rosalind.info/problems/ini2/

f = open('./rosalind_ini2.txt')

l = []
for line in f:
     l.append(list(line.strip('\n').split(' ')))


res = float(l[0][0]) ** 2 + float(l[0][1]) ** 2

print(res)



