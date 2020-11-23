##estudiantes=int(input("..."))
##presupuesto=int(input(".."))  #50 90 100
##profesores=input("...")
##
##duracion=0
##
##
##if estudiantes >0 and estudiantes<=3:
##    duracion=3
##elif estudiantes>3 and estudiantes<=5:
##    duracion=4
##elif estudiantes>5:
##    edad=eval(input("ingrese la edad promedio:"))
##    duracion= estudiantes* (edad /10)
##elif estudiantes==0:
##    print("No se hace el proyecto sin estudiantes")
##else:
##    print("error")
##
##if presupuesto<90:
##    duracion=duracion+3

#Modelo computacional
#Sistema: Que organismo pertenece la secuencia
#Entradas: secuencia(variable, tipo cadena)
#Salidas: organismo (variable, tipo cadena)
#Constantes:
#CitC_humano:'AGDVEKGKKIFIMKCSQCHTVEKGGKHKTGPNLHGLFGRKTGQA'
#CitC_gorila:    'AGDQEKGKKIFIMKCSQCHTVEKGGKHKTGPNLHGLFGRKTGQA'
#CitC_pollo:     'AGDIEKGKKIFVQKCSQCHTVEKGGKHKTGPNLHGLFGRKTGQA'
#Algortimo:
#1) pedir secuencia
#2) declaro las constantes
#3) condicional:  SI secuencia == CitC_humano ENTONCES organismo="humano"
#                 SI secuencia == CitC_gorila ENTONCES organismo="gorila"
#                 SI secuencia == CitC_pollo ENTONCES organismo="pollo"
#                SINO imprimo "organismo no definido"
#4) imprimo organismo
#implementacion

secuencia=input("ingrese una secuencia: ")
CitC_humano="AGDVEKGKKIFIMKCSQCHTVEKGGKHKTGPNLHGLFGRKTGQA"
CitC_gorila="AGDQEKGKKIFIMKCSQCHTVEKGGKHKTGPNLHGLFGRKTGQA"
CitC_pollo="AGDIEKGKKIFVQKCSQCHTVEKGGKHKTGPNLHGLFGRKTGQA"

if secuencia== CitC_humano:
    organismo="humano"
    print(organismo)
else:
    print("no definido")
    
#comentario nuevo
