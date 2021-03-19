#TEST MEMORIA VIRTUAL

from tkinter import*

#Importamos la biblioteca de audio

import winsound
from tkinter import messagebox



#Ventana
ventana=Tk()
ventana.geometry("1360x700+0+0")
ventana.title("Test memoria virtual")

#Scrollbar
scrollbar=Scrollbar(ventana)
can=Canvas(ventana,background="powderblue",yscrollcommand=scrollbar.set)
scrollbar.config( command = can.yview )
scrollbar.pack(side=RIGHT,fill=Y)
frame=Frame(can,bg="powderblue")
can.pack(side="left",fill="both",expand=True)
can.create_window(0,0,window=frame,anchor='nw')
#marcos (ruben)
marco0=Frame(frame,bd=5, relief="groove",bg="#cdc9c9",background="white")
marco0.grid(column=0,row=2,sticky="w")
marco0.columnconfigure(0, weight=1)
marco0.rowconfigure(0, weight=1)

marco1=Frame(frame,bd=5, relief="groove",bg="#cdc9c9",background="white")
marco1.grid(column=1,row=2,sticky="w")
marco1.columnconfigure(0, weight=1)
marco1.rowconfigure(0, weight=1)

marco2=Frame(frame,bd=5, relief="groove",bg="#cdc9c9",background="white")
marco2.grid(column=2,row=2,sticky="w")
marco2.columnconfigure(0, weight=1)
marco2.rowconfigure(0, weight=1)


#Aqui va el texto y disenio


#variable para que cuando inicie no comienze seleccionada ninguna opcion y almacenar la eleccion

selecP1=IntVar()

selecP2=IntVar()

selecP3=IntVar()

selP4a=IntVar()
selP4b=IntVar()
selP4c=IntVar()
selP4d=IntVar()

selecP5=IntVar()

selecP6=IntVar()

selP7a=IntVar()
selP7b=IntVar()
selP7c=IntVar()
selP7d=IntVar()

selP8a=IntVar()
selP8b=IntVar()
selP8c=IntVar()
selP8d=IntVar()

selecP9=IntVar()

selecP10=IntVar()

#Preguntas

Pregunta1 = Label(marco0,wraplength=5000,text="1. ¿Quien es este jugaror?",font=("Helvetica",14,"bold"),background="white").grid(column=2,row=17)

Pregunta2 = Label(marco0,wraplength=5000,text="2. ¿ Cual es el apodo de este jugador?",font=("Helvetica",14,"bold"),background="white").grid(column=2,row=22)

Pregunta3 = Label(marco0,wraplength=5000,text="3. ¿Que acontecimiento historico produjo este jugador?",font=("Helvetica",14,"bold"),background="white").grid(column=2,row=27)

Pregunta4 = Label(marco0,wraplength=5000,text="4. ¿Cuales de estos anios son algunos de los titulos conseguidos?",font=("Helvetica",14,"bold"),background="white").grid(column=2,row=32)

Pregunta5 = Label(marco0,wraplength=5000,text="5. ¿Quien es este jugador?",font=("Helvetica",14,"bold"),background="white").grid(column=2,row=38)

Pregunta6 = Label(marco0,wraplength=5000,text="6. ¿Este DT es el del famoso 4-0?",font=("Helvetica",14,"bold"),background="white").grid(column=2,row=43)

Pregunta7 = Label(marco0,wraplength=5000,text="7. Marque dos frases tipicas del famoso Chacho Coudet",font=("Helvetica",14,"bold"),background="white").grid(column=2,row=49)

Pregunta8 = Label(marco0,wraplength=5000,text="8. Marque el nombre de estos dos delanteros",font=("Helvetica",14,"bold"),background="white").grid(column=2,row=55)

Pregunta9 = Label(marco0,wraplength=5000,text="9. ¿Cual es el nombre de este arquero?",font=("Helvetica",14,"bold"),background="white").grid(column=2,row=61)

Pregunta10 = Label(marco0,wraplength=5000,text="10 ¿Quien es este famoso Defensor?",font=("Helvetica",14,"bold"),background="white").grid(column=2,row=66)


