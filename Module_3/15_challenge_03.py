#Atividade 15 - Desafios: Análise de algoritmos

#Dasafio 3
print('\n', '-'*15, 'Desafio 3', '-'*15, '\n')

def pesbi(reg, lis):
    
    if len(lis) == 0:
        return -1
    
    esq = 0
    dir = len(lis)-1

    meio = int((esq+dir)/2)
    
    while esq <= dir and reg != lis[meio]:
        if reg > lis[meio]:
            esq = meio+1
        else:
            dir = meio-1
        
        meio = int((esq+dir)/2)
        print(meio)

    if reg == lis[meio]:
        return meio
    else:
        return -1

seqcres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
j = pesbi(9,seqcres)

print(seqcres, j)

# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <