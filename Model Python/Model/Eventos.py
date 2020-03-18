#!/usr/bin/python
#-*- coding: utf-8 -*-

from Sequia import Sequia
from Ataque barbaro import Ataque barbaro
from Falsos profetas import Falsos profetas
from Peste import Peste
from Revuelta callejera import Revuelta callejera
from Recaudación import Recaudación

class Eventos(Sequia, Ataque barbaro, Falsos profetas, Peste, Revuelta callejera, Recaudación):
    def __init__(self):
        self.AlegriaCiudadanos = None