#Respuestas
#1
RdbP1a = Radiobutton(marco0,value=1,wraplength=5000,text="Marco Ruben",font=("Helvetica",12),background="white",variable=selecP1).grid(column=2,row=18,sticky="w")
RdbP1b = Radiobutton(marco0,value=2,wraplength=5000,text="Paglialunga",font=("Helvetica",12),background="white",variable=selecP1).grid(column=2,row=19,sticky="w")
RdbP1c = Radiobutton(marco0,value=3,wraplength=5000,text="Nacho Scocco",font=("Helvetica",12),background="white",variable=selecP1).grid(column=2,row=20,sticky="w")
#2
RdbP2a = Radiobutton(marco0,value=4,wraplength=5000,text="Mister River Plate",font=("Helvetica",12),background="white",variable=selecP2).grid(column=2,row=23,sticky="w")
RdbP2b = Radiobutton(marco0,value=5,wraplength=5000,text="Sebastian Abreu",font=("Helvetica",12),background="white",variable=selecP2).grid(column=2,row=24,sticky="w")
RdbP2c = Radiobutton(marco0,value=6,wraplength=5000,text="Teito",font=("Helvetica",12),background="white",variable=selecP2).grid(column=2,row=25,sticky="w")
#3
RdbP3a = Radiobutton(marco0,value=7,wraplength=5000,text="3 goles al Barcelona",font=("Helvetica",12),background="white",variable=selecP3).grid(column=2,row=28,sticky="w")
RdbP3b = Radiobutton(marco0,value=8,wraplength=5000,text="El Pirulazo",font=("Helvetica",12),background="white",variable=selecP3).grid(column=2,row=29,sticky="w")
RdbP3c = Radiobutton(marco0,value=9,wraplength=5000,text="Gol de cabeza de mitad de cancha",font=("Helvetica",12),background="white",variable=selecP3).grid(column=2,row=30,sticky="w")
#4
ChkP4a=Checkbutton(marco0,wraplength=5000,text="Conmebol 1995",font=("Helvetica",12),background="white",variable=selP4a,onvalue=1, offvalue=0).grid(column=2,row=33,sticky="w")
ChkP4b=Checkbutton(marco0,wraplength=5000,text="Campeonato Primera division 1987",font=("Helvetica",12),background="white",variable=selP4b,onvalue=1, offvalue=0).grid(column=2,row=34,sticky="w")
ChkP4c=Checkbutton(marco0,wraplength=5000,text="Torneo Nacional 1980",font=("Helvetica",12),background="white",variable=selP4c,onvalue=1, offvalue=0).grid(column=2,row=35,sticky="w")
ChkP4d=Checkbutton(marco0,wraplength=5000,text="Copa Argentina 2015",font=("Helvetica",12),background="white",variable=selP4d,onvalue=1, offvalue=0).grid(column=2,row=36,sticky="w")
#5
RdbP5a = Radiobutton(marco0,value=10,wraplength=5000,text="Toledo",font=("Helvetica",12),background="white",variable=selecP5).grid(column=2,row=39,sticky="w")
RdbP5b = Radiobutton(marco0,value=11,wraplength=5000,text="La cobra Wanchope",font=("Helvetica",12),background="white",variable=selecP5).grid(column=2,row=40,sticky="w")
RdbP5c = Radiobutton(marco0,value=12,wraplength=5000,text="Bracamonte",font=("Helvetica",12),background="white",variable=selecP5).grid(column=2,row=41,sticky="w")
#6
RdbP6a = Radiobutton(marco0,value=13,wraplength=5000,text="Tal vez",font=("Helvetica",12),background="white",variable=selecP6).grid(column=2,row=45,sticky="w")
RdbP6b = Radiobutton(marco0,value=14,wraplength=5000,text="No",font=("Helvetica",12),background="white",variable=selecP6).grid(column=2,row=46,sticky="w")
RdbP6c = Radiobutton(marco0,value=15,wraplength=5000,text="Si",font=("Helvetica",12),background="white",variable=selecP6).grid(column=2,row=47,sticky="w")
#7
ChkP7a=Checkbutton(marco0,wraplength=5000,text="Mis objetivos son otros",font=("Helvetica",12),background="white",variable=selP7a,onvalue=1, offvalue=0).grid(column=2,row=50,sticky="w")
ChkP7b=Checkbutton(marco0,wraplength=5000,text="¿Queres que te cuente un chiste? Newells gana un clasico",font=("Helvetica",12),background="white",variable=selP7b,onvalue=1, offvalue=0).grid(column=2,row=51,sticky="w")
ChkP7c=Checkbutton(marco0,wraplength=5000,text="La fiesta pajarito",font=("Helvetica",12),background="white",variable=selP7c,onvalue=1, offvalue=0).grid(column=2,row=52,sticky="w")
ChkP7d=Checkbutton(marco0,wraplength=5000,text="Riquelme esta feliz",font=("Helvetica",12),background="white",variable=selP7d,onvalue=1, offvalue=0).grid(column=2,row=53,sticky="w")
#8
ChkP8a=Checkbutton(marco0,wraplength=5000,text="Washington Sebastian  Abreu",font=("Helvetica",12),background="white",variable=selP8a,onvalue=1, offvalue=0).grid(column=2,row=56,sticky="w")
ChkP8b=Checkbutton(marco0,wraplength=5000,text="Washington Camacho",font=("Helvetica",12),background="white",variable=selP8b,onvalue=1, offvalue=0).grid(column=2,row=57,sticky="w")
ChkP8c=Checkbutton(marco0,wraplength=5000,text="Franco Cervi",font=("Helvetica",12),background="white",variable=selP8c,onvalue=1, offvalue=0).grid(column=2,row=58,sticky="w")
ChkP8d=Checkbutton(marco0,wraplength=5000,text="Franco Niell",font=("Helvetica.",12),background="white",variable=selP8d,onvalue=1, offvalue=0).grid(column=2,row=59,sticky="w")
#9
RdbP9a = Radiobutton(marco0,value=16,wraplength=5000,text="Mauricio Caranta",font=("Helvetica",12),background="white",variable=selecP9).grid(column=2,row=62,sticky="w")
RdbP9b = Radiobutton(marco0,value=17,wraplength=5000,text="Ruso Rodriguez",font=("Helvetica",12),background="white",variable=selecP9).grid(column=2,row=63,sticky="w")
RdbP9c = Radiobutton(marco0,value=18,wraplength=5000,text="Sebastian Sosa",font=("Helvetica",12),background="white",variable=selecP9).grid(column=2,row=64,sticky="w")
#10
RdbP10a = Radiobutton(marco0,value=19,wraplength=5000,text="Loncho Ferrari",font=("Helvetica",12),background="white",variable=selecP10).grid(column=2,row=67,sticky="w")
RdbP10b = Radiobutton(marco0,value=20,wraplength=5000,text="El petaco Carbonari",font=("Helvetica",12),background="white",variable=selecP10).grid(column=2,row=68,sticky="w")
RdbP10c = Radiobutton(marco0,value=21,wraplength=5000,text="Yeimar Pastor",font=("Helvetica",12),background="white",variable=selecP10).grid(column=2,row=69,sticky="w")



