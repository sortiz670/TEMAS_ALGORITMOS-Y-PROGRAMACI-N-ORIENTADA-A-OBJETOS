# 1.Crear una clase Student que tiene los siguientes atributos: name, age y grades (una lista de números)

# Definir la clase Estudiante
class Estudiante:
    def __init__(self, nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas

    def add_notas(self, nueva_nota):
        self.notas.append(nueva_nota)

    def average_notas(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def __str__(self):
        return f"Estudiante: {self.nombre}, Edad: {self.edad}, Notas: {self.notas}"


# Lista de diccionarios de estudiantes
estudiantes_dict = [
    {
        "nombre": "Juan",
        "edad": 20,
        "notas": [90, 85, 88, 92]
    },
    {
        "nombre": "Maria",
        "edad": 22,
        "notas": [85, 90, 78, 85]
    },
    {
        "nombre": "Pedro",
        "edad": 21,
        "notas": [88, 82, 90, 78]
    }
]

# Umbral para filtrar estudiantes por nota promedio
umbral = 85

# List comprehension para crear una lista de objetos Estudiante
estudiantes = [Estudiante(est["nombre"], est["edad"], est["notas"]) for est in estudiantes_dict]

# Dictionary comprehension para crear un diccionario con estudiantes que tienen nota promedio por encima del umbral
estudiantes_filtrados_dict = {
    estudiante.nombre: estudiante for estudiante in estudiantes if estudiante.average_notas() >= umbral
}

# Imprimir el diccionario de estudiantes filtrados
for nombre, estudiante in estudiantes_filtrados_dict.items():
    print(nombre, ":", estudiante)
