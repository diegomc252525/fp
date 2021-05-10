#importar limpiado de pantalla
from os import system
import math
system("cls")

#funcion para dar espacios
def d(cadena=""):
	if cadena=="":
		cadena="    " + cadena
	else:
		cadena="     " + cadena
	return cadena

#1)-------------------------------------------------
#funcion de sacar promedio
def promedioJDMC():
	#variables para calcular promedio
	notas=[0.0,0.0,0.0,0.0]
	ponderado=[0.2,0.15,0.15,0.5]
	promedio=0

	#pedir datos y guardarlas en las variables
	i=0
	for n in notas:
		if i==3:
			notas[i]=float(input(d("nota trabajo final: ")))
			break
		notas[i]=float(input(d("nota unidad "+str(i+1)+": ")))
		i=i+1
	
	#calcular el promedio
	i=0
	for s in notas:	
		promedio=s*ponderado[i]+promedio
		i=i+1

	#imprimir el promedio del estudiante
	print(d(),"su promedio es: ",round(promedio,2))

#2)---------------------------------------------------
def calBonoJDMC():
	#variables de datos
	puntos=0
	porcentajes=[0.1,0.4,0.7]
	sueldo=950.0
	bono=0

	#pedir datos
	puntos=int(input(d("cuantos puntos tienes usted: ")))
	sueldoF=input(d("coloque el sueldo minimo o use 950 por defecto: "))
	if sueldoF=='':
		sueldo=950
	else:
		sueldo=float(sueldoF)
	
	#calcular bono
	if 50<=puntos and puntos<=100:
		bono=porcentajes[0]*sueldo
	elif 101<=puntos and puntos<=150:
		bono=porcentajes[1]*sueldo
	elif puntos>=151:
		bono=porcentajes[2]*sueldo

	#mostrar bono
	print(d("su bono que le corresponde: "),bono)
#3)----------------------------------------------------
def vacunaJDMC():
	#variables de datos
	edad=0
	genero=""
	vacuna=""
	#pedir datos
	edad=int(input(d("cual es su edad: ")))
	genero=input(d("cual es su genero F o M: "))

	#logica de vacuna a usar
	if edad>70:
		vacuna="C"
	elif edad>16 and edad<69:
		if genero=="F" or genero=="f":
			vacuna="B"
		if genero=="M" or genero=="m":
			vacuna="A"
	elif edad<=16:
		vacuna="A"

	#mostrar vacuna a usar
	print(d("el tipo de vacuna que se le colocara sera: "),vacuna)

#4)-------------------------------------------------------------
def operacionesBAsicasJDMC():
	#variables de los datos
	#a=num1 b=num2 c=resultado
	a=0.0
	b=0.0
	c=0.0
	operacion=""
	null=0

	#pedir datos
	a=float(input(d("primer numero: ")))
	b=float(input(d("segundo numero: ")))
	operacion=str(input(d("operacion a realizar : ")))

	#calcular la operacion basica
	if operacion=="+":
		c=a+b
	elif operacion=="-":
		c=a-b
	elif operacion=="*":
		c=a*b
	elif operacion=="/":
		if b==0:
			null=1
		else:
			c=a/b
	elif operacion=="^":
		c=math.pow(a,b)
	else:
		null=1
		print(d("operacion no valida"))


	#mostrar resultado de la operacion
	if null==0:
		print(d("resultado de la operacion "),a,operacion,b," = ",c)
	else:
		print(d("resultado de la operacion no existe"))



#5)-----------------------------------------
#seleccion de ejercicios:
def eleccion(a):
	if numero==1:
		promedioJDMC()
	elif numero==2:
		calBonoJDMC()
	elif numero==3:
		vacunaJDMC()
	elif numero==4:
		operacionesBAsicasJDMC()
	else:
		print("no existe ese funcion")

while True:
	print("Menu",d("0 para salir\n"))
	numero=int(input(d("1)calcular promedio\n")+d("2)calcular bono\n")+d("3)dar tipo de vacuna\n")+d("4)operaciones basicas\n")+d("opcion: ")))
	if numero==0:
		break
	while True:
		system("cls")
		print("PROBLEMA",numero)
		eleccion(numero)
		letra=str(input("menu: cualquier tecla                  reiniciar: \"r\"   : "))
		system("cls")
		if letra!="r":
			break
