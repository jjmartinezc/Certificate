#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Certificate X509
"""

import datetime
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa

def cert():


    timeInit = datetime.datetime.now()
    
    #Se genera la llave RSA
    key = rsa.generate_private_key(
            
            public_exponent=65537,
            key_size=2048,
            
            )
    
    subject = issuer = x509.Name([
            
            #Datos del certificado
            x509.NameAttribute(NameOID.COUNTRY_NAME, u"CO"),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Bogota"),
            x509.NameAttribute(NameOID.LOCALITY_NAME, u"Bogota"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Company"),
            x509.NameAttribute(NameOID.COMMON_NAME, u"mysite.com"),
            
            ])
    
    cert = x509.CertificateBuilder().subject_name(
            
            subject
            
    ).issuer_name(
            
            issuer
            
    ).public_key(
            #Llave publica
            key.public_key()
            
    ).serial_number(
            #Serial del certificado
            x509.random_serial_number()
            
    ).not_valid_before(
            
            #Fecha de expedicion del certificado
            datetime.datetime.utcnow()
            
    ).not_valid_after(
            
            # Fecha de expiracion del certificado
            datetime.datetime.utcnow() + datetime.timedelta(days=30)
            
    ).add_extension(
            
            x509.SubjectAlternativeName([x509.DNSName(u"localhost")]),
            critical=False,
            
    ).sign(key, hashes.SHA256())
    
    
    timeFin = datetime.datetime.now()
    time = timeFin - timeInit
    string = str(time)+" - X.509"
    print(string)
    return string
    
    
    