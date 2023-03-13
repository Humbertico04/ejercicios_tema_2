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
        vector = Punto(coordenada_x, coordenada_y)
        return vector
    def vector_str(self, punto):
        return f"El vector resultante de {self} --> {punto} = {self.vector(punto)}"

    def distancia(self, punto):
        distancia = math.sqrt((punto.x - self.x)**2 + (punto.y - self.y)**2)
        return distancia
    def distancia_str(self, punto):
        return f"La distancia entre {self} y {punto} = {self.distancia(punto)}"

class Rectangulo:
    def __init__(self, punto_inicial=Punto(), punto_final=Punto()):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    def base(self):
        base = abs(self.punto_final.x - self.punto_inicial.x)
        return base
    def base_str(self):
        return "La base del rectángulo formada por los puntos de su diagonal {} y {} es {}".format(self.punto_inicial, self.punto_final, self.base())

    def altura(self):
        altura = abs(self.punto_final.y - self.punto_inicial.y)
        return altura
    def altura_str(self):
        return "La altura del rectángulo formada por los puntos de su diagonal {} y {} es {}".format(self.punto_inicial, self.punto_final, self.altura())
    
    def area(self):
        area = self.base() * self.altura()
        return area
    def area_str(self):
        return "El area del rectángulo formada por los puntos de su diagonal {} y {} es {}".format(self.punto_inicial, self.punto_final, self.area())
