#Funciones RSA

import math
import gmpy2 

#Calculo de si un numero es primo
def primo (num):
    for i in range(2,(int(math.sqrt(num)))):
        if (num% i==0):
            return 1
    return 0

#Calculo de n sabiendo p y q 
def guessn(p,q):
    n = p*q
    return n

#Calculo de uno de los factores de n, sabiendo n
def guessfactor(n,factor):
    if( n % factor != 0 ):
        return (-1) 
    otherfactor = n//factor
    return(otherfactor)

#Calculo de phi de n con p y q
def totient(p,q) : 
    tot = (p-1)*(q-1)
    return tot

#Generación de clave de desncriptado sabiendo e y phi(n)
def keygen (e,tot):
    d = gmpy2.invert(e,tot)
    return d

#Factorizar n
def factoring(n):
    for i in range(2,math.sqrt(n)):
        if (n % i==0):
            return i
