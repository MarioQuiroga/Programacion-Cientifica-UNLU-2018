# -*- coding: utf-8 -*-
"""
@author: Mario Quiroga. 
"""

from sympy.parsing.mathematica import mathematica
from sympy.parsing.maxima import parse_maxima
from sympy import *

#	RECIBE UNA FUNCION EN FORMATO STRING, 2 PUNTOS DE ARRANQUE Y EL ERROR
def secante(exp, xAnt, x, error):	
	#PARSEO LA FUNCION
	f = mathematica(exp)
	print ('f(x) ingresada = '+str(f))
	
	print ('X1 = '+str(xAnt)+'     X2 = '+str(x))
    
	while(abs(f.subs('x',x))>error):
		xAux = xAnt
		xAnt = x		
		
		#IMPRIMO X y F(X) EN EL PUNTO 
		print ('f(x) = '+str(float(f.subs('x',xAnt))))
		print ('x = '+str(float(xAnt)))		
		
		# DEFINO LA RECTA TANGENTE 
		m = float((f.subs('x',x) - f.subs('x',xAux)) / ( x - xAux))
		print ('m',m)
		
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

#EJ FUNCIONES TRIGONOMÉTRICAS cos[x].Cuidado pueden tardar mucho.
if __name__ == "__main__":
    Fx = '-2x**3+3x*5'   # PASO LA FUNCION EN FORMATO STRING
    x1 = 2
    x2 = 10
    error = 0.1
    
    secante(Fx, x1, x2, error)			
