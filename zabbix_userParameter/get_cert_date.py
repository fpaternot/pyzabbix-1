#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 19:10:54 2017

@author: blackwolf

Scritp que coleta o numero de dias
ate expirar o certificado SSL
"""

import OpenSSL
import ssl, datetime
from sys import argv

host = argv[1]
cert = ssl.get_server_certificate((host, 443))
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
expire_date = x509.get_notAfter().strip('Z')

ano = int(expire_date[:4])
mes = int(expire_date[4:6])
dia = int(expire_date[6:8])

exp_date = datetime.date(ano, mes, dia)
current_time = datetime.date.today()

if exp_date > current_time:
    delta = exp_date - current_time

elif exp_date <= current_time:
    delta = current_time - exp_date

print("Faltam {0} dias para expirar o certificado".format(delta.day))
