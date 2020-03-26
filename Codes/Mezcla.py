from Tkinter import *
import sys
import tkFont
import RPi.GPIO as GPIO
from decimal import *
import time                                #Import time library
import tkMessageBox
import subprocess

GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering

RELE=[26,19,13,6,5,22]
TRIG = 27                                #Associate pin 23 to TRIG
ECHO = 4                                  #Associate pin 24 to ECHO
TRIG2 = 17                                  #Associate pin 23 to TRIG
ECHO2 = 21
#Rojo=26	
#Verde = 19
#Motor= 13
#valvula=6 	
#BBase=22	 
#Baditivo=5
                                        #Declaracion ECHO entrada y TRIG salida
GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in
GPIO.setup(TRIG2,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO2,GPIO.IN)                   #Set pin as GPIO in

for i in RELE:                          #Declarar ciclo para reles inicien en modo OFF
        GPIO.setup(i,GPIO.OUT)
        GPIO.output(i,GPIO.HIGH)
        time.sleep(0.2)

win= Tk ()                              #declaracion ventana principal
frame= Frame(win)
win.attributes('-zoomed',True)
frame.pack

CA= IntVar()
#bottomframe= Frame (win)
#bottomframe.pack(side= BOTTOM)

#NAd= IntVar()                                       #declaracion fuentes de texto de ventana y tamaños de letra
titulo = tkFont.Font(family = 'Helvetica', size = 15, weight='bold' )
titulo1 = tkFont.Font(family = 'Helvetica', size =15)
texto = tkFont.Font(family = 'Helvetica', size = 14)
texto2= tkFont.Font(family= 'Helvetica', size =30)

                                        #declaracion geometria de ventana tamaño 
win.title("LOVEGA CONSULTORES")
#win.geometry('500x500')

#win.resizable(width=True, height= True)



def ok():   #DEFINICION DE BOTON OK
       print ("okk")
       okButton["text"] = "Datos Almacenados "
       Nad= Adm.get() #Aditivo en Mililitros
       NAd= (Decimal(Nad))/1000 #Aditivo en Litros
       Nba= Bal.get() #Base en Litros
       NCA= Decimal(NAd) + Decimal(Nba)  #cantidad Total
       print NCA
       global NCA
       NBa=Decimal(Nba)
       PBa= (NBa*100)/NCA
       PAc= (NAd*100)/NCA
       NProporcion= PAc/PBa
       NCo= NProporcion

       global t
       print NCo
       Vb= (Decimal(NCA)/ (Decimal(NCo)+1)) #operacion para hallar VBase
       Vb= round( Vb, 3) #redondear a 3 decimales Vbase
       Vbl= Vb-40.5
       print "Volumen Base " , Vb
       global Vb
       Va= Decimal(NCA)-Decimal(Vb) #Hallar VaditivoConcentrado
       Va= round( Va, 3)#redondear a 3 decimales Vbase
       print "Volumen Aditivo" ,Va
       global Va 

#CALCULO DE ALTURA DE ALTURA DE NIVEL
        #TANQUE BASE
       hb= -0.26194*( Vbl+40.5) +93.56 #funcion que describe hb vs vb
       print"hb", hb
               #TANQUE ADITIVO
       global hb
       ha= -0.0185*Va*1000+43.5 #funcion que describe hac vs vaprint"hac",Decimal (ha)
       global ha
       print"ha", ha
       LB["text"] = Vb
       MA["text"] = Va
       CA["text"] = NCA
      

def aceptar():
        while True:
                GPIO.output(TRIG, False)                 #Set TRIG as LOW
                print "Waitng For Sensor To Settle1"
                time.sleep(0.5)                            #Delay of 2 second
                GPIO.output(TRIG, True)                  #Set TRIG as HIGH
                time.sleep(0.01)                      #Delay of 0.00001 seconds
                GPIO.output(TRIG, False)
                while GPIO.input(ECHO)==0:
                        pulse_start = time.time()
                while GPIO.input(ECHO)==1:
                        pulse_end = time.time()                #Saves the last known time of HIGH pulse
                pulse_duration = pulse_end - pulse_start #Get pulse duration to a variabl
                distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
                distance = round(distance, 2)            #Round to two decimal points
                print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
                if distance >= hb:
                        GPIO.setup(5,GPIO.OUT)
                        GPIO.output(5,GPIO.LOW)
                else:
                        GPIO.setup(5,GPIO.OUT)
                        GPIO.output(5,GPIO.HIGH)
                        break


        while True:
                GPIO.output(TRIG2, False)                 #Set TRIG as LOW
                print "Waitng For Sensor To Settle2"
                time.sleep(0.5)                           #Delay of 2 second
                GPIO.output(TRIG2, True)                  #Set TRIG as HIGH
                time.sleep(0.01)                      #Delay of 0.00001 seconds
                GPIO.output(TRIG2, False)
                while GPIO.input(ECHO2)==0:
                        pulse_start2 = time.time()
                while GPIO.input(ECHO2)==1:
                        pulse_end2 = time.time()                #Saves the last known time of HIGH puls
                pulse_duration2 = pulse_end2 - pulse_start2 #Get pulse duration to a variabl
                distance2 = pulse_duration2 * 17150        #Multiply pulse duration by 17150 to get distance
                distance2 = round(distance2, 2)            #Round to two decimal points
                print "Distance2:",distance2 - 0.5,"cm"  #Print distance with 0.5 cm calibration
                if distance2 >= ha:
                        GPIO.setup(22,GPIO.OUT)
                        GPIO.output(22,GPIO.LOW)
                else:
                        GPIO.setup(22,GPIO.OUT)
                        GPIO.output(22,GPIO.HIGH)
                        tkMessageBox.showinfo("Mensaje","Verifique nivel de Aditivo concentrado en la Bureta")
                        break
      

