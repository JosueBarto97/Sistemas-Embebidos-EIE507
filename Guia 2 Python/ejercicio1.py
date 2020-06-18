# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 17:55:04 2020

@author: Sebastian
"""

varA=10
varB=30
if type(varA)==str or type(varB)==str:
    print('string involucrado')
elif varB>varA:
    print('mas pequeño')
elif varB<varA:
    print('mas grandre')
elif varB == varA:
    print('igual')
