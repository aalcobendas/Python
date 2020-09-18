from constraint import *

problem = Problem()

# Variables: Asignaturas con el dominio las franjas horarias
#      	Profesores con el dominio asignaturas


problem.addVariables(['N','N2','C', 'C2', 'I','I2','E'], range(10)) #horas de asignaturas a impartir
problem.addVariables(['M', 'M2'], [0,3,6,9])  #matematicas se debe impartir en las primeras horas y c. sociales en las ultimas.
problem.addVariables(['S','S2'], [2,5,8,10])
#problem.addVariables(['I','I2'], [1,4,7,10]) #El problema no tendra solucion
problem.addVariables(['L','L1', 'A','A1','J1', 'J'], ['N', 'S', 'E', 'C', 'M', 'I']) #cada profesor imparte dos asignaturas
#problem.addVariables('J', 'E') #El problema no tendra solucion

#La duracion de cada una de las clases es de 1 hora de duracion, en la que solo se puede impartir una unica materia.

#def NotConsecutive (a, b):  #con esta restriccion el problema tampoco tendria solucion
#	if a==2 or a==5 or a==8:
#		return False	
#	if b>a and b<a+2:
#		return True		
   	 
#problem.addConstraint(NotConsecutive, ('E', 'I'))

def notEqual(*args):
    for i in range (len(args)):
   	 for j in range(i+1, len(args)):
   		 if i!=j and args[i]==args[j]:
   			 return False
    return True

problem.addConstraint(AllDifferentConstraint()) 

#2h de Ciencias de la Naturaleza seguidas

def consecutive (a, b):
	if a==2 or a==5 or a==8:
		return False
	else:
		if b>a and b<a+2:
			return True		
   	 
problem.addConstraint(consecutive, ('N', 'N2'))

#La materia de Matematicas no puede impartirse el mismo dia que Ciencias de la Naturaleza e Ingles.
def noImpartir(*args): 
	for i in range(0,10,3):  
    		for j in range(len(args)-2):
   			 if args[j] in range (i,i+3) and (args[4] in range(i,i+3) or args[5] in range(i,i+3)):
				return False

	return True	


problem.addConstraint(noImpartir, ('N','N2','I','I2','M','M2'))


#Matematicas debe impartirse en las primeras horas, y la de Ciencias Sociales en las ultimas.

#problem.addVariables('M', [0,3,6,9])
#problem.addVariables('S', [2,5,8,10])

#Cada profesor debe impartir 2 materias, que son diferentes a las de sus companeros.

problem.addConstraint(AllDifferentConstraint(), ('L','L1', 'A','A1','J','J1'))


def equals (a,b,c,d):
  if (a=='E'or b== 'E'):
	if (c=='S'or d=='S'):
		return True

problem.addConstraint(equals, ('A','A1', 'L','L1'))


#Juan no quiere encargarse de Ciencias de la Naturaleza o de Ciencias Sociales, si algunas de sus horas se imparte a primera hora los lunes y jueves.

def Encargarse(*args):
    	for i in range(len(args)-2):
   		if (args[i]==0 or args[i]==9) and (args[4]==args[i] and args[5]==args[i]): 
			return False
	return True

problem.addConstraint(Encargarse, ('N','N2','S','S2','J','J1'))

resultado= (problem.getSolution()).items()
asignaturas=[]
for i in resultado:
	for j in (['S','S2','M', 'M2','N','N2','C', 'C2','I', 'I2', 'E']):
		if i[0] == j:
			asignaturas.append(i)

asignaturas.sort(key=lambda asignatura: asignatura[1]) #lista de tuplas con las asignaturas ordenadas en orden creciente

print(""" 
L  | M  | X  | J	
-----------------  
{0}  | {3} | {6} | {9}
{1} | {4}  | {7} | {10}
{2} | {5} | {8} 
	   		             """.format(asignaturas[0][0], asignaturas[1][0], asignaturas[2][0], asignaturas[3][0], asignaturas[4][0], asignaturas[5][0], asignaturas[6][0], asignaturas[7][0], asignaturas[8][0], asignaturas[9][0], asignaturas[10][0]))

profesores=[]
for i in resultado:
	for j in (['L','L1', 'A','A1','J','J1']):
		if i[0] == j:
			profesores.append(i)
profesores.sort(key=lambda profesor: profesor[0]) #lista de tuplas con los profesores ordenados en orden creciente
print(
""" 
Andrea imparte {0} y {1}
Juan   imparte {2} y {3}
Lucia  imparte {4} y {5}   """.format(profesores[0][1], profesores[1][1], profesores[2][1], profesores[3][1], profesores[4][1], profesores[5][1]))


