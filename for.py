#el for se utiliza siempre y cuando sepamos la cantidad de veces a iterar algo

# for i in range(0,11):
#     print(i)

# milista = [1,4,62,23,6,4,36,69]
# contador = 0
# for i in milista:
#     if(i == 69):
#         print('alta pose')
#         print('El contador es igual a: ',contador)
#     contador += 1
    

# milistastring = ['vane','chritian','carmen','glinglis']

# for nombre in milistastring:
#     print(nombre)
# for i in [1,2,3]:
#     print("hola", end=" ")
# for i in ["casa","perro"]:
#     print(i)

# email=False
# miEmail=input("Introduce tu direccion de email: ")

# for i in miEmail:
#     if(i=="@"):
#         email=True
# if email:
#     print("Email es correcto")
# else:
#     print("El email no es correcto")

contador=0
miEmail=input("Introduce tu direccion de email: ")

while(contador2 < 3):
    for i in miEmail:
        if(i=="@" or i=="."):
        contador=contador+1 ##contador+=1
    if contador==2:
        print("Email es correcto")
    else:
        print("El email no es correcto")













