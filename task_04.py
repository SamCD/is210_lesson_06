#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generates password cracks"""

import data
SALT = 'monosodium-glutamate'


def test_passwords(listobj):
    """Weeds out bad passwords"""
    cracked = []
    for account in listobj:
        aparts = account.split(':')
        passwd = crack_it(aparts[1])
        if passwd:
            cracked.append((aparts[0], passwd))

    return cracked


def crack_it(pwdhash):
    """Cracking"""
    retval = False
    for word in data.WORDS:
        crypted = data.crypt(word, SALT)
        if pwdhash == crypted:
            retval = word
            break
    return retval


def report(listtup):
    """Generates report of bad passwords"""
    rept = 'Cracked passwords\n' + ('-' * 50) + '\n'
    userline = '{0} {1}\n'
    for user in listtup:
        rept += userline.format(user[0], user[1])

    return rept
