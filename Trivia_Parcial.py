# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 09:02:58 2021
@author: andre
"""
from tkinter import *
import random
 
ventana = Tk()
ventana.title('TRIVIA UTS' )
ventana.geometry("500x330")
 
preguntas=["En telecomunicaciones, TCP/IP es: \n A: Una variable \n B: Un protocolo de comunicación \n C: Un tipo de archivo \n D: Un programa",
"¿Como se le llama al almacenamiento usando internet? \n A: Almacenamiento en la nube \n B: Almacenamiento local \n C: Almacenamiento servidor \n D: Backup local",
"El numero binario 1001 en sistema decimal es: \n A: 2 \n B: 5 \n C: 3 \n D: 9",
"El formato .Doc hace referencia a: \n A: Una tabla de excel \n B: Un archivo de datos \n C: Un documento office \n D: Una base de datos",
"Alguna de estas opciones NO es una red social \n A: Facebook \n B: Instagram \n C: CCleaner \n D: Twiter",
"¿Cuál de los siguientes numeros EN PROGRAMACIÓN es Hexagesimal? \n A: 0b011 \n B: 0x20 \n C: 100 \n D: 3.18",
"¿Cuál de las siguientes opciones es un sistema operativo? \n A: Rapsbian \n B: LoRa \n C: Office \n D: C++",
"La comunicación RS232 se realiza: \n A: de manera serial \n B: de manera paralela \n C: de manera analoga \n D: ninguna de las anteriores",
"El termino 'se cayó la página' es: \n A: Se fue la luz \n B: Se cayó el computador \n C: No responde el servidor \n D: No quiere trabajar",
"La función print en phyton es para: \n A: Ejecutar la impresora \n B: Imprimir un archivo \n C: imprimir en la ventaja de ejecución \n D: printear la pantalla",
"EN PROGRAMACIÓN, si 2+2=4, 4+2=6, 6+0B10 es: \n A: 10 \n B: 0x08 \n C: 0B10 \n D: 1006",
"¿Cuál de las siguientes opciones permite cortar en un windows? \n A: CTRL+X \n B: CTRL+C \n C: CRTL+B \n D: CTRL+F4",
"¿Entre los servicios de la UTS no incluye \n A: Salud \n B: Emprendimiento \n C: Bienestar Universitario \n D: Biblioteca",
"¿Cuál es el primer proceso para usar los recursos de Bienestar en las UTS? \n A: Contactar al coordinador \n B: Inscribirse en las oficinas de bienestar \n C: No hay proceso, los recursos son libres \n D: Enviar correo a admisiones",
"¿En que año se realizaron las primeras pruebas de comunicación por internet? \n A: 1945 \n B: 1995 \n C: 1923 \n D: Ninguna de las anteriores",
"El término 'servidor' en telecomunicaciones es: \n A: Un dispositivo para almacenar datos \n B: Un dispositivo con sistema operativo y acceso remoto \n C: El comando de ayudas de windows \n D: Un pendrive",
"En telecomunicaciones, JAVA es: \n A: Junta Accionista de Valores Aleatorios \n B: Un lenguaje de programación \n C: Un software para leer archivos .DXF \n D: Un ejecutor de comandos de windows",
"Una muñeca vestida de azul, dicho color en formato RGB de 24bits sería: \n A: (0,0,255) \n B: (00FF00) \n C: 0X1800000 \n D: BLUE",
"Un procesador de doble núcleo permite: \n A: Hacer dos actividades a la vez \n B: Doble velocidad de procesamiento \n C: Doble velocidad de navegación \n D: Doble capacidad de almacenamiento",
"El término IP en telecomunicaciones es: \n A: Individual Protocol \n B: Interfaz de programación \n C: Interactive Protocol \n D: InterProcessing",
"En telecomunicaciones, Dirección MAC hace referencia a: \n A: Dirección de PC MACBOOK \n B: Identificación del dispositivo en la red \n C: Manual Active Computer \n D: Serial del fabricante",
"Almacenar en la nube hace referencia a: \n A: Volar una cometa \n B: Guardar archivo en servidores NO locales \n C: Enviar una carta \n D: El clima esta Nublado",
"El numero decimal 128 en sistema binario es: \n A: 100000000 \n B: 11111110 \n C: 11110011 \n D: 100010000",
"El formato .XLS hace referencia a: \n A: Un libro de excel \n B: Un documento de word \n C: Un ejecutable de windows \n D: Una URL",
"Alguna de estas opciones NO es un editor de texto \n A: Bloc de notas \n B: Worpad \n C: Word \n D: Google",
"¿Cuál de los siguientes numeros EN PROGRAMACIÓN es binario? \n A: 0B011 \n B: 0X20 \n C: 100 \n D: 3.18",
"¿Cuál de las siguientes opciones es un NO es un sistema operativo? \n A: Rapsbian \n B: LoRa \n C: Windows \n D: Linux",
"El comando CRTL+F4 sirve para: \n A: Abrir archivos .TXT \n B: Cerrar la ventana activa en windows \n C: Realizar una consulta en el buscador \n D: ninguna de las anteriores",
"El término 'no hay WIFI' es: \n A: No existe acceso a la red \n B: se acabó el WIFI \n C: No responde el computador \n D: No hay dinero",
"La función import en phyton es para: \n A: Darle importancia a un programa \n B: hacer un llamado de libreria \n C: imprimir en la ventaja de ejecución \n D: Borrar el programa",
"¿Cuál de las siguientes opciones permite copiar en un windows? \n A: CTRL+C \n B: CTRL+X \n C: CRTL+B \n D: CTRL+F4",
"La función while en phyton es para: \n A: ejecutar el programa \n B: Sumar variables \n C: Mantener encendido el computador \n D: hacer un ciclo repetitivo",
"¿No hace parte de la misión de la institución \n A: Sentido ético \n B: Pensamiento crítico \n C: Transformación social \n D: Actitud Emprendedora",
"¿Cuál es el primer proceso para usar matricularse en las UTS? \n A: Contactar al coordinador \n B: Inscribirse en las oficinas de bienestar \n C: No hay proceso, los recursos son libres \n D: Enviar correo a admisiones",
"¿Cuál fue la primera empresa en desarrollar un procesador? \n A: APPLE \n B: Microsoft \n C: IBM \n D: Ninguna de las anteriores",
"El término 'pendrive' en telecomunicaciones es: \n A: Un dispositivo para almacenar datos \n B: Un dispositivo con sistema operativo y acceso remoto \n C: El comando de ayudas de windows \n D: Un servidor",
"En telecomunicaciones, phyton es: \n A: Junta Accionista de Valores Aleatorios \n B: Un lenguaje de programación \n C: Un software para leer archivos .DXF \n D: Un ejecutor de comandos de windows",
"El término 'RAM' en telecomunicaciones es: \n A: Memoria de acceso aleatorio \n B: Memoria de solo lectura \n C: Memoria de lectura y escritura electrica \n D: Memoria principal de almacenamiento",
"El formato .exe hace referencia a: \n A: Un libro de excel \n B: Un documento de word \n C: Un ejecutable de windows \n D: Una URL",
"¿Cuál de las siguientes opciones permite pegar en un windows? \n A: CTRL+C \n B: CTRL+X \n C: CRTL+V \n D: CTRL+F4"]

respuestas=["B","A","D","C","C","B","A","A","C","C","B","A","B","B","D","B","B","A","A","B",
            "B","B","A","A","D","A","B","B","A","B","A","D","C","D","C","A","B","A","C","C"]
opciones=[]
conteo =0
def selecPre(preguntas):  
    global palabra
    palabra=random.randint(0,39)
    
    global conteo 
    if conteo<1:
        opciones.append(palabra)
    else:
        i=0
        while i<conteo:
            if palabra==opciones[i]:
                palabra=random.randint(0,39)
                i=0
            else:
                i=i+1
        opciones.append(palabra)
        
               
    label=Label(ventana, text=(preguntas[palabra]),justify=CENTER,width=70)
    label.grid(row=0,column=0,padx=5,pady=30,columnspan=3)
    label=Label(ventana, text="Respuestas:",justify=CENTER)
    label.grid(row=1,column=0,padx=2,pady=2,columnspan=3)
    
    
def botonA():
    print("Presiono A") 
    rta="A"
    if rta==respuestas[palabra]:
        label1=Label(ventana, text="                              " ,justify=CENTER)
        label1.grid(row=8,column=0,padx=2,pady=2,columnspan=3)
        print ("Muy Bien")
        rt=selecPre(preguntas)   
        boton3['state'] = NORMAL
        boton4['state'] = NORMAL
    else :
        print ("Fallaste")
        ventana.destroy()
    
def botonB():
    print("Presiono B") 
    rta="B"
    if rta==respuestas[palabra]:
        label1=Label(ventana, text="                              ",justify=CENTER)
        label1.grid(row=8,column=0,padx=2,pady=2,columnspan=3)
        print ("Muy Bien")
        selecPre(preguntas)
        rt=selecPre(preguntas)
        boton1['state'] = NORMAL
        boton4['state'] = NORMAL
    else :
        print ("Fallaste")
        ventana.destroy()
        

def botonC():
    print("Presiono C") 
    rta="C"
    if rta==respuestas[palabra]:
        label1=Label(ventana, text="                              ",justify=CENTER)
        label1.grid(row=8,column=0,padx=2,pady=2,columnspan=3)
        print ("Muy Bien")
        selecPre(preguntas)
        rt=selecPre(preguntas)
        boton2['state'] = NORMAL
        boton4['state'] = NORMAL
    else :
        print ("Fallaste")
        ventana.destroy()
       
def botonD():
    print("Presiono D") 
    rta="D"
    if rta==respuestas[palabra]:
       label1=Label(ventana, text="                              ",justify=CENTER)
       label1.grid(row=8,column=0,padx=2,pady=2,columnspan=3)
       print ("Muy Bien")
       selecPre(preguntas)
       rt=selecPre(preguntas)
       boton1['state'] = NORMAL
       boton2['state'] = NORMAL 
    else :
        print ("Fallaste")
        ventana.destroy()
        

def cambioPregunta():
    print("1 Ayuda") 
    rta=respuestas[palabra]
    if rta==respuestas[palabra]:
       label1=Label(ventana, text="La Respuesta es: " + rta,justify=CENTER)
       print ("Siguiente")
       selecPre(preguntas)
       botonA.destroy()
           
def ayudaAmigo():
    print("3 Ayuda") 
    rta=respuestas[palabra]
    label1=Label(ventana, text="La Respuesta es: " + rta ,state = NORMAL,justify=CENTER)
    label1.grid(row=8,column=0,padx=2,pady=2,columnspan=3)
    botonC.destroy()   
    
        
def delPregunta():
    print("2 Ayuda") 
    if respuestas[palabra]=="A":
        boton3['state'] = DISABLED
        boton4['state'] = DISABLED
    if respuestas[palabra]=="B":
        boton1['state'] = DISABLED
        boton4['state'] = DISABLED
    if respuestas[palabra]=="C":
        boton2['state'] = DISABLED
        boton4['state'] = DISABLED
    if respuestas[palabra]=="D":
        boton1['state'] = DISABLED
        boton2['state'] = DISABLED
        
    botonB.destroy()        

boton1=Button(ventana, text="A",width=15,command=botonA) 
boton1.grid(row=2,column=0,padx=5,pady=5)
boton2=Button(ventana, text="B",width=15,command=botonB) 
boton2.grid(row=2,column=2,padx=5,pady=5)
boton3=Button(ventana, text="C",width=15,command=botonC)
boton3.grid(row=3,column=0,padx=2,pady=2)
boton4=Button(ventana, text="D",width=15,command=botonD) 
boton4.grid(row=3,column=2,padx=2,pady=2)

botonA=Button(ventana, text="CAMBIA ¿?",width=10,command=cambioPregunta) 
botonA.grid(row=5,column=0,padx=2,pady=2)
botonB=Button(ventana, text="50 / 50",width=10,command=delPregunta) 
botonB.grid(row=5,column=2,padx=2,pady=2)
botonC=Button(ventana, text="Ayuda Amigo",width=10,command=ayudaAmigo) 
botonC.grid(row=5,column=1,padx=2,pady=2)

selecPre(preguntas) 
    
ventana.mainloop()