from os import system
system("cls")

#util
def imp():
	print("\n--------------------------------------------------")
#identacion para txto
def d(cadena=""):
	cadena="       "+cadena
	return cadena

	





#1)--------------------------------------------------------
def fun1():
	
	edad=int(input(d("ponga su edad: ")))

	if edad>=18:
		print(d("Puede votar"))
	else :
		print(d("No puedes votar"))

	

#2)-------------------------------------------------------
def fun2():
	horasT=int(input(d("cuantas horas a trabajado: ")))
	PagoPH=int(input(d("cuanto cobra por hora: ")))
	pago=0;

	if horasT <= 40:
		pago=horasT*PagoPH
	else:
		pago=PagoPH*40
		pago+=(horasT-40)*PagoPH*2
	print(d("pago de la semana: "),pago)

#3)-------------------------------------------------------
def fun3():
	print(d("opciones: Targeta, Chocolates, Flores, Anillo"))
	dinero=float(input(d("cuanto dinero tienes?: ")))
	if dinero<=10:
		print(d("puedes comprar una: Targeta"))
	elif dinero>=11 and 100>=dinero:
		print(d("puedes comprar: Chocolates"))
	elif dinero>=101 and 250>=dinero:
		print(d("puedes comprar unas: Flores"))
	else:
		print(d("puedes comprar un: Anillo"))

#4)-------------------------------------------------------
def fun4():
	hora=int(input(d("que hora es para poder cobrarle?: ")))
	if hora <=2:
		print(d("su costo a pagar seria $5.00"))
	elif hora>2 and hora<=5:
		print(d("su costo a pagar seria $4.00"))
	elif hora>5 and hora<=10:
		print(d("su costo a pagar seria $3.00"))
	elif hora>10:
		print(d("su costo a pagar seria $2.00"))

#5)-------------------------------------------------------
def fun5():
	nom=[["",0],["",0],["",0]]
	i=0
	for n in nom:
		nom[i][0]=str(input(d("nombre: ")))
		nom[i][1]=int(input(d("edad: ")))
		i=i+1
	i=0
	if nom[0][1]<nom[1][1]and nom[0][1]<nom[2][1]:
		print(d(),nom[0][0],": es menor")
		i=1
	elif nom[1][1]<nom[0][1] and nom[1][1]<nom[2][1]:
		print(d(),nom[1][0],": es menor")
		i=1
	elif nom[2][1]<nom[0][1] and nom[2][1]<nom[1][1]:
		print(d(),nom[2][0],": es menor")
		i=1

	if i==0 and nom[0][1]==nom[1][1] and nom[0][1]==nom[2][1]:
		print(d(),"tienen igual edad y son menores: ",nom[0][0], " ,",nom[1][0],", ",nom[2][0])
	elif i==0 and nom[0][1]==nom[1][1]:
		print(d(),"tienen igual edad y son menores: ",nom[0][0], " y ",nom[1][0])
	elif i==0 and nom[1][1]==nom[2][1]:
		print(d(),"tienen igual edad: y son menores ",nom[1][0], " y ",nom[2][0])


#6)-------------------------------------------------------
def fun6():
	costo=int(input(d(" cual es el costo del objeto: ")))
	descuento=0

	if costo>=200:
		descuento=costo*0.15
	elif costo<200 and costo>100:
		descuento=costo*0.12
	elif costo<100:
		descuento=costo*0.10

	print(d(),"su descuento es : ",descuento)
	print(d(),"precio a pagar es: ",costo-descuento)

#7)-------------------------------------------------------
def fun7():
	pass
	print(d("notas de 1 a 10"))
	edad=int(input(d("edad: ")))
	nota=float(input(d("nota: ")))
	pension=0
	if edad>=18:
		if nota>=9:
			print(d("su beca es $2000.00"))
		elif nota>=7.5:
			print(d("su beca es $1000.00"))
		elif nota>=6:
			print(d("su beca es $500.00"))
		else:
			print(d("sigue esforzandote para conseguir una beca"))
	else:
		if nota>=9:
			print(d("su beca es $3000.00"))
		elif nota>=8:
			print(d("su beca es $2000.00"))
		elif nota>=6:
			print(d("su beca es $100.00"))
		else:
			print(d("sigue esforzandote para conseguir una beca"))


#8)-------------------------------------------------------

