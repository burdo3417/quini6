import urllib2
from bs4 import BeautifulSoup
import ssl
import sys

ssl._create_default_https_context = ssl._create_unverified_context


import urllib2
from bs4 import BeautifulSoup


print "--------------------------------------------------"
print("")
print("Bienvenido/a. Le deseamos mucha suerte")
print("")
print("")

print "Ingrese 1 para jugada Completa. Participa en todos los sorteos."
print "Ingrese 2 para jugada Media. Participa en sorteos Tradicional, Segunda y Revancha."
print "Ingrese 3 para jugada Simple. Participa en sorteos Tradicional y Segunda."
print("")
opcion_jugada = int(input("Ingrese su opcion: "))
while opcion_jugada >3 or opcion_jugada < 1:
    print("Debe ingresar un numero entre 1 y 3")
    opcion_jugada = int(input("Ingrese su opcion: "))


print("")
print("")


nro1 = int(input("Ingrese su primer nro: "))
while nro1 >45:
    print("Debe ingresar un numero entre 0 y 45")
    nro1 = int(input("Ingrese su primer nro: "))

nro2 = int(input("Ingrese su segundo nro: "))
while nro2 >45 or nro2 == nro1:
    print("Debe ingresar un numero entre 0 y 45 y no repetido")
    nro2 = int(input("Ingrese su segundo nro: "))

nro3 = int(input("Ingrese su tercer nro: "))
while nro3 >45 or nro3 == nro1 or nro3 == nro2:
    print("Debe ingresar un numero entre 0 y 45 y no repetido")
    nro3 = int(input("Ingrese su tercer nro: "))

nro4 = int(input("Ingrese su cuarto nro: "))
while nro4 >45 or nro4 == nro3 or nro4 == nro2 or nro4 == nro1:
    print("Debe ingresar un numero entre 0 y 45 y no repetido")
    nro4 = int(input("Ingrese su cuarto nro: "))

nro5 = int(input("Ingrese su quinto nro: "))
while nro5 >45 or nro5 == nro4 or nro5 == nro3 or nro5 == nro2 or nro5 == nro1:
    print("Debe ingresar un numero entre 0 y 45 y no repetido")
    nro5 = int(input("Ingrese su quinto nro: "))

nro6 = int(input("Ingrese su sexto nro: "))
while nro6 >45 or nro6 == nro5 or nro6 == nro4 or nro6 == nro3 or nro6 == nro2 or nro6 == nro1:
    print("Debe ingresar un numero entre 0 y 45 y no repetido")
    nro6 = int(input("Ingrese su sexto nro: "))



jugados_list = []
jugados_list.append(nro1)
jugados_list.append(nro2)
jugados_list.append(nro3)
jugados_list.append(nro4)
jugados_list.append(nro5)
jugados_list.append(nro6)

jugados_list.sort(key=int)

print("")
print("")

print "--------------------------------------------------"
print("Sus numeros jugados son: ")
print(jugados_list)
print "--------------------------------------------------"
print("")
print("")
print("")


quote_page = "https://www.quini-6-resultados.com.ar/"

page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, "html.parser")

todos = str(soup.findAll(attrs={"class":"nro"}))
todos_nros = str(filter(str.isdigit, todos))

date = soup.find(name=None, attrs={"class":"lead"}, recursive=True, text=None, kwargs='')
date = date.text.strip()
date = date.encode("utf-8")


result_tradicional = soup.findAll(name=None, attrs={"class":"sorteo"}, recursive=True, text=None, limit=None, kwargs='')[4].findNext(name=None, attrs={}, text=None, kwargs='')
result_tradicional = str(result_tradicional.text.strip())
result_tradicional = result_tradicional[1:]
result_tradicional = result_tradicional.replace("$","  $")



