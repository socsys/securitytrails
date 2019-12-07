# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 14:46:40 2019

@author: k1759874
"""

import requests
from bs4 import BeautifulSoup
for i in range (1,74):
    fr = open('D:/Research Paper/paper5 cnamecloaking/json/'+str(i)+'.txt', 'w')
    
    
    url = "https://api.securitytrails.com/v1/domains/list"
    
    querystring = {"apikey":"","page":str(i)}
    
    payload = "{\"filter\":{\"cname\":\"dnsdelegation.io\"}}"
    response = requests.request("POST", url, data=payload, params=querystring)
    
    
    print str(i)
    soup = BeautifulSoup(response.text, 'html.parser')
    fr.write(str(soup))
    fr.write('\n')
    fr.close()