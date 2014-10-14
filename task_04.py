#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generates password cracks"""

import data
SALT = 'monosodium-glutamate'
def test_passwords(users):

    """
    Weeds out bad passwords"""

    cracked_pws = []
    for i in users:
        pws = [users[i].split(':')[0], users[i].split(':')[4]]
        cracked = crack_it(pws)
        if cracked:
            cracked_pws.append(users[i].split(':')[0], users[i].split(':')[4])
            users = cracked_pws
        return users

def crack_it(pws):

    """
    Tests passwords against a words database"""
    
    words = test_passwords(pws)
    users = ''
    for i in data.WORDS:
        bad = data.crypt(data.WORDS[i], SALT)
        if bad[1] in words:
            users = bad
        return users

def report(users):
    """Generates report of bad passwords"""
    print "Cracked passwords\n--------\n{0}".format(test_passwords(users))
