import requests
import os
if "data_brevet.csv" not in os.listdir():
    file = open("data_brevet.csv",'w')
    file.write("Nom,Prénom,Mention,Homonyme")
    file.close()
file = open("data_brevet.csv",'r')
tableau = file.read().split('\n')
file.close()

if tableau[-1].split(",")[0] == "Nom":
    nombre = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
else :
    nom = tableau[-1].split(",")[0].lower()
    nombre = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    index = 0
    for i in nom:
        p = 0
        for l in list("abcdefghijklmnopqrstuvwxyz "):
            if l == i:
                nombre[index] = p
            p += 1
        index += 1

ltt = list("abcdefghijklmnopqrstuvwxyz ")
lettre = []
for i in ltt :
  lettre.append(i)

t = 0
while True:
    nb = nombre[0]
    nombre[0] = nb + 1
    for i in nombre:
        if len(lettre) in nombre:
            tour = 0
            for n in nombre:
                if int(n) == int(len(lettre)):
                    changement = tour
                tour = tour + 1
            nombre[changement] = 0
            target = changement + 1
            nb = nombre[target]
            nombre[target] = int(nb) + 1

    position = 0
    total = len(nombre) - 1
    final = []
    while position < total:
        if int(nombre[position]) != -1:
            po = int(nombre[position])
            lf = lettre[po]
            final.append(str(lf))
        position = position + 1
    mot = ''.join(final)

    #Rechere le nom
    r = requests.get(f'https://cyclades.ac-nancy-metz.fr/publication_A12/publication?filtre={mot}&contexte=eyJjb2RlRG9tYWluZSI6IkROQiIsImNvZGVFbnRpdGVSZXNwb25zYWJsZSI6IkExMiIsImNvZGVTZXNzaW9uIjoiMjAyMTpCOkROQi0yLjMiLCJjb2RlR3JvdXBlRGVjaXNpb24iOiIxIiwiY29kZVF1YWxpZmljYXRpb24iOm51bGwsImNvZGVDb250ZXh0ZVJlZ2xlbWVudGFpcmUiOm51bGwsImNvZGVab25lR2VvZ3JhcGhpcXVlIjpudWxsfQ%3D%3D&_=1625845265472')
    page = r.text
    if page == '{"results":[ ]}': 
        print('None',end='\r')
    else :
        ls = page.split('{')
        ls = "}".join(ls).split('}')
        del ls[0]
        del ls[0]
        del ls[-1]
        ls = "' , '".join(ls).split("' , '")
        l = ls.copy()
        ls = []
        for i in l:
            if i != "":
                ls.append(i)
        for candidat in ls:
            try :
                l = candidat.split('"nom" : ')
                del l[0]
                l = "".join(l).split('"')
                name = l[1]
                prenom = l[5]
                result = l[9]
                homonyme = l[12]
                file = open("data_brevet.csv",'r')
                tableau = file.read().split('\n')
                file.close()
                m = f"{name},{prenom},{result},{homonyme}"
                if m not in tableau:
                    tableau.append(f"{name},{prenom},{result},{homonyme}")
                    file = open("data_brevet.csv",'w')
                    file.write("\n".join(tableau))
                    file.close()
                    print(f"{name},{prenom},{result},{homonyme}")
                else :
                    print(f"{name},{prenom},{result},{homonyme}  <- ALREADY HERE")
            except :
                print(candidat,end='\r')
    t += 1
