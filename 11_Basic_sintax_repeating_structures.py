#Atividade 10 - Sintaxe básica: Estruturas condicionais

#Exercício 1
print('\n', '-'*15, 'Exercício 1', '-'*15, '\n')

for i in range(0,11):
    print(i, end=' ')

print('')

num = 0

while num < 11:
    print(num, end=' ')
    num = num + 1

print('')

#Exercício 2
print('\n', '-'*15, 'Exercício 2', '-'*15, '\n')

for l in range(0,11,2):
    print(l, end=' ')

print('')

mun = 0

while mun < 11:
    if mun%2==0:
        print(mun, end=' ')
    else:
        print('', end='')
    
    mun = mun + 1

print('')

#Exercício 3
print('\n', '-'*15, 'Exercício 3', '-'*15, '\n')

sedna = 'TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT'

for i in sedna:
    if i == 'A' or i == 'T' or i == 'C' or i == 'G':
        print('DNA', end=' ')
    else:
        print('Não DNA')

print('')

print('\n', '-'*15, 'Exercício 4', '-'*15, '\n')

# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <