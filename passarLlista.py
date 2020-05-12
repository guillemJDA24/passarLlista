import os
from datetime import date

directoriMatricula="matricula"
directoriAssistencia="assistencia"
directoriGrups="grups"

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
      directoriGrups=input('a quin directori guardas grups.csv')
    while os.path.isdir(directoriAssistencia)!= True:
      directoriAssistencia=input('a quin directori guardas asistencia.csv')


  elif (opcioMenu == 2):
    eso1 = open(directoriGrups +"/eso1.csv","w")
    eso2 = open(directoriGrups +"/eso2.csv","w")
    eso3 = open(directoriGrups +"/eso3.csv","w")
    eso4 = open(directoriGrups +"/eso4.csv","w")
    bat1 = open(directoriGrups +"/bat1.csv","w")
    bat2 = open(directoriGrups +"/bat2.csv","w")
    fitxer=open(directoriMatricula +"/alumnat.csv","r")
    
    linea=fitxer.readline()
    for i in fitxer:
      alumne=i.split(',')
      ##TODO Pot una laumne tenir dos edats a la vegada?
      if (alumne[1] == '11'):
        eso1.write(alumne[0] +"," + alumne[2] + ','+alumne[5]  )
      elif (alumne[1] =='12') :
        eso1.write(alumne[0] +','+ alumne[2] + ','+alumne[5]  )
      elif (alumne[1] =='13'):
        eso2.write(alumne[0] + ','+alumne[2] +','+ alumne[5]  )
      elif (alumne[1] =='14'):
        eso3.write(alumne[0] + ','+alumne[2] + ','+alumne[5]  )
      elif (alumne[1] =='15'):
        eso4.write(alumne[0] +','+ alumne[2] + ','+alumne[5]  )
      elif (alumne[1] =='16'):
        bat1.write(alumne[0] + ','+alumne[2] +','+ alumne[5]  )
      ##TODO Pot una laumne tenir dos edats a la vegada?  
      elif (alumne[1] =='17'):
        bat2.write(alumne[0] +','+ alumne[2] + ','+alumne[5]  )
      elif (alumne[1]=='18'):
        bat2.write(alumne[0] +','+ alumne[2] + ','+alumne[5]  )
    eso1.close()
    eso2.close()
    eso3.close()
    eso4.close()
    bat1.close()
    bat2.close()

  if (opcioMenu == 3):
    eso1 = open(directoriGrups +"/eso1.csv","r")
    eso2 = open(directoriGrups +"/eso2.csv","r")
    eso3 = open(directoriGrups +"/eso3.csv","r")
    eso4 = open(directoriGrups +"/eso4.csv","r")
    bat1 = open(directoriGrups +"/bat1.csv","r")
    bat2 = open(directoriGrups +"/bat2.csv","r")
    curs = input('quin curs vols pasar llista')
    dia=date.today()
    if (curs =='eso1'):
      eso1asis=open(directoriAssistencia+'/eso1_'+str(dia)+'.csv','w')
      for n in eso1:
        alumne = n.split(',')
        print(alumne[0])
        asis=input('esta alumne 1=si 0=no')
        if asis == '1':
          eso1asis.write(' '+alumne[0]+'-1')
        elif (asis == '0'):
          eso1asis.write(' '+alumne[0]+'-0')
      eso1asis.close()   
        

          
           

      #Obrir tots elsarxius per escriptura
    #Bucle sobre arxiu matricula
      #Agafar camps separats per ","
      #Segons edat escriure arxiu on toca
      #A l'arxiu escriure nom, email i telèfon
    #Tancar
print("Adéu bon dia tinguis!")