#IMAGEN

#1

marcoruben=PhotoImage(file="marcoruben.gif")
lblimagen2 = Label(marco0,wraplength=5000,image=marcoruben).grid(column=2,row=21)

#2

teito=PhotoImage(file="teito.gif")
lblimagen1 = Label(marco0,wraplength=5000,image=teito).grid(column=2,row=26)

#3

pirulazo=PhotoImage(file="pirulazo.gif")
lblimagen3 = Label(marco0,wraplength=5000,image=pirulazo).grid(column=2,row=31)

#4

RC=PhotoImage(file="RC.gif")
lblimagen4 = Label(marco0,wraplength=5000,image=RC).grid(column=2,row=37)

#5

wanchope=PhotoImage(file="wanchope.gif")
lblimagen5 = Label(marco0,wraplength=5000,image=wanchope).grid(column=2,row=42)

#6

russo=PhotoImage(file="russo.gif")
lblimagen6 = Label(marco0,wraplength=5000,image=russo).grid(column=2,row=48)

#7

chacho=PhotoImage(file="chacho.gif")
lblimagen7 = Label(marco0,wraplength=5000,image=chacho).grid(column=2,row=54)

#8

abreuniell=PhotoImage(file="abreuniell.gif")
lblimagen8 = Label(marco0,wraplength=5000,image=abreuniell).grid(column=2,row=60)

#9

caranta=PhotoImage(file="caranta.gif")
lblimagen9 = Label(marco0,wraplength=5000,image=caranta).grid(column=2,row=65)

