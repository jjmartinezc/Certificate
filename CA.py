# -*- coding: utf-8 -*-
"""
CA Implicit Certificate EC
"""

import datetime
from fastecdsa.point import Point
from fastecdsa import keys, curve, ecdsa
from fastecdsa.keys import export_key, gen_keypair
from fastecdsa.keys import import_key
import random

def setCurve(a):

    if a == 0: 
        curva = curve.P192
    if a == 1: 
        curva = curve.P224
    if a == 2: 
        curva = curve.P256
    if a == 3: 
        curva = curve.P384
    if a == 4: 
        curva = curve.P521
    if a == 5: 
        curva = curve.secp192k1
    if a == 6: 
        curva = curve.secp224k1
    if a == 7: 
        curva = curve.secp256k1
    
    timeInit = datetime.datetime.now()
    
    #Parametros de la curva
    n = curva.p
    d = curva.G
    q = random.randint(1,n)
    
    #Id del dispositivo
    disp = "DispositivoA"
    
    #Estado o provincia del dispositivo
    state = "Bogota"
    
    #Ciudad del dispositivo
    city = "Bogota"
    
    #Organizacion del dispositivo
    org = "Uniandes"
    
    #Dominio del dispositivo
    dom = "Uniandes.edu.co"
    
    # Dispositivo A genera punto R
    priv_keyA, pub_keyA = keys.gen_keypair(curva)
    R = Point(pub_keyA.x, pub_keyA.y, curva)
    
    # Llave del CA
    priv_keyCA, pub_keyCA = keys.gen_keypair(curva)
    
    #CA genera un entero q
    Q = d * q

    # Suma Q + R
    D = Q + R
    
    #Fecha de expedicion del certificado
    expedicion = datetime.datetime.utcnow()

    # Fecha de expiracion del certificado
    expiracion=datetime.datetime.utcnow() + datetime.timedelta(days=30)
    
    #Se genera el certificado implicito (IC)
    IC = disp+"-"+state+"-"+city+"-"+org+"-"+dom+"-"+str(D)+"-"+str(expedicion)+"-"+str(expiracion)
    hIC = hash(IC)
    
    #Se genera la implicit signature a partir de la cual A construye su llave privada
    s = (hIC*q)+priv_keyCA
    
    timeFin = datetime.datetime.now()
    time = timeFin - timeInit
    string = str(time)+" - "+curva.name
    print(string)
    return string
    
    

    
    