result_lasegunda = soup.findAll(name=None, attrs={"class":"sorteo"}, recursive=True, text=None, limit=None, kwargs='')[5].findNext(name=None, attrs={}, text=None, kwargs='')
result_lasegunda = str(result_lasegunda.text.strip())
result_lasegunda = result_lasegunda[1:]
result_lasegunda = result_lasegunda.replace("$","  $")


result_revancha = soup.findAll(name=None, attrs={"class":"sorteo"}, recursive=True, text=None, limit=None, kwargs='')[6].findNext(name=None, attrs={}, text=None, kwargs='')
result_revancha = str(result_revancha.text.strip())
result_revancha = result_revancha[1:]
result_revancha = result_revancha.replace("$","  $")


result_siempresale = soup.findAll(name=None, attrs={"class":"sorteo"}, recursive=True, text=None, limit=None, kwargs='')[7].findNext(name=None, attrs={}, text=None, kwargs='')
result_siempresale = str(result_siempresale.text.strip())
result_siempresale = result_siempresale[1:]
result_siempresale = result_siempresale.replace("$","  $")


result_extra = soup.findAll(name=None, attrs={"class":"sorteo"}, recursive=True, text=None, limit=None, kwargs='')[8].findNext(name=None, attrs={}, text=None, kwargs='')
result_extra = str(result_extra.text.strip())
result_extra = result_extra[1:]
result_extra = result_extra.replace("$","  $")


print (date)

print("")
print("")


tradicional_list = []
lasegunda_list = []
revancha_list = []
siempresale_list = []
extra_list = []

for i in range(0,12,2):
    tradicional_list.append(int(todos_nros[i]+todos_nros[i+1]))
for i in range(12,24,2):
    lasegunda_list.append(int(todos_nros[i]+todos_nros[i+1]))
for i in range(24,36,2):
    revancha_list.append(int(todos_nros[i]+todos_nros[i+1]))
for i in range(36,48,2):
    siempresale_list.append(int(todos_nros[i]+todos_nros[i+1]))




aciertos_tradicional = 0
aciertos_segunda = 0
aciertos_revancha = 0
aciertos_siempresale = 0
aciertos_extra = 0

for i in jugados_list:
    for i2 in tradicional_list:
        if i == i2:
            aciertos_tradicional += 1


for i in jugados_list:
    for i2 in lasegunda_list:
        if i == i2:
            aciertos_segunda += 1


for i in jugados_list:
    for i2 in revancha_list:
        if i == i2:
            aciertos_revancha += 1


for i in jugados_list:
    for i2 in siempresale_list:
        if i == i2:
            aciertos_siempresale += 1



for i in range (0,6):
    extra_list.append(tradicional_list[i])
for i in range (0,6):
    extra_list.append(lasegunda_list[i])
for i in range (0,6):
    extra_list.append(revancha_list[i])

extrafinal_list = []
def Remove(duplicate): 
     
    for num in duplicate: 
        if num not in extrafinal_list: 
            extrafinal_list.append(num) 
    return extrafinal_list 

Remove(extra_list)

extrafinal_list.sort(key=int)



for i in jugados_list:
    for i2 in extrafinal_list:
        if i == i2:
            aciertos_extra += 1


