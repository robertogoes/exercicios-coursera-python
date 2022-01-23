        
import re

def le_assinatura():
        '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
        print("Bem-vindo ao detector automático de COH-PIAH.")
        print("Informe a assinatura típica de um aluno infectado:")

        wal = float(input("Entre o tamanho médio de palavra:"))
        ttr = float(input("Entre a relação Type-Token:"))
        hlr = float(input("Entre a Razão Hapax Legomana:"))
        sal = float(input("Entre o tamanho médio de sentença:"))
        sac = float(input("Entre a complexidade média da sentença:"))
        pal = float(input("Entre o tamanho medio de frase:"))

        return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
        '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
        i = 1
        textos = []
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
        while texto:
                textos.append(texto)
                i += 1
                texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

        return textos

def n_palavras_unicas(lista_palavras): #
        '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
        freq = dict()
        unicas = 0
        for palavra in lista_palavras:
                p = palavra.lower()
                if p in freq:
                        if freq[p] == 1:
                                unicas -= 1
                        freq[p] += 1
                else:
                        freq[p] = 1
                        unicas += 1

        return unicas

def n_palavras_diferentes(lista_palavras): #
        '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
        freq = dict()
        for palavra in lista_palavras:
                p = palavra.lower()
                if p in freq:
                    freq[p] += 1
                else:
                    freq[p] = 1

        return len(freq)

def separa_palavras(frase): #
        '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
        return frase.split()

def separa_frases(sentenca): #
        '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
        return re.split(r'[,:;]+', sentenca)

def separa_sentencas(texto): #
        '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
        sentencas = re.split(r'[.!?]+', texto)
        if sentencas[-1] == '':
                del sentencas[-1]
        return sentencas

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def compara_assinatura(as_a, as_b):
        '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
        i = len(as_b)
        j = absoluto = 0
        while j < i:
                absoluto = absoluto + abs(as_a[j]-as_b[j])
                j += 1
        sab = absoluto/6               
        return sab

def calcula_assinatura(texto):
        '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
        acumulador = 0
        num_car_sent = 0
        total_frases = 0
        num_car_frases = 0
        ass_txt = []
        palavras = []
        novas_sentencas = []
        novas_frases = []
        novas_palavras = []
        novas_sentencas = separa_sentencas(texto) # lista com sentencas

        for sent in novas_sentencas: # pega a primeira sentenca
                novas_frases = separa_frases(sent) # pegou a primeira sentenca e separou em varias frases
                num_car_sent = num_car_sent + len(sent)
                total_frases = total_frases + len(novas_frases)
                for fras in novas_frases:
                    num_car_frases = num_car_frases + len(fras)
                    novas_palavras = separa_palavras(fras)
                    palavras.extend(novas_palavras)

        for word in palavras:
                acumulador = acumulador + len(word)
                
        wal_texto = acumulador/(len(palavras)) # TAMANHO MÉDIO DE PALAVRA
        ass_txt.append(wal_texto)
        ttr_texto = n_palavras_diferentes(palavras)/len(palavras) # RELAÇÃO TYPE-TOKEN
        ass_txt.append(ttr_texto)
        hlr_texto = n_palavras_unicas(palavras)/len(palavras)# RAZÃO HAPAX-LEGOMANA
        ass_txt.append(hlr_texto)
        sal_texto = num_car_sent/len(novas_sentencas)# TAMANHO MÉDIO DE SENTENÇA
        ass_txt.append(sal_texto)
        sac_texto = total_frases/len(novas_sentencas) # COMPLEXIDADE MEDIA DE SENTENÇA
        ass_txt.append(sac_texto)
        pal_texto = num_car_frases/total_frases# TAMANHO MÉDIO DE FRASE
        ass_txt.append(pal_texto)
                
        return ass_txt

def avalia_textos(textos, ass_cp):
        '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
        assinatura = []
        vetor_assinatura = []
        armazenador = []
        armazena_similaridade = []
        i = 0
        
        for texto in textos:
                assinatura = calcula_assinatura(texto)
                vetor_assinatura.append(assinatura)
                assinatura = []
        for ass_txt in vetor_assinatura:
                armazenador = compara_assinatura(ass_txt, ass_cp)
                armazena_similaridade.append(armazenador)
                armazenador = []

        print(armazena_similaridade)
        indice = armazena_similaridade[0]
        pump = i
        n = len(armazena_similaridade)
        print("Valor de N é: ", n)
        
        while i < n:
                print("I: ", i)
                print(armazena_similaridade[i])
                if armazena_similaridade[i] < indice:
                        indice = armazena_similaridade[i]
                        pump = i
                i += 1
        pump = pump + 1
                
        return pump

ass_cp = le_assinatura()
textos = le_textos()
resultado = avalia_textos(textos, ass_cp)
print("O autor do texto ", resultado, "está infectado com COH-PIAH!")

