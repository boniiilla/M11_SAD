#!/usr/bin/python3
import base64
fitxer = open("missatgecodificat.txt", "r")
contingut= fitxer.read()
num = int(input("Indica el nombre de cops a fer:"))
for i in range(1,num+1):
     contingut=base64.b64decode(contingut)
     print(contingut)