if opcion_jugada == 1:

    print("Los resultados para el Sorteo Tradicional son: " )
    print(tradicional_list)
    print(result_tradicional)
    print "Ud obtuvo ", aciertos_tradicional," aciertos"
    if aciertos_tradicional > 3:
        print("Ud ha ganado un premio. Consulte a su agencia de Loteria")
    else:
        print "No tiene premio"
    print("")
    print("")
    raw_input("Presione Enter para continuar")
    print("")
    print "--------------------------------------------------"

    print("Los resultados para el Sorteo de La Segunda son: ")
    print(lasegunda_list)
    print(result_lasegunda)
    print "Ud obtuvo ", aciertos_segunda," aciertos"
    if aciertos_segunda > 3:
        print("Ud ha ganado un premio. Consulte a su agencia de Loteria")
    else:
        print "No tiene premio"
    print("")
    print("")
    raw_input("Presione Enter para continuar")
    print("")
    print "--------------------------------------------------"

    print("Los resultados para el Sorteo Revancha son: ")
    print(revancha_list)
    print(result_revancha)
    print "Ud obtuvo ", aciertos_revancha," aciertos"
    if aciertos_revancha > 5:
        print("Ud ha ganado un premio. Consulte a su agencia de Loteria")
    else:
        print "No tiene premio"
    print("")
    print("")
    raw_input("Presione Enter para continuar")
    print("")
    print "--------------------------------------------------"

    print("Los resultados para el Sorteo Siempre Sale son: ")
    print(siempresale_list)
    print(result_siempresale)
    print "Ud obtuvo ", aciertos_siempresale," aciertos"
    if aciertos_siempresale > 3:
        print "Puede tener un premio. Consulte a su agencia de Loteria"
    else:
        print "No tiene premio"
    print("")
    print("")
    raw_input("Presione Enter para continuar")
    print("")
    print "--------------------------------------------------"

    print("Los resultados para el Sorteo Extra son: ")
    print(extrafinal_list)
    print(result_extra)
    print "Ud obtuvo ", aciertos_extra," aciertos"
    if aciertos_siempresale > 5:
        print "Ud ha ganado un premio. Consulte a su agencia de Loteria"
    else:
        print "No tiene premio"
    print("")
    print("")
    raw_input("Presione Enter para continuar")
    print("")
    print "--------------------------------------------------"

elif opcion_jugada == 2:
    print("Los resultados para el Sorteo Tradicional son: " )
    print(tradicional_list)
    print(result_tradicional)
    print "Ud obtuvo ", aciertos_tradicional," aciertos"
    if aciertos_tradicional > 3:
        print("Ud ha ganado un premio. Consulte a su agencia de Loteria")
    else:
        print "No tiene premio"
    print("")
    print("")
    raw_input("Presione Enter para continuar")
    print("")
    print "--------------------------------------------------"

    print("Los resultados para el Sorteo de La Segunda son: ")
    print(lasegunda_list)
    print(result_lasegunda)
    print "Ud obtuvo ", aciertos_segunda," aciertos"
    if aciertos_segunda > 3:
        print("Ud ha ganado un premio. Consulte a su agencia de Loteria")
    else:
        print "No tiene premio"
    print("")
    print("")
    raw_input("Presione Enter para continuar")
    print("")
    print "--------------------------------------------------"

    print("Los resultados para el Sorteo Revancha son: ")
    print(revancha_list)
    print(result_revancha)
    print "Ud obtuvo ", aciertos_revancha," aciertos"
    if aciertos_revancha > 5:
        print("Ud ha ganado un premio. Consulte a su agencia de Loteria")
    else:
        print "No tiene premio"
    print("")
    print("")
    raw_input("Presione Enter para continuar")
    print("")
    print "--------------------------------------------------"


else:
    print("Los resultados para el Sorteo Tradicional son: " )
    print(tradicional_list)
    print(result_tradicional)
    print "Ud obtuvo ", aciertos_tradicional," aciertos"
    if aciertos_tradicional > 3:
        print("Ud ha ganado un premio. Consulte a su agencia de Loteria")
    else:
        print "No tiene premio"
    print("")
    print("")
    raw_input("Presione Enter para continuar")
    print("")
    print "--------------------------------------------------"

    print("Los resultados para el Sorteo de La Segunda son: ")
    print(lasegunda_list)
    print(result_lasegunda)
    print "Ud obtuvo ", aciertos_segunda," aciertos"
    if aciertos_segunda > 3:
        print("Ud ha ganado un premio. Consulte a su agencia de Loteria")
    else:
        print "No tiene premio"
    print("")
    print("")
    raw_input("Presione Enter para continuar")
    print("")
    print "--------------------------------------------------"










