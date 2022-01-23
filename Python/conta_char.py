def conta_letras(frase, contar="vogais"):
    cont = 0
    if contar == "vogais":
        cont += frase.count("a")
        cont += frase.count("e")
        cont += frase.count("i")
        cont += frase.count("o")
        cont += frase.count("u")

        return cont
    elif contar == "consoantes":
        cont += frase.count("b")
        cont += frase.count("c")
        cont += frase.count("d")
        cont += frase.count("f")
        cont += frase.count("g")
        cont += frase.count("h")
        cont += frase.count("j")
        cont += frase.count("k")
        cont += frase.count("l")
        cont += frase.count("m")
        cont += frase.count("n")
        cont += frase.count("p")
        cont += frase.count("q")
        cont += frase.count("r")
        cont += frase.count("s")
        cont += frase.count("t")
        cont += frase.count("v")
        cont += frase.count("w")
        cont += frase.count("x")
        cont += frase.count("y")
        cont += frase.count("z")

        return cont

#print(conta_letras('programamos em python'))
#print(conta_letras('programamos em python', 'vogais'))
#print(conta_letras('programamos em python', 'consoantes'))
        
        
        
        
        
