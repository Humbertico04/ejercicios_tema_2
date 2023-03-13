import helpers
import database as db

# Experimentación
def iniciar():
    helpers.limpiar_pantalla()

    print("Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla")
    A = db.Punto(2,3)
    B = db.Punto(5,5)
    C = db.Punto(-3,-1)
    D = db.Punto(0,0)
    print("A{}, B{}, C{}, D{}".format(A, B, C, D))

    print("\nConsulta a que cuadrante pertenecen el punto A, C y D.")
    print(A.cuadrante())
    print(C.cuadrante())
    print(D.cuadrante())

    print("\nConsulta los vectores AB y BA")
    print(A.vector_str(B))
    print(B.vector_str(A))

    print("\nConsulta la distancia entre los puntos 'A y B' y 'B y A'")
    print(A.distancia_str(B))
    print(B.distancia_str(A))

    # print("\nCrea un rectángulo utilizando los puntos A y B")
    rectangulo = db.Rectangulo(A,B)

    print("\nConsulta la base, altura y área del rectángulo")
    print(rectangulo.base_str())
    print(rectangulo.altura_str())
    print(rectangulo.area_str())

    print("\nFinaliza la experimentación")