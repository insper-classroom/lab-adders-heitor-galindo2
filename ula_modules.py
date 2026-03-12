#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blocos combinacionais de somadores em MyHDL.

Este modulo declara implementacoes de:
- meio somador (half adder),
- somador completo (full adder),
- somador de 2 bits,
- somador generico por encadeamento,
- somador vetorial comportamental.
"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):

    @always_comb
    def comb():
        soma.next = a ^ b
        carry.next = a & b

    return instances()


from myhdl import block, always_comb, Signal, instances

@block
def fullAdder(a, b, c, soma, carry):

    s = [Signal(bool(0)) for i in range(3)]

    ha1 = halfAdder(a, b, s[0], s[1])
    ha2 = halfAdder(s[0], c, soma, s[2])

    @always_comb
    def comb():
        carry.next = s[1] | s[2]

    return instances()


from myhdl import block, Signal, instances

@block
def adder2bits(x, y, soma, carry):
    
    carry_intermediario = Signal(bool(0))

    # Soma do bit menos significativo
    ha = halfAdder(
        x[0],
        y[0],
        soma[0],
        carry_intermediario
    )

    # Soma do bit mais significativo
    fa = fullAdder(
        x[1],
        y[1],
        carry_intermediario,
        soma[1],
        carry
    )

    return instances()


@block
def adder(x, y, soma, carry):
    """Somador generico para vetores de mesmo tamanho.

    Implementacao esperada por ripple-carry (encadeamento de carries)
    usando celulas de full adder.

    Args:
        x: Vetor de entrada.
        y: Vetor de entrada.
        soma: Vetor de saida com mesma largura de x/y.
        carry: Carry de saida mais significativo.
    """
    return instances()


@block
def addervb(x, y, soma, carry):
    """Somador vetorial em estilo comportamental.

    Versao combinacional que pode usar operacoes aritmeticas diretas
    sobre os vetores para gerar soma e carry.

    Args:
        x: Vetor de entrada.
        y: Vetor de entrada.
        soma: Vetor de saida.
        carry: Carry de saida.
    """
    @always_comb
    def comb():
        pass

    return instances()
