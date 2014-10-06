#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generates password cracks"""

import data
SALT = 'monosodium-glutamate'
def test_passwords(users):
    for i in range(0, len(users)):
        cracked_pws = []
        pws = [users[i].split(':')[0], users[i].split(':')[1]]
        cracked = crack_it(pws)
        if cracked:
            cracked_pws.append(users[i].split(':')[0], users[i].split(':')[1])
            users = cracked_pws
        return users

def crack_it(pws):
    words = test_passwords(pws)
    users = ()
    for i in range(0, len(data.WORDS)):
        x = data.crypt(data.WORDS[i], SALT)
        if x[1] in words:
            users.append([x])
        return users

def report(users):
    print "Cracked passwords\n-------------\n{0}".format(test_passwords(data.WORDS))