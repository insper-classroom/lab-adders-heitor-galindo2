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
        carry.next = s[1] or s[2]

    return instances()


from myhdl import block, Signal, instances

@block
def adder2bits(x, y, soma, carry):

    carry_intermediario = Signal(bool(0))

    ha = halfAdder(
        x[0],
        y[0],
        soma[0],
        carry_intermediario
    )

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

    n = len(x)

    faList = [None for i in range(n)]
    c = [Signal(bool(0)) for i in range(n+1)]

    for i in range(n):
        faList[i] = fullAdder(x[i], y[i], c[i], soma[i], c[i+1])

    @always_comb
    def comb():
        carry.next = c[n]

    return instances()


@block
def addervb(x, y, soma, carry):

    @always_comb
    def comb():
        resultado = x + y

        n = len(soma)

        soma.next = resultado & ((1 << n) - 1)
        carry.next = resultado >> n
    
    return instances()