def vertir ():
    try:
        GPIO.output(6,GPIO.LOW)#time.sleep(3600)-------------- numero real
        time.wait(350);
        GPIO.output(6,GPIO.HIGH)#time.sleep(3600)-------------- numero real
        tkMessageBox.showinfo("Mensaje","Vertido con exito")
    except KeyboardInterrupt:
        print "quit"
        
def mezclar ():
    try:
        GPIO.output(19,GPIO.LOW)#time.sleep(3600)-------------- numero real
        GPIO.output(13,GPIO.LOW)
        time.sleep(1);  #TIEMPO MEZCLADO ADITIVO
       
        tkMessageBox.showinfo("Mensaje","Mezclado con exito")
      
    except KeyboardInterrupt:
        print "quit"
def detener ():
       GPIO.cleanup()
       
def uso():
        
                tkMessageBox.showinfo("Informacion adicional","Ingrese cantidad de aditivo y base, presione guardar, y siga el orden de los botones, cada uno le indicara cuando presionar el siguiente")
        


TI=Label (win, text= "MEZCLA DE ADITIVO", font=titulo).grid(row=1,column=2)


Tba= Label(win, text= "Base(lt)",font= titulo1,borderwidth=1 )
Tba.grid(row=2,column=1)
Bal= Spinbox(win,font= texto2, from_=45,to=300,borderwidth=1,  width= 12)  #BASELITROS
Bal.grid(row=2,column=2)


Tad= Label(win, text= "Aditivo(ml)",font= titulo1,borderwidth=1 )
Tad.grid(row=3,column=1)
Adm= Spinbox(win,font= texto2,from_= 1,to=2000, borderwidth=1, width= 12)#ADITIVOMILILITROS
Adm.grid(row=3,column=2)


okButton= Button(win, text= "Guardar ",font= texto, borderwidth=5, relief= RAISED,command = ok )
okButton.grid(row=4,column=2)

TCA= Label(win, text= "Total(lt)",font= titulo1, borderwidth=1)
TCA.grid(row=5,column=1)
CA= Label (win,font= titulo1, borderwidth=1)
CA.grid(row=5,column=2,sticky=W)

TLB= Label(win, text= "Litros Base",font= titulo1,borderwidth=1 )
TLB.grid(row=6,column=1)
LB = Label(win,font=titulo1,borderwidth=1 )
LB.grid(row=6,column=2,sticky=W)
TMA= Label(win, text= "Litros Aditivo Concentrado",font= titulo1,borderwidth=1 )
TMA.grid(row=7,column=1)
MA = Label(win,font=titulo1,borderwidth=1 )
MA.grid(row=7,column=2,sticky=W)
Aviso=Button(win,text="?",font= titulo, command=uso,borderwidth=5 ,background="yellow",)
Aviso.grid(row=1, column=1)

#botones
aceptar=Button(win, text= "1.Comenzar llenado ", font= texto,relief= RAISED,command = aceptar, height=2 , width= 14).grid(row=8,column=1)
vertir= Button(win, text= "2.Verter Aditivo ", font= texto, relief= RAISED,command = vertir,height=2 , width= 12).grid(row=8,column=2)
mez= Button(win, text= "3.Iniciar Mezcla ", font= texto,relief= RAISED,command = mezclar,height=2 , width= 12 ).grid(row=8,column=3)
stop= Button(win, text= "Detener ", font= texto,relief= RAISED, borderwidth=5 ,background="red",command = detener, height=2, width= 8).grid(row=9,column=2)

win.mainloop()

