#!/usr/bin/python

"""
Sum Function
"""

import random
import string

def RandomPasswordGenerator(passLen=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''

    for i in range(passLen):
        password += random.choice(characters)

    return password