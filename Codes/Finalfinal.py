from Tkinter import *
import sys 
import tkFont
import RPi.GPIO as GPIO
from decimal import *
import time
import threading
from threading import Thread  
 #Import time library
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 
TRIG = 23                                  #Associate pin 23 to TRIG
ECHO = 24                                  #Associate pin 24 to ECHO
TRIG2 = 26                                  #Associate pin 23 to TRIG
ECHO2 = 19 
vertir=15
mezclar=18

GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in

GPIO.setup(TRIG2,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO2,GPIO.IN)                   #Set pin as GPIO in
GPIO.setup(vertir,GPIO.OUT)
GPIO.setup(mezclar,GPIO.OUT)

win= Tk ()
frame= Frame(win)
frame.pack
bottomframe= Frame (win)
bottomframe.pack(side= TOP)
CA= IntVar()
titulo = tkFont.Font(family = 'Helvetica', size = 28, weight='bold' )
titulo1 = tkFont.Font(family = 'Helvetica', size = 28)
texto = tkFont.Font(family = 'Helvetica', size = 26)

win.title("LOVEGA CONSULTORES")

def ok():   #DEFINICION DE BOTON OK
       print ("okk")
       okButton["text"] = "Datos Almacenados "
       NCA= CA.get() #Guardar valor Cantidad Aditivo
       NCo= Co.get() #Guardar Valor Cantidad Concentracion
       Vb= (int(NCA)/ (Decimal(NCo)+1)) #operacion para hallar VBase
       Vb= round( Vb, 3) #redondear a 3 decimales Vbase
       print "Volumen Base " , Vb
       global Vb
       Va= int(NCA)*Vb  #Hallar VaditivoConcentrado
       print "Volumen Aditivo" ,Va
       global Va #Revisar mk o litros _____________

        #CALCULO DE ALTURA DE ALTURA DE NIVEL
        
        #TANQUE BASE
       dtb=69.7 #diametro tanque base 69.7cm
       rtb=dtb/2 #radio
       hb= Vb/(3.15*rtb*rtb) #altura que alcanzara base
       hs1= 70  #Medicion h S1 (cm) en T=0____________________
       hd1= hs1+hb #altura del nivel Base
       print hd1
       global hd1
       #TANQUE ADITIVO
       dta=4 #diametro Tanque aditivo__________________
       rta= dta/2 #diametro tanque aditivo ___________
       ha= Va/(3.15*rta*rta) #altura que alcanzara aditivo
       hs2= 20 #medicion h S2 (cm) en T=0 ______________
       hd2= hs2+ha
       print hd2
       global hd2
       LB["text"] = Vb
       MA["text"] = Va

def aceptar(): 
       while True:
              GPIO.output(TRIG, False)                 #Set TRIG as LOW
              print "Waitng For Sensor To Settle"
              time.sleep(0.5)                            #Delay of 2 second
              GPIO.output(TRIG, True)                  #Set TRIG as HIG
              time.sleep(0.00001)                      #Delay of 0.00001 seconds
              GPIO.output(TRIG, False)

              while GPIO.input(ECHO)==0:
                     pulse_start = time.time()
              while GPIO.input(ECHO)==1:
                     pulse_end = time.time()                #Saves the last known time of HIGH pulse
              pulse_duration = pulse_end - pulse_start #Get pulse duration to a variabl
              distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
              distance = round(distance, 2)            #Round to two decimal points
              print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
              if distance > 3:
                     print "si"
              else:
                     print "fooook"
                     break      
       while True:
              GPIO.output(TRIG2, False)                 #Set TRIG as LOW
              print "Waitng For Sensor To Settle"
              time.sleep(0.5)                            #Delay of 2 second
              GPIO.output(TRIG2, True)                  #Set TRIG as HIGH
              time.sleep(0.00001)                      #Delay of 0.00001 seconds
              GPIO.output(TRIG2, False)
              while GPIO.input(ECHO2)==0:
                     pulse_start2 = time.time()
              while GPIO.input(ECHO2)==1:
                     pulse_end2 = time.time()                #Saves the last known time of HIGH pulse
                     pulse_duration2 = pulse_end2 - pulse_start2 #Get pulse duration to a variabl
                     distance2 = pulse_duration2 * 17150        #Multiply pulse duration by 17150 to get distance
                     distance2 = round(distance2, 2)            #Round to two decimal points
                     print "Distance2:",distance2 - 0.5,"cm"  #Print distance with 0.5 cm calibration
              if Distance2==5:
                     print "error"
              else:
                     print "fooook"
                     break
       
              
       
          
def vertir ():
       GPIO.output(15,GPIO.HIGH)
       print "vertir"
def mezclar ():
       GPIO.output(18,GPIO.HIGH)
       print "mezclar"
def detener ():
       GPIO.cleanup()
       
       

TI=Label (win, text= "MEZCLA DE ADITIVO", font=titulo)
TI.pack()
TCA= Label(win, text= "Cantidad Aditivo (LTS )",font= titulo1, borderwidth=4)
TCA.pack()
CA= Entry(win,textvariable=CA,font= texto, borderwidth=1 )
CA.pack()
TCo= Label(win, text= "Concentracion (Vaditivo/VBase)",font= titulo1,borderwidth=1 )
TCo.pack()
Co= Entry(win,font= texto, borderwidth=1 )
Co.pack()
okButton= Button(win, text= "Guardar ",font= texto, borderwidth=5, relief= RAISED,command = ok )
okButton.pack()

TLB= Label(win, text= "Litros Base",font= titulo1,borderwidth=1 )
TLB.pack()
LB = Label(win,font=texto,borderwidth=1 )
LB.pack()
TMA= Label(win, text= "Mililitros Aditivo",font= titulo1,borderwidth=1 )
TMA.pack()
MA = Label(win,font=texto,borderwidth=1 )
MA.pack()

#botones
aceptar=Button(win, text= "Aceptar ", font= texto,relief= RAISED,command = aceptar, height=4 , width= 8 )
aceptar.pack(side=LEFT)
vertir= Button(win, text= "Vertir Aditivo ", font= texto, relief= RAISED,command = vertir,height=4 , width= 10)
vertir.pack(side=LEFT)
mez= Button(win, text= "Mezclar ", font= texto,relief= RAISED,command = mezclar,height=4 , width= 8 )
mez.pack(side=LEFT)
stop= Button(win, text= "Detener ", font= texto,relief= RAISED, borderwidth=5 ,command = detener )
stop.pack(side=RIGHT)

mainloop()

