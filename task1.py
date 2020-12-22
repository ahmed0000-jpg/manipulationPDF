import ftplib
import xlrd
import pandas as pd
import os
import shutil


FTP_HOST = "talend.ecolotrans.net"

FTP_USER = "talend"

FTP_PASS = "Rand069845"
# connect to the FTP server
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
# force UTF-8 encoding
ftp.encoding = "utf-8"

ftp.cwd('/Preprod/IN/POC_ON_DEMAND/INPUT/ClientInput')

clients = ftp.nlst()
print(clients)
for client in clients:
    path_racine = '/Preprod/IN/POC_ON_DEMAND/INPUT/ClientInput'
    path_client = path_racine + '/' + client
    ftp.cwd(path_client)
    print("success")
    liste_fichier_client = ftp.nlst(path_client)
    print(liste_fichier_client)
    if(len(liste_fichier_client) != 0):
        os.mkdir(client)
        for fichier in liste_fichier_client:
            file_name = fichier.split('/')[7]
            print(file_name)
            with open(file_name, "wb") as file:
                commande = "RETR " + file_name
                ftp.retrbinary(commande, file.write)
            shutil.move(file_name, client)