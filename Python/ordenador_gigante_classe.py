# criar função que cria vetor com elementos aleatorios
# funcao se a lista está em ordem crescente ou não
import random

class Ordenador:
    def selecao_direta(self, lista):

        fim = len(lista)

        for i in range(fim - 1):
            #inicialmente, o menor elemento já visto é o i-ésimo
            posicao_do_minimo = i

            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j

            # coloca o menor elemento encontrado no inicio da sub-lista
            # para isso, troca de lugar os elementos nas posições i e posicao_do_minimo
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]

def cria_vetor(quantidade):
    vetor = []
    cont = 0
    while cont < quantidade:
        vetor.append(random.randint(-1000,1000))
        cont += 1

    if verifica_ordem(vetor):
        print(vetor)
        print("O vetor está fora de ordem")
        o = Ordenador()
        o.selecao_direta(vetor)
        print(vetor)
    else:
        print("O vetor já está ordenado!")
        
def verifica_ordem(vetor):
# se o número anterior for maior que o posterior a lista não está ordenada
    n = len(vetor)
    for i in range(n-1):
        if vetor[i] > vetor[i+1]:
            return True
    return False
    
    