#10

carbonari=PhotoImage(file="carbonari.gif")
lblimagen10 = Label(marco0,wraplength=5000,image=carbonari).grid(column=2,row=70)




   
def Marco (): 
    winsound.PlaySound("marco.wav", winsound.SND_FILENAME)


#BOTON FINALIZAR



#Aqui creamos la variable para que python calcule el resultado
        
def Finalizar ():
            #CONTADOR
   cont=0
#1
   if selecP1.get() == 1:
        cont=cont+1
        etiquetap1 = Label(marco1,text="CORRECTO",font=("Helvetica",16,"bold","underline"), padx=(10), pady=(10),bg="lawngreen").grid(column=3,row=19)
        Pregunta12= Label(marco1,wraplength=5000,text="",font=("Helvetica",50,"bold"),background="white").grid(column=3,row=20)

   else:
        etiquetap1 = Label(marco1,text="INCORRECTO",font=("Helvetica",16,"bold","underline"), padx=(10), pady=(10),bg="red").grid(column=3,row=19)
        Pregunta13= Label(marco1,wraplength=5000,text="",font=("Helvetica",405,"bold"),background="white").grid(column=3,row=20)
        RdbP1a = Radiobutton(marco0,value=1,wraplength=5000,text="Marco Ruben",font=("Helvetica",12),background="lawngreen",variable=selecP1).grid(column=2,row=18,sticky="w")

#2
   if selecP2.get() == 6:
        cont=cont+1
        etiquetap2 = Label(marco1,text="CORRECTO",font=("Helvetica",16,"bold","underline"), padx=(10), pady=(10),bg="lawngreen").grid(column=3,row=23)
        Pregunta22= Label(marco1,wraplength=5000,text="",font=("Helvetica",50,"bold"),background="white").grid(column=3,row=24)
   else:
        etiquetap2 = Label(marco1,text="INCORRECTO",font=("Helvetica",16,"bold","underline"), padx=(10), pady=(10),bg="red").grid(column=3,row=23)
        Pregunta23= Label(marco1,wraplength=5000,text="",font=("Helvetica",405,"bold"),background="white").grid(column=3,row=24)
        RdbP2c = Radiobutton(marco0,value=6,wraplength=5000,text="Teito",font=("Helvetica",12),background="lawngreen",variable=selecP2).grid(column=2,row=25,sticky="w")


#3
   if selecP3.get() == 8:
        cont=cont+1
        etiquetap3 = Label(marco1,text="CORRECTO",font=("Helvetica",16,"bold","underline"), padx=(10), pady=(10),bg="lawngreen").grid(column=3,row=27)
        Pregunta32= Label(marco1,wraplength=5000,text="",font=("Helvetica",50,"bold"),background="white").grid(column=3,row=28)
   else:
        etiquetap3 = Label(marco1,text="INCORRECTO",font=("Helvetica",16,"bold","underline"), padx=(10), pady=(10),bg="red").grid(column=3,row=27)
        Pregunta24= Label(marco1,wraplength=5000,text="",font=("Helvetica",405,"bold"),background="white").grid(column=3,row=28)
        RdbP3b = Radiobutton(marco0,value=8,wraplength=5000,text="El Pirulazo",font=("Helvetica",12),background="lawngreen",variable=selecP3).grid(column=2,row=29,sticky="w")


       
#4
   if selP4a.get() == 1 and selP4b.get() == 1 and selP4c.get() == 1 and selP4d.get() == 0:
        cont=cont+1
        etiquetap4 = Label(marco1,text="CORRECTO",font=("Helvetica",16,"bold","underline"), padx=(10), pady=(10),bg="lawngreen").grid(column=3,row=31)
        Pregunta42= Label(marco1,wraplength=5000,text="",font=("Helvetica",50,"bold"),background="white").grid(column=3,row=32)
   else:
        etiquetap4 = Label(marco1,text="INCORRECTO",font=("Helvetica",16,"bold","underline"), padx=(10), pady=(10),bg="red").grid(column=3,row=31)
        Pregunta43= Label(marco1,wraplength=5000,text="",font=("Helvetica",405,"bold"),background="white").grid(column=3,row=32)
        ChkP4a=Checkbutton(marco0,wraplength=5000,text="Conmebol 1995",font=("Helvetica",12),background="lawngreen",variable=selP4a,onvalue=1, offvalue=0).grid(column=2,row=33,sticky="w")
        ChkP4b=Checkbutton(marco0,wraplength=5000,text="Campeonato Primera division 1987",font=("Helvetica",12),background="lawngreen",variable=selP4b,onvalue=1, offvalue=0).grid(column=2,row=34,sticky="w")
        ChkP4c=Checkbutton(marco0,wraplength=5000,text="Torneo Nacional 1980",font=("Helvetica",12),background="lawngreen",variable=selP4c,onvalue=1, offvalue=0).grid(column=2,row=35,sticky="w")

        

