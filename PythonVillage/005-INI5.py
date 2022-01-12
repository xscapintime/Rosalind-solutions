# https://rosalind.info/problems/ini5/

with open('./rosalind_ini5.txt') as f:
    lines = f.readlines()

out = open('./005-INI5-result.txt', 'w')

num = 0
for line in lines:
    if num % 2 == 1:
        print(line.strip(), file=out)
    num += 1


out.close()


