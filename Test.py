#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Implicit Certificate CE & X509
"""
import X509
import CA
file = open("./data.txt", "w")
for i in range(0,8):
    for j in range(0,1000):
        n = i % 8
        file.write(CA.setCurve(n)+'\n')

for x in range(0,1000):
    file.write(X509.cert()+'\n')