#5
   if selecP5.get() == 11:
        cont=cont+1
        etiquetap5 = Label(marco1,text="CORRECTO",font=("Helvetica",16,"bold","underline"), padx=(10), pady=(10),bg="lawngreen").grid(column=3,row=36)
        Pregunta52= Label(marco1,wraplength=5000,text="",font=("Helvetica",50,"bold"),background="white").grid(column=3,row=37)
   else:
        etiquetap5 = Label(marco1,text="INCORRECTO",font=("Helvetica",16,"bold","underline"), padx=(10), pady=(10),bg="red").grid(column=3,row=36)
        Pregunta53= Label(marco1,wraplength=5000,text="",font=("Helvetica",405,"bold"),background="white").grid(column=3,row=37)
        RdbP5b = Radiobutton(marco0,value=11,wraplength=5000,text="La cobra Wanchope",font=("Helvetica",12),background="lawngreen",variable=selecP5).grid(column=2,row=40,sticky="w")


#6
   if selecP6.get() == 15:
        cont=cont+1
        etiquetap6 = Label(marco1,text="CORRECTO",font=("Helvetica",16,"bold","underline"), padx=(10), pady=(10),bg="lawngreen").grid(column=3,row=40)
        Pregunta62= Label(marco1,wraplength=5000,text="",font=("Helvetica",50,"bold"),background="white").grid(column=3,row=41)
   else:
        etiquetap6 = Label(marco1,text="INCORRECTO",font=("Helvetica",16,"bold","underline"), padx=(10), pady=(10),bg="red").grid(column=3,row=40)
        Pregunta63= Label(marco1,wraplength=5000,text="",font=("Helvetica",405,"bold"),background="white").grid(column=3,row=41)
        RdbP6c = Radiobutton(marco0,value=15,wraplength=5000,text="Si",font=("Helvetica",12),background="lawngreen",variable=selecP6).grid(column=2,row=47,sticky="w")


#7
   if selP7a.get() == 0 and selP7b.get() == 1 and selP7c.get() == 1 and selP7d.get() == 0:
        cont=cont+1
        etiquetap7 = Label(marco1,text="CORRECTO",font=("Helvetica",16,"bold","underline"), padx=(10), pady=(10),bg="lawngreen").grid(column=3,row=44)
        Pregunta72= Label(marco1,wraplength=5000,text="",font=("Helvetica",50,"bold"),background="white").grid(column=3,row=45)
   else:
        etiquetap7 = Label(marco1,text="INCORRECTO",font=("Helvetica",16,"bold","underline"), padx=(10), pady=(10),bg="red").grid(column=3,row=44)
        Pregunta73= Label(marco1,wraplength=5000,text="",font=("Helvetica",405,"bold"),background="white").grid(column=3,row=45)
        ChkP7b=Checkbutton(marco0,wraplength=5000,text="¿Queres que te cuente un chiste? Newells gana un clasico",font=("Helvetica",12),background="lawngreen",variable=selP7b,onvalue=1, offvalue=0).grid(column=2,row=51,sticky="w")
        ChkP7c=Checkbutton(marco0,wraplength=5000,text="La fiesta pajarito",font=("Helvetica",12),background="lawngreen",variable=selP7c,onvalue=1, offvalue=0).grid(column=2,row=52,sticky="w")

       
   
