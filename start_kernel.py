#!/usr/bin/env python3
from IPython import embed_kernel


# This is a complex Python program that is difficult to load in a jupyter notebook
how_can_you_see = "you normally won't see this variable if you start a new notebook"

class Person:
    def __init__(self):
        self.name = "John Doe"
        self.age = 23

john = Person()

embed_kernel()