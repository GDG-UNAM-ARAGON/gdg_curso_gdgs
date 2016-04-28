print('Saludar ------------------------')
def saludar(nombre, mensaje="Hola dude"):
		print(mensaje, nombre)


saludar('David')
saludar('Zahid','Hola')


#--------------------------------------------
#--------------------------------------------
#--------------------------------------------
print('Operaciones básicas -----------------')
def suma(x,y):
	return x + y

def resta(x,y):
	return x - y

def multi(x,y):
	return x * y

def div(x,y):
	return x / y

print(suma(2,3))
print(resta(4,2))
print(multi(2,5))
print(div(10,5))
#--------------------------------------------
#--------------------------------------------
#--------------------------------------------
#calcular el total con IVA
print('Precio total --------------------------')
def total(precio,rebaja):
	rebaja = (rebaja/100) * precio
	return (precio + (precio * .15)) - rebaja

p = int(input('Precio del producto: '))
r = int(input('Rebaja: '))
datos = {
	'precio':p,
	'rebaja':r
}
print(total(**datos))