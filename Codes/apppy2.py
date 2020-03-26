import Tkinter as tk
import sys 
import tkFont
import RPi.GPIO as GPIO
from decimal import *
import time                                #Import time library
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 
TRIG = 23                                  #Associate pin 23 to TRIG
ECHO = 24                                  #Associate pin 24 to ECHO

GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in
myFont = tkFont.Font(family = 'Ubuntu', size = 30, weight = 'bold')

#s= IntVar() declarar neva variable


class window1:
    def _init_(self,master): #DECLARACION DE LABELS Y BOTONES

        
        TCA= Label(win, text= "Cantidad Aditivo (LTS )",font=myFont,borderwidth=1 )
        TCA.pack()
        CA= Entry(win,textvariable=CA, font= myFont, borderwidth=1 )
        CA.pack()
        TCo= Label(win, text= "Concentracion (Vaditivo/VBase)",font=myFont,borderwidth=1 )
        TCo.pack()
        Co= Entry(win, font= myFont, borderwidth=1 )
        Co.pack()
        okButton= Button(win, text= "ok", relief= RAISED, font = myFont, command = ok )
        okButton.pack()
        
    #CA= IntVar()    #cantidad aditivo deseado
    #Co= DoubleVar() #cantidad Concentracion
    #Vtb=DoubleVar() #volumenTanqueBase
    #Vta=DoubleVar() #volumenTanqueAditivo
    
    
    def ok(self):   #DEFINICION DE BOTON OK
        print ("okk")
        okButton["text"] = "Datos Almacenados "
        NCA= CA.get() #Guardar valor Cantidad Aditivo
        NCo= Co.get() #Guardar Valor Cantidad Concentracion
        Vb= (int(NCA)/ (Decimal(NCo)+1)) #operacion para hallar VBase
        Vb= round( Vb, 3) #redondear a 3 decimales Vbase
        print "Volumen Base " , Vb
        Va= int(NCA)*Vb  #Hallar VaditivoConcentrado
        print "Volumen Aditivo" ,Va

        #CALCULO DE ALTURA DE ALTURA DE NIVEL
        
        #TANQUE BASE
        dtb=69.7 #diametro tanque base 69.7cm
        rtb=dtb/2 #radio
        hb= Vb/(3.15*rtb*rtb) #altura que alcanzara base
        hs1= 70  #Medicion h S1 (cm) en T=0____________________
        hd1= hs1+hb #altura del nivel Base
        print hd1
        #TANQUE ADITIVO
        dta=4 #diametro Tanque aditivo__________________
        rta= dta/2 #diametro tanque aditivo ___________
        ha= Va/(3.15*rta*rta) #altura que alcanzara aditivo
        hs2= 20 #medicion h S2 (cm) en T=0 ______________
        hd2= hs2+ha
        print hd2
        
    def calculo(self):#sensor ultrasonico1
        while True:
            GPIO.output(TRIG, False)                 #Set TRIG as LOW
            print "Waitng For Sensor To Settle"
            time.sleep(0.5)                            #Delay of 2 seconds
            GPIO.output(TRIG, True)                  #Set TRIG as HIGH
            time.sleep(0.00001)                      #Delay of 0.00001 seconds
            GPIO.output(TRIG, False)                 #Set TRIG as LOW
            while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
                pulse_start = time.time()              #Saves the last known time of LOW pulse
            while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
                pulse_end = time.time()                #Saves the last known time of HIGH pulse
                pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable
                distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
                distance = round(distance, 2)            #Round to two decimal points
                print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
            if Distance==40:
                print "error"
            else:
                print "fooook"
            break
   
    
if __name__ == "__main__":
    win= tk.Tk()
    app = Demo1( win)
    win.mainloop()
    
if __name__== '__main__':
    main()
    

import Tkinter as tk
import sys 
import tkFont
import RPi.GPIO as GPIO
from decimal import *
import time                                #Import time library
GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 
TRIG = 23                                  #Associate pin 23 to TRIG
ECHO = 24                                  #Associate pin 24 to ECHO

GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in
myFont = tkFont.Font(family = 'Ubuntu', size = 30, weight = 'bold')

#s= IntVar() declarar neva variable


class window1:
    def _init_(self,master): #DECLARACION DE LABELS Y BOTONES

        
        TCA= Label(win, text= "Cantidad Aditivo (LTS )",font=myFont,borderwidth=1 )
        TCA.pack()
        CA= Entry(win,textvariable=CA, font= myFont, borderwidth=1 )
        CA.pack()
        TCo= Label(win, text= "Concentracion (Vaditivo/VBase)",font=myFont,borderwidth=1 )
        TCo.pack()
        Co= Entry(win, font= myFont, borderwidth=1 )
        Co.pack()
        okButton= Button(win, text= "ok", relief= RAISED, font = myFont, command = ok )
        okButton.pack()
        
    #CA= IntVar()    #cantidad aditivo deseado
    #Co= DoubleVar() #cantidad Concentracion
    #Vtb=DoubleVar() #volumenTanqueBase
    #Vta=DoubleVar() #volumenTanqueAditivo
    
    
    def ok(self):   #DEFINICION DE BOTON OK
        print ("okk")
        okButton["text"] = "Datos Almacenados "
        NCA= CA.get() #Guardar valor Cantidad Aditivo
        NCo= Co.get() #Guardar Valor Cantidad Concentracion
        Vb= (int(NCA)/ (Decimal(NCo)+1)) #operacion para hallar VBase
        Vb= round( Vb, 3) #redondear a 3 decimales Vbase
        print "Volumen Base " , Vb
        Va= int(NCA)*Vb  #Hallar VaditivoConcentrado
        print "Volumen Aditivo" ,Va

        #CALCULO DE ALTURA DE ALTURA DE NIVEL
        
        #TANQUE BASE
        dtb=69.7 #diametro tanque base 69.7cm
        rtb=dtb/2 #radio
        hb= Vb/(3.15*rtb*rtb) #altura que alcanzara base
        hs1= 70  #Medicion h S1 (cm) en T=0____________________
        hd1= hs1+hb #altura del nivel Base
        print hd1
        #TANQUE ADITIVO
        dta=4 #diametro Tanque aditivo__________________
        rta= dta/2 #diametro tanque aditivo ___________
        ha= Va/(3.15*rta*rta) #altura que alcanzara aditivo
        hs2= 20 #medicion h S2 (cm) en T=0 ______________
        hd2= hs2+ha
        print hd2
        
    def calculo(self):#sensor ultrasonico1
        while True:
            GPIO.output(TRIG, False)                 #Set TRIG as LOW
            print "Waitng For Sensor To Settle"
            time.sleep(0.5)                            #Delay of 2 seconds
            GPIO.output(TRIG, True)                  #Set TRIG as HIGH
            time.sleep(0.00001)                      #Delay of 0.00001 seconds
            GPIO.output(TRIG, False)                 #Set TRIG as LOW
            while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
                pulse_start = time.time()              #Saves the last known time of LOW pulse
            while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
                pulse_end = time.time()                #Saves the last known time of HIGH pulse
                pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable
                distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
                distance = round(distance, 2)            #Round to two decimal points
                print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
            if Distance==40:
                print "error"
            else:
                print "fooook"
            break
   
    
if __name__ == "__main__":
    win= tk.Tk()
    app = Demo1( win)
    win.mainloop()
    
if __name__== '__main__':
    main()
    

