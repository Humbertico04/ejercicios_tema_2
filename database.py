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
        
