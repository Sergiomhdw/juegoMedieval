#!/usr/bin/python
#-*- coding: utf-8 -*-

from Ciudadanos import Ciudadanos
from Compañia import Compañia

class Militares(Ciudadanos, Compañia):
    def __init__(self):
        self.Numero = None
        self.tipo = None

    def Luchan(self, ):
        pass

    def Mueren(self, ):
        pass

    def EstarArmado(self, ):
        pass

