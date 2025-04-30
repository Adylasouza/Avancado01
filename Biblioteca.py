def imprime_nome(nome):
    print(f"Nome: {nome}")


def piramide(num):
    for i in range(1, num + 1):
        for x in range(0, i):
            print(i, end=" ")
        print()