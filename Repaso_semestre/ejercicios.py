# crear un programa que que me pida la edad de una persona si la edad 
# es mayor o igal a 18 que me muestre un mensaje
#  "eres mayor de edad" en caso contrario que me muestre
# "eres menor de edad"
# edad=int(input('dime tu edad : '))
# if edad >=18:
#     print('eres mayor de edad')
# else:
#     print('eres menor de edad')

# una tienda comercial desea hacer un descuento del 20%, crear un progra que me muestre si el cliente es acreedor 
# teniendo en cuenta los siguientes : si el cliente realiza una compar igual o mayor que 1000 soles 
# mostrar un mensaje que muestre un mesaje que diga "ganaste el descuento de 20% ahora pagaras 
# <mostrarel total de la compra menos el descuento> "
# en caso no supere los 1000 soles entonces mostrar un mesaje que diga 
# 'no aplicas al descuento <mostrar el monto de la compra>'

# precio_compra= int(input('dime el precio que compraste: '))
# if precio_compra>=1000:
#     descuento=precio_compra * 0.2
#     total_con_descuento = precio_compra-descuento
#     print("¡ Ganaste el descuento del 20% ! ahora pagaras:",total_con_descuento,"soles")
# else:
#     print("no aplicas al descuento. el monto del descuento es :",precio_compra, "soles") 

# crear una programa que me pidaq 5 veces un nombre y por cada vez que lo pida muestre la cantidad de veces que ingreso el nombre
# for n in range(1,6):
#         nombre=input("ingrese un nombre: ")
#         print(f"ingresaste {n} veces el nombre")
# crear un programa que pida un numero y lo evalues con el numero premiado si el numero ingresado es el premiado el programa finalizara
# si el numero ingresaso es incorrecto el programa seguira pidiendo
numero_premiado = 95

while True:
    numero_ingresado = int(input("Ingresa un número: "))

    if numero_ingresado == numero_premiado:
        print("¡Felicidades! Has acertado el número premiado.")
        break 
    else:
        print("Número incorrecto. Inténtalo de nuevo.")