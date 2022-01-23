import re

def n_palavras_unicas(lista_palavras): 
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

def n_palavras_diferentes(lista_palavras): 
        '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
        freq = dict()
        for palavra in lista_palavras:
            p = palavra.lower()
            if p in freq:
                freq[p] += 1
            else:
                freq[p] = 1

        return len(freq)

def separa_palavras(frase): 
        '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
        return frase.split()
    
def separa_frases(sentenca): 
        '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
        return re.split(r'[,:;]+', sentenca)
  
def separa_sentencas(texto): 
        '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
        sentencas = re.split(r'[.!?]+', texto)
        if sentencas[-1] == '':
            del sentencas[-1]
        return sentencas
texto = "Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova."

acumulador = 0
num_car_sent = 0
total_frases = 0
num_car_frases = 0
ass_cp = []
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
ttr_texto = n_palavras_diferentes(palavras)/len(palavras)# RELAÇÃO TYPE-TOKEN
hlr_texto = n_palavras_unicas(palavras)/len(palavras)# RAZÃO HAPAX-LEGOMANA
sal_texto = num_car_sent/len(novas_sentencas)# TAMANHO MÉDIO DE SENTENÇA
sac_texto = total_frases/len(novas_sentencas) # COMPLEXIDADE MEDIA DE SENTENÇA
pal_texto = num_car_frases/total_frases# TAMANHO MÉDIO DE FRASE


# TESTADOR SE AS FUNÇÕES DE REGISTRO SÃO RETORNADAS CORRETAMENTE 
print("Esse é o vetor de palavras: ", palavras)
print("Esse é o número de palavras do texto: ", len(palavras))
print("Esse é o número de letras do texto: ", acumulador)
print("O tamanho médio de palavra é: ", wal_texto)
print("Relação type-token: ", ttr_texto)
print("Razão HAPAX-LEGOMANA: ", hlr_texto)
print("SENTENÇAS: ", len(novas_sentencas))
print("Soma dos numeros de caracteres em sentenças: ", num_car_sent)
print("Tamanho médio da sentença: ", sal_texto)
print("Complexidade de sentença: ", sac_texto)
print("Numero total de frases: ", total_frases)
print("Tamanho médio de frase: ", pal_texto)

def compara_assinatura(as_a, as_b):
        '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
        i = len(as_b)
        print(i)
        j = 0
        absoluto = 0
        print(j, absoluto)
        while j < i:
                absoluto = absoluto + abs(as_a[j]-as_b[j])
                j += 1
        sab = absoluto/6
        print(sab)
                        
        return sab

def compara_assinatura(as_a, as_b):
                '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
                i = len(as_b)
                j = 0
                while j < i:
                        absoluto = abs(as_a[j]-as_b[j])
                        i += 1
                sab = absoluto/6
                        
                return sab
