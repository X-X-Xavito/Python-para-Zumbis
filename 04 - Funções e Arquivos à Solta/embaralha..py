import random

def embaralha(frase):
    lista = list(frase)
    random.shuffle(lista)
    return "".join(lista)
