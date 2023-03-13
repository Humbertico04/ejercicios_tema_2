import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return f"El punto {self} pertenece al primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return f"El punto {self} pertenece al segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return f"El punto {self} pertenece al tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return f"El punto {self} pertenece al cuarto cuadrante"
        elif self.x == 0 and self.y != 0:
            return f"El punto {self} se sitúa sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return f"El punto {self} se sitúa sobre el eje X"
        elif self.x == 0 and self.y == 0:
            return f"El punto {self} está sobre el origen de coordenadas"
        
    def vector(self, punto):
        coordenada_x = punto.x - self.x
        coordenada_y = punto.y - self.y
        return f"El vector resultante de {self} --> {punto} = ({coordenada_x},{coordenada_y})"
    
    def distancia(self, punto):
        distancia = math.sqrt((punto.x - self.x)**2 + (punto.y - self.y)**2)
        return f"La distancia entre {self} y {punto} = {distancia}"
    
p1 = Punto(2,3)
p2 = Punto(5,-5)
p3 = Punto(-3,-1)
p4 = Punto(0,0)

print(p1.cuadrante())

print(p1.vector(p2))

print(p1.distancia(p2))