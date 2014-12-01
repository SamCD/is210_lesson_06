#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Makes lists of odd and/or even numbers"""


def evens_and_odds(numbers, show_even=True):
    """Shows either even or odd members of a list"""
    odds = []
    evens = []
    for i in numbers:
        if i % 2 == 1:
            odds.append(i)
        else:
            evens.append(i)
    if show_even is True:
        return evens
    else:
        return odds
