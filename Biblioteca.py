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

def estoque(produto, quantidade, valorUnitario):
    valorUnitario=quantidade*valorUnitario
    return valorUnitario

def funcao(numero):
    if numero==0:
        print("Z")
    elif numero>0:
        print("P")
    else:
        print("Nf")

def soma(numero1, numero2):
    #se fosse uma tupla: def soma(*numero)
    soma = numero1+numero2
    print(soma)

def som (*a):
    #somar mais de dois numeros em uma tupla
    soma= 0
    for x in range(len(a)):
        soma+=a[x]
    print(soma)

def txt (texto):
    '''  se for contar letras e espaços em branco
     cont =0
    for x in range(len(texto)-1,-1,-1):
                print(texto[x], end= " ")
                if t[x!=" ":
                    cont+=1
    print(cont)'''
    for x in range(len(texto)-1,-1,-1):
        print(texto[x], end= " ")

def list(n):
    n=[" "]
    novalista=[" "]
    for x in range (len(n)):
        if n[x]