# #Se utiliza el while siempre y cuando no sepamos la cantidad de iteraciones que necesitamos
# numero = 0
# while(numero < 11):
#     print(numero)
#     numero = numero + 1 #esto es un acumulador, es igual a decir 'numero+=1'


# #otro ejemplo, con if

# bandera = input('Desea iniciar el programa?: ')
# while(bandera == 'si'):
#     print('que onda wachin')
#     bandera = input('Desea continuar con el programa, wachin?: ')


#----------------------- EJERCICIO 1 -------------------------------------
#Escriba un programa que pregunte una y otra vez si desea continuar con el programa, 
# siempre que se conteste exactamente sí (en minúsculas).
# respuesta = input('Desea continuar?: ')

# while respuesta == 'si ' :
#     respuesta = input('Desea continuar?: ')

# nombre = input('Dame nombre: ')
# apellido = input('Dame apellido: ')

# while nombre == 'vane' or apellido == 'moreno':
#     print('entramos al while')
#     break

#--------------------EJERCICO 2-------------------------
#Escriba un programa que pregunte una y otra vez si desea terminar el programa,
# salvo si se contesta exactamente SI (en mayúscula

# respuesta = input("Desea terminar el programa? ")

# while respuesta != "SI":
#     respuesta  = input('Desea continuar?: ')
    
# import math
# numero=input("Digite un numero: ")
# while numero<0:
#     print("Error debe ser un numero postivo")
#     numero=input("Digite otro numero positivo: ")
# print(f"\nSu raiz cuadrada es: {(math.sqrt(numero)):.2f})
# i= 0
# while i<10:
#     print("Hola Mundo")
#     i +=1
i=0
while i<10:
    print(i)
    i +=1
