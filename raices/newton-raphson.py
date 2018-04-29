# -*- coding: utf-8 -*-
"""
@author: Mario Quiroga. 
"""

from sympy.parsing.mathematica import mathematica
from sympy.parsing.maxima import parse_maxima
from sympy import *

#	RECIBE UN FUNCION EN FORMATO STRING, x ES UN VALOR SUPUESTAMENTE CERCANO A LA RAIZ		
def newtonRaphson(exp, x, error):	
	#PARSEO LA FUNCION
	f = mathematica(exp)
	print ('f(x) ingresada = '+str(f))
	
	#CALCULO LA DERIVADA
	df = diff(f)	
	print ('f\'(x) = '+str(df))
	while(abs(f.subs('x',x))>error):
		xAnt = x
		
		#IMPRIMO X y F(X) EN EL PUNTO 
		print ('f(x) = '+str(float(f.subs('x',xAnt))))
		print ('x = '+str(float(xAnt)))
		
		# EL X SIGUIENTE ES: X(n+1) = Xn - (f(Xn)/f'(Xn))
		x = x - (f.subs('x',x)/df.subs('x',x))		
		
		# DEFINO LA RECTA TANGENTE 
		rect = str(float(df.subs('x',xAnt)))+'*x+'+str(float(f.subs('x',xAnt)-df.subs('x',xAnt)*xAnt))		
		frect = mathematica(rect)
		

		print ('Recta: ', frect)
		print ('X(n+1) = ', float(x)) 
		print ('f(X(n+1)) = ',float(f.subs('x',x))) 
		
		# 
		if(f.subs('x',x)<=error):
			print('El algoritmo ha convergido. f(X(n+1))<=error')			
		#GRAFICO DE LA FUNCION Y LA RECTA TANGENTE		
		plot(f, frect)
		

#############################################################################################
# 	MAIN		

if __name__ == "__main__":
    #Fx = 'sin[x]'   # PASO LA FUNCION EN FORMATO STRING
    Fx = '3x**3+5x**2'
    puntoDeArranque = 5
    error = 0.1

    newtonRaphson(Fx,puntoDeArranque,error)			
		
