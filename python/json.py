names = int(input('Ingresa el numero de nombre: '))
l = {}
for elements in range(names):
    clave = input('Clave: ')
    nombre_clave = 'Nombre'
    nombre_valor = input('Nombre: ')
    edad_clave = 'Edad'
    edad_valor = int(input('Edad: '))
    numero_clave = 'Numero'
    numero_valor = int(input('Numero: '))
    valor = {

    }
    valor[nombre_clave] = nombre_valor
    valor[edad_clave] = edad_valor
    valor[numero_clave] = numero_valor
    l[clave] = valor

print(l)