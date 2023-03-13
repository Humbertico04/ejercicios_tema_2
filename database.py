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

class Rectangulo:
    def __init__(self, punto_inicial=Punto(), punto_final=Punto()):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    def base(self):
        base = abs(self.punto_final.x - self.punto_inicial.x)
        return base

    def altura(self):
        altura = abs(self.punto_final.y - self.punto_inicial.y)
        return altura
    
    def area(self):
        area = self.base() * self.altura()
        return area
    
    
p1 = Punto(2,3)
p2 = Punto(5,-5)
p3 = Punto(-3,-1)
p4 = Punto(0,0)

print(p1.cuadrante())
print(p1.vector(p2))
print(p1.distancia(p2))

rec1 = Rectangulo(p1,p2)
print(rec1.base()) # f"La base del rectángulo formada por los puntos de su diagonal {self.punto_inicial} y {self.punto_final} es {base}"
print(rec1.altura()) # f"La altura del rectángulo formada por los puntos de su diagonal {self.punto_inicial} y {self.punto_final} es {altura}"
print(rec1.area())