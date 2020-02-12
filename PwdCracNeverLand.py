#Codigo escrito para resolver el desafio password_crack del NeverLAN CTF 2020 
#Escrito por srbleu en el acto

import hashlib

colores =["blue","red","pink","rose","brown","black","white","grey","yellow","purple","violet","orange","silver","gold","magenta","tan","cyan","olive","maroon","navy","aquamarine","turquoise","lime","teal","indigo","gray"]
teammember = ["s7a73farm","bashninja","zestyfe","durkinza","purvesta","n30","viking"]

for year in range (0,2020):
    for color in colores:
        for member in teammember:
            result = hashlib.md5(str.encode("{0}-{1}-{2}".format(color,year,member)))
            result = result.hexdigest()
            if (result == "267530778aa6585019c98985eeda255f"):
                print("{0}-{1}-{2}".format(color,year,member))
