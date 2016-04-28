class Operacion:
    def datos(self,base,altura):
        self.base=base
        self.altura=altura
    def imprimir(self):
        print(self.resultado)
       

class Rectangulo(Operacion): #Aqui esta la herencia 
    def operar(self):
        self.resultado=self.base * self.altura


class Triangulo(Operacion): #-------
    def operar(self):
        self.resultado=(self.base * self.altura)/2


s=Rectangulo()
s.datos(10,20)

s.operar()
print('La suma es:')
s.imprimir()

r=Triangulo()
r.datos(10,10)
r.operar()
print('La resta es:')
r.imprimir()