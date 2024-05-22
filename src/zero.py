# SPDX-License-Identifer: MIT

"""Implementação do exercício zero."""


def procura_maior(lista):
    """Procura maior item na lista usando procura linear."""
    return max(lista)

def procura_menor(lista):
    """Procura o menor item na lista."""
    return min(lista)

def procura_impares(lista):
    """Procura numeros impares."""
    impares = []
    for item in lista:
        if (item%2) != 0:
            impares.append(item)
    return impares

def procura_pares(lista):
    """Procura numeros pares."""
    pares = []
    for item in lista:
        if (item%2) == 0:
            pares.append(item)
    return pares
