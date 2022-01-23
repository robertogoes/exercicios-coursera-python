#a matriz é obrigatoriamente quadrada, entao eu só preciso passar um parâmetro i = j
def cria_matriz(m):
    matriz = []
    for i in range(1,(m*2)+1):
        linha = []
        k = 1
        for j in range(1,(m*2)+1):
            if i == j:
                if m < j:
                    linha.append((m*2)+1-j)
                else:
                    linha.append(i)
            if j > i:
                if j > m:
                    linha.append(j-k)
                else:
                    linha.append(i)
            if i > j:
                if i > m:
                    linha.append(i-k)
                else:
                    linha.append(j)
        matriz.append(linha)
        print(linha,"\n")
    return

m = int(input("Digite o inteiro M: "))
result = cria_matriz(m)


# elif (m < i or m < j):
