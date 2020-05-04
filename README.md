# Crear jeràrquia de directoris i arxius donat un CSV (curs 2016/2017)

![](https://cdn.memegenerator.es/imagenes/memes/full/18/1/18012436.jpg)

L'institut us ha contractat perquè tracteu les dades de matrícula del curs.

Per això us passen un fitxer amb les dades de l'alumnat matriculat, està en format [CSV](https://ca.wikipedia.org/wiki/CSV).


## Exercici 1 - Configuració. 

Preguntar pels directoris de treball:

- on està guardat el fitxer de matrícula, el fitxer alumnes.csv.
- on es volen guardar les llistes dels grups.
- on es vol que es guardi passar llista.

S'ha de comprovar que siguin directoris. Vegeu aquest codi com ho fa:

```python3
import os

fpath = '/workspace/python/'
if (os.path.isdir(fpath)):
    print("És directori")
else:
    print("No és directori")
```
Heu d'adaptar el codi anterior fins que l'usuari no entri correctament els directoris.

## Exercici 2 - Crear les llistes de classe de cada curs. 

No es podrà accedir en aquesta llista si en la configuració no s'ha indicat:
- quin és el directori on està l'arxiu de matricula.
- on es guarden els arxius d'assistència.

Les llistes de curs han de contenir:

- nom
- email
- mòbil

S'ha de crear la llista d'alumnes de cada grup, segons l'edat:
- Si l'alumne té 11 o 12 anys s'afegeix a un arxiu anomenat ESO1.csv.
- Si l'alumne té 13  anys s'afegeix a un arxiu anomenat ESO2.csv
- Si l'alumne té 14 anys s'afegeix a un arxiu anomenat ESO3.csv
- Si l'alumne té 15 anys s'afegeix a un arxiu anomenat ESO4.csv
- Si l'alumne té 16 anys s'afegeix a un arxiu anomenat BAT1.csv
- Si l'alumne té 17 o 18 anys s'afegeix a un arxiu anomenat BAT2.csv

Per llegir l'arxiu alumnat heu de quedar-vos amb els valors que necessiteu del fitxer alumnat.csv . Penseu:
- que els diferents valors es separen per ,
- que la primera línia només és la capçalera i no interessa.

## Exercici 3 - Passar llista

No es podrà accedir en aquesta llista si en la configuració no s'ha indicat:
- quin és el directori on està l'arxiu de matricula.
- on es guarden els arxius d'assistència.
- on es guarda el registre de la llista.

Per passar llista haureu de seguir aquest fluxe:

- demanar quin curs es vol passar llista
- mostra nom a nom (línia a línia) de l'alumnat. 
- després de mostrar el nom haureu de demanar si l'alumne:
  - ha assistit (marqui 1)
  - no ha assisit (marqui 0)
- si l'usuari no entra 1 o 0. Se li torna a demanar que marqui correctament l'assistència.
- un cop marcada assistència, registrar-la en un arxiu. El nom de l'arxiu ha de ser curs+dataavui.txt . Per exemple passo avui llista a ESO1 el fitxer de la llista serà: **ESO12020-05-04.txt**

Aquí veieu com podeu obtenir la data actual.
```python3=
from datetime import date

#dia actual
today = date.today()
print(today)
```
- a l'arxiu s'ha de guardar un registre (en el cas que hagi assistit)
```text=
Muñoz Carbó. Miguel - 1
```

## Exercici 4 - Consultar assistència

En aquesta opció el professorat vol consultar l'assistència d'un dia. Per fer-ho mostrareu tots els arxius registrats de passar llista, el professorat tria un nom i se li mostra l'assistència d'aquell dia.         

Heu de mostrar nom a nom de l'alumne i posar Falta! en el cas que s'hagi registrat un 0.

Mireu exemple:
- arxiu registrat
```text=
Muñoz Carbó. Miguel - 1
Alegría García. Pilar 0
```
- mostreu per consola
```text=
Muñoz Carbó. Miguel 
Alegría García. Pilar Falta!
``` 

