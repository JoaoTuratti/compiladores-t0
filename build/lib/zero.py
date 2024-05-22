# SPDX-License-Identifer: MIT

"""Implementação do exercício zero."""


def procura_maior(lista):
    """Procura maior item na lista usando procura linear."""
    maior = lista[0]
    for item in lista[1:]:
        if item > maior:
            maior = item
    return maior

def procura_menor(lista):
    """procura o menor item na lista"""
    menor = lista[0]
    for item in lista[1:]:
        if item < menor:
            menor = item
    return menor

def procura_impares(lista):
    """procura numeros impares"""
    impares = []
    for item in lista:
        if (item%2) != 0:
            impares.append(item)
    return impares

def procura_pares(lista):
    """procura numeros pares"""
    pares = []
    for item in lista:
        if (item%2) == 0:
            pares.append(item)
    return pares