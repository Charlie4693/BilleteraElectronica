'''
Created on May 11, 2016

@author: carlos
'''
from datetime import *
import calendar
import sys
import time

formato = "%d/%m/%Y"

class dueno:
    def __init__(self, nombres, apellidos, ci):
        self.nombres = nombres
        self.apellidos = apellidos
        self.ci = ci

class transaccion:
    def __init__(self, monto, fecha, idEst):
        self.monto = monto
        self.fecha = fecha
        self.id = idEst 
        
    def __str__(self):
        cadena= 'Monto: '+self.monto+', fecha: '+self.fecha +', Id Establecimiento: ' +self.idEst 
        return cadena
        
        
class creditos:
    def __init__(self):
        self.creditos = []
        
    def nuevaRecarga(self, transaccion):
        self.creditos.append(transaccion)
                
               
class debitos:
    def __init__(self):
        self.debitos = []
        
    def nuevoConsumo(self, transaccion):
        self.debitos.append(transaccion)

class BilleteraElectronica:
    def __init__(self, identificador, dueno, pin):
        self.identificardor = identificador
        self.dueno = dueno
        self.pin = pin
        self.saldo = 0
        self.creditos = creditos()
        self.debitos = debitos()
                
    def saldo(self):
        return self.saldo
       
    def recargar(self, monto, idEst):
        fecha = time.strftime("%d/%m/%y")
        cre = transaccion(monto, fecha, idEst)
        self.creditos.nuevaRecarga(cre)
        self.saldo = self.saldo + monto
        
    def consumir(self, monto, idEst, pin):
        if (self.saldo >= monto and self.pin == pin):
            fecha = time.strftime("%d/%m/%y")
            deb = transaccion(monto, fecha, idEst)
            self.debitos.nuevoConsumo(deb)
            self.monto = self.saldo - monto
            
        elif self.pin != pin:
            print("Clave incorrecta")
            
            
        else:
            print('No posee saldo suficiente para realizar esta operacion')
            
            