def fun8():
	sueldo=float(input(d("ingrese su sueldo: ")))
	antiguedad=int(input(d("cual es su antiguedad: ")))
	bono1=0.0
	bono2=0.0

	if antiguedad>2 and antiguedad<5:
		bono1=0.2*sueldo
	elif antiguedad>=5:
		bono1=0.3*sueldo

	if sueldo<1000:
		bono2=sueldo*0.25
	elif sueldo>=1000 and sueldo<=3500:
		bono2=sueldo*0.15
	else:
		bono2=sueldo*0.1

	print(d(),"bono1 : ",bono1,"bono2: ",bono2)
	if bono1>bono2:
		print(d(),"su bono seria: ",bono1)
	else:
		print(d(),"su bono seria: ",bono2)

#9)-------------------------------------------------------
def fun9():
	poliza=str(input(d("Elige la poliza A o B: ")))
	print(d("responda con s/n"))
	bebe=str(input(d("Consume alcohol?: ")))
	lentes=str(input(d("Usa lentes?: ")))
	enfermedades=str(input(d("Tiene enfermedades cardiovasculares o diabeticos: ")))
	edad=int(input(d("Cual es su edad?: ")))
	base1=1200
	base2=950
	cantidad1=base1
	cantidad2=base2
	if poliza=="A" or poliza=="a":
		if bebe=="s":
			cantidad1=cantidad1+base1*0.1
		if lentes=="s":
			cantidad1=cantidad1+base1*0.05
		if enfermedades=="s":
			cantidad1=cantidad1+base1*0.05
		if edad>40:
			cantidad1=cantidad1+base1*0.2
		else:
			cantidad1=cantidad1+base1*0.1
		print(d(),"el presio de su poliza A es: ",cantidad1)
	elif poliza=="B" or poliza=="b":
		if bebe=="s":
			cantidad2=cantidad2+base2*0.1
		if lentes=="s":
			cantidad2=cantidad2+base2*0.05
		if enfermedades=="s":
			cantidad2=cantidad2+base2*0.05
		if edad>40:
			cantidad2=cantidad2+base2*0.2
		else:
			cantidad2=cantidad2+base2*0.1
		print(d(),"El presio de su poliza B es: ",cantidad2)


#10)-------------------------------------------------------
def fun10():
	costoPK=float(input(d("Cuanto cuesta el pasaje del bus por kilometro: ")))
	dinero=float(input(d("Cuanto dinero tiene: ")))
	lugares = [750,800,1200,1800]
	if (costoPK*2*lugares[3])<=dinero:
		print(d("usted podra viajar a: Cancun"))
	elif (costoPK*2*lugares[2])<=dinero:
		print(d("usted podra viajar a: Acapulco"))
	elif (costoPK*2*lugares[1])<=dinero:
		print(d("usted podra viajar a: P.V."))
	elif (costoPK*2*lugares[0])<=dinero:
		print(d("usted podra viajar a: Mexico"))
	else:
		print(d("usted no podra viajar"))
#11)-------------------------------------------------------
#12)-------------------------------------------------------
#13)-------------------------------------------------------
#14)-------------------------------------------------------
#15)-------------------------------------------------------
#16)-------------------------------------------------------
#17)-------------------------------------------------------
#18-------------------------------------------------------
#19)-------------------------------------------------------
#20)-------------------------------------------------------

#3i2
#-------------------------------------------------------




#-----------------------------------------------------------------------
#seleccion
def eleccion(a):
	if numero==1:
		fun1()
	elif numero==2:
		fun2()
	elif numero==3:
		fun3()
	elif numero==4:
		fun4()
	elif numero==5:
		fun5()
	elif numero==6:
		fun6()
	elif numero==7:
		fun7()
	elif numero==8:
		fun8()
	elif numero==9:
		fun9()
	elif numero==10:
		fun10()
	else:
		print("no existe es numero de preguntas")
	"""elif numero==11:
		fun11()
	elif numero==12:
		fun12()
	elif numero==13:
		fun13()
	elif numero==14:
		fun14()
	elif numero==15:
		fun15()
	elif numero==16:
		fun16()
	elif numero==17:
		fun17()
	elif numero==18:
		fun18()
	elif numero==19:
		fun19()
	elif numero==20:
		fun20()
	elif numero==21:
		fun21()"""
	

	


while True:
	print("Menu")
	imp()
	print(d("0 para salir"))
	numero=int(input(d("numero de ejercicio 1-10: ")))
	if numero==0:
		break
	while True:
		system("cls")
		print("PROBLEMA",numero)
		imp()
		eleccion(numero)
		imp()
		letra=str(input("menu: cualquier tecla                  reiniciar: \"r\"   : "))
		system("cls")
		if letra!="r":
			break
	
	
	