#8
   if selP8a.get() == 1 and selP8b.get() == 0 and selP8c.get() == 0 and selP8d.get() == 1:
        cont=cont+1
        etiquetap8 = Label(marco1,text="CORRECTO",font=("Helvetica",16,"bold","underline"), padx=(10), pady=(10),bg="lawngreen").grid(column=3,row=49)
        Pregunta82= Label(marco1,wraplength=5000,text="",font=("Helvetica",50,"bold"),background="white").grid(column=3,row=50)
   else:
        etiquetap8 = Label(marco1,text="INCORRECTO",font=("Helvetica",16,"bold","underline"), padx=(10), pady=(10),bg="red").grid(column=3,row=49)
        Pregunta83= Label(marco1,wraplength=5000,text="",font=("Helvetica",405,"bold"),background="white").grid(column=3,row=50)
        ChkP8d=Checkbutton(marco0,wraplength=5000,text="Franco Niell",font=("Helvetica.",12),background="lawngreen",variable=selP8d,onvalue=1, offvalue=0).grid(column=2,row=59,sticky="w")
        ChkP8a=Checkbutton(marco0,wraplength=5000,text="Washington Sebastian  Abreu",font=("Helvetica",12),background="lawngreen",variable=selP8a,onvalue=1, offvalue=0).grid(column=2,row=56,sticky="w")


#9
   if selecP9.get() == 16:
        cont=cont+1
        etiquetap9 = Label(marco1,text="CORRECTO",font=("Helvetica",16,"bold","underline"), padx=(10), pady=(10),bg="lawngreen").grid(column=3,row=54)
        Pregunta92= Label(marco1,wraplength=5000,text="",font=("Helvetica",50,"bold"),background="white").grid(column=3,row=55)
   else:
        etiquetap9 = Label(marco1,text="INCORRECTO",font=("Helvetica",16,"bold","underline"), padx=(10), pady=(10),bg="red").grid(column=3,row=54)
        Pregunta93= Label(marco1,wraplength=5000,text="",font=("Helvetica",405,"bold"),background="white").grid(column=3,row=55)
        RdbP9a = Radiobutton(marco0,value=16,wraplength=5000,text="Mauricio Caranta",font=("Helvetica",12),background="lawngreen",variable=selecP9).grid(column=2,row=62,sticky="w")


        
#10
   if selecP10.get() == 20:
        cont=cont+1
        etiquetap10 = Label(marco1,text="CORRECTO",font=("Helvetica",16,"bold","underline"), padx=(10), pady=(10),bg="lawngreen").grid(column=3,row=58)
        Pregunta102= Label(marco1,wraplength=5000,text="",font=("Helvetica",50,"bold"),background="white").grid(column=3,row=59)
   else:
        etiquetap10 = Label(marco1,text="INCORRECTO",font=("Helvetica",16,"bold","underline"), padx=(10), pady=(10),bg="red").grid(column=3,row=58)
        Pregunta103= Label(marco1,wraplength=5000,text="",font=("Helvetica",405,"bold"),background="white").grid(column=3,row=59)
        RdbP10b = Radiobutton(marco0,value=20,wraplength=5000,text="El petaco Carbonari",font=("Helvetica",12),background="lawngreen",variable=selecP10).grid(column=2,row=68,sticky="w")

  
#Preguntas correctas e incorrectas

   t="PREGUNTAS CORRECTAS: "+ str(cont)
   to=10- int(cont)
   t2="PREGUNTAS INCORRECTAS: " + str(to)
   pr= int(cont)*int(10)
   t3="PORCENTAJE:" + str(pr)+"%"
   pregcorrectas=Label(marco2,text=t,font=("Helvetica",16,"bold"), padx=(10), pady=(10),bg="lawngreen").grid(column=0,row=13,sticky="w")
   pregincorrectas=Label(marco2,text=t2,font=("Helvetica",16,"bold"), padx=(10), pady=(10),bg="red").grid(column=0,row=14,sticky="w")
   porcentaje=Label(marco2,text=t3,font=("Helvetica",16,"bold"), padx=(10), pady=(10),bg="yellow").grid(column=0,row=15,sticky="w")

   messagebox.showinfo("puntuscion","Ha sacado un: " + str(cont) )

#Botones

btnfinalizar=Button(marco0, text="FINALIZAR",font=("Helvetica",16,"bold",),command=lambda: [Marco(), Finalizar()], bd=10, bg="yellow",cursor="hand2").grid(column=2,row=71)

#Final de ventana y scroll



ventana.update()
can.config(scrollregion=can.bbox("all"))
ventana.mainloop()


