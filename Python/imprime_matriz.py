def imprime_matriz(matriz):
    for i in range(len(matriz)):
        lista = []
        for j in range(len(matriz[0])):
            creu = str(matriz[i][j])
            if j == len(matriz[0])-1:
                print(creu, end = "")
            else:
                print(creu, end = " ")
        print()
            
    return 
