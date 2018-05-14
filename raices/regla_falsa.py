# -*- coding: utf-8 -*-
"""
@author: Mario Quiroga. 
"""

from sympy.parsing.mathematica import mathematica
from sympy.parsing.maxima import parse_maxima
from sympy import *

#	RECIBE UN FUNCION EN FORMATO STRING, x ES UN VALOR SUPUESTAMENTE CERCANO A LA RAIZ		
def regla_falsa(exp, x1, x2, error):	
  #PARSEO LA FUNCION
	f = mathematica(exp)
	print ('f(x) ingresada = '+str(f))
	
	print ('X1 = '+str(xAnt)+'     X2 = '+str(x))
    	
	# CALCULO EL PUNTO INTERIOR 
		
	# PREGUNTO SI MENOR QUE EL ERROR
	while(abs(f.subs('x',x))>error):
		xAux = xAnt
		xAnt = x		
		
		# IMPRIMO X y F(X) EN EL PUNTO 
		print ('f(x) = '+str(float(f.subs('x',xAnt))))
		print ('x = '+str(float(xAnt)))		
		
		# DEFINO LA RECTA que pasa por los puntos (x1, F(x1)) (x2, F(x2))
		m = float((f.subs('x',x) - f.subs('x',xAux)) / ( x - xAux))
		print ('m',m)
		
		
		
		# SI NO, EVALUO EL PROXIMO INTERVALO
		
		# CALCULO EL PUNTO INTERIOR 
		
		
		
		b = float(f.subs('x',xAux) - (m * xAux))		
		print ('b', b)
		
		rect = '('+str(m) + ') * x+ (' + str(b)+')'	# FORMATO STRING	
		print(rect)
		frect = mathematica(rect) #PARSEO EL STRING
		
		# CALCULO EL X SIGUIENTE: 
		# X(n+1) = Xn - (Xn - X(n-1)) / (f(Xn) - f(X(n-1)))*f(Xn)
		x = x - ((x - xAux) / (f.subs('x',x) - f.subs('x',xAux)) * f.subs('x',x))								

		print ('Recta: ', frect)
		print ('X(n+1) = ', float(x)) 
		print ('f(X(n+1)) = ',float(f.subs('x',x))) 
		
		
		if(abs(f.subs('x',x))<=error):
			print('El algoritmo ha convergido. f(X(n+1))<=error')			
		#GRAFICO DE LA FUNCION Y LA RECTA TANGENTE		
		plot(f, frect) 
		

#############################################################################################
# 	MAIN		

if __name__ == "__main__":
    #Fx = 'sin[x]'   # PASO LA FUNCION EN FORMATO STRING
    Fx = '3x**3+5x**2'
    x1 = -5
    x2 = 10
    error = 0.1

    regla_falsa(Fx,x1,x2,error)	
