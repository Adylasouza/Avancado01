def imprime_nome(nome):
    print(f"Nome: {nome}")


def piramide(num):
    for i in range(1, num + 1):
        for x in range(0, i):
            print(i, end=" ")
        print()

def contVogais(texto):
    '''código que fiz
    texto = "O rato roeu a roupa do rei de Roma"
    vogais= "a", "e", "i" , "o", "u"
    soma = 0

    for x in range(0,(len(texto))):
        if texto == vogais:
            soma= vogais+1
        print(soma)'''

    contar= 0
    for x in range (len(texto)):
        if texto[x]  == "a" or texto[x] == "e" or texto[x]=="i" or texto[x] =="o" or texto[x]=="u":
            contar=contar+1
    print(contar)