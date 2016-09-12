#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

FLEMISH = inquisition.SPANISH

Random_word = 'Spanish'

length_word = len(Random_word)

finding = inquisition.SPANISH.index('Spanish')

Variable_1 = FLEMISH[:finding]

Variable_2 = FLEMISH[finding + length_word:]

FLEMISH = Variable_1 + 'Flemish' + Variable_2

print FLEMISH
