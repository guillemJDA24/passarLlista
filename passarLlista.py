import os
from datetime import date

directoriMatricula=""
directoriAssistencia=""
directoriGrups=""

opcioMenu =0
while (opcioMenu !=5):
  print("1- Configurar sistema")
  print("2- Fer fulls de grup")
  print("3- Passa llista")
  print("4- Consultar assistència")
  print("5- Sortir")
  opcioMenu = int(input("Quina opció vols?"))
  if  (opcioMenu==1):
    while os.path.isdir(directoriMatricula)!= True:
      directoriMatricula=input('a quin directori guardas alumnat.csv')
    while os.path.isdir(directoriGrups)!= True:
      directoriGrups=input('a quin directori guardas grups.csv)
    while os.path.isdir(directoriAssistencia)!= True:
      directoriAssistencia=input('a quin directori guardas asistencia.csv)
  elif (opcioMenu == 2):
    eso1 = open(directoriGrups +"/eso1.csv","w")
    eso2 = open(directoriGrups +"/eso2.csv","w")
    eso3 = open(directoriGrups +"/eso3.csv","w")
    eso4 = open(directoriGrups +"/eso4.csv","w")
    bat1 = open(directoriGrups +"/bat1.csv","w")
    bat2 = open(directoriGrups +"/bat2.csv","w")
    fitxer=open(directoriMatricula +"/alumnat.csv','r')
    
    linea=fitxer.readline()
    for i in fitxer:
      alumne=i.split(',')
      if (alumne[1] ==11) and (alumne[1]==12):
        eso1.write(alumne[0])
      elif (alumne[1] ==13):
        eso2.write(i)
    
    #Obrir tots elsarxius per escriptura
    #Bucle sobre arxiu matricula
      #Agafar camps separats per ","
      #Segons edat escriure arxiu on toca
      #A l'arxiu escriure nom, email i telèfon
    #Tancar
print("Adéu bon dia tinguis!")
