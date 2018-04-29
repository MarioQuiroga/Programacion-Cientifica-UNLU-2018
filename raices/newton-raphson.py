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
		print ('f(x) = '+str(f.subs('x',xAnt)))
		print ('x = '+str(xAnt))
		
		# EL X SIGUIENTE ES: X(n+1) = Xn - (f(Xn)/f'(Xn))
		x = x - (f.subs('x',x)/df.subs('x',x))		
		
		# DEFINO LA RECTA TANGENTE 
		rect = str(df.subs('x',xAnt))+'*x+'+str(f.subs('x',xAnt)-df.subs('x',xAnt)*xAnt)		
		frect = mathematica(rect)
		

		print ('Recta: ', frect)
		print ('X(n+1) = ', x) 
		print ('f(X(n+1)) = ',f.subs('x',x)) 
		
		# 
		if(f.subs('x',x)<=error):
			print('El algoritmo ha convergido. f(X(n+1))<=error')			
		#GRAFICO DE LA FUNCION Y LA RECTA TANGENTE		
		print ('Cierre La gráfica de la función para continuar')
		plot(f, frect)
		

#############################################################################################
# 	MAIN		

Fx = 'x**3'   # PASO LA FUNCION EN FORMATO STRING
puntoDeArranque = 5
error = 0.1

newtonRaphson(Fx,puntoDeArranque,error)			
