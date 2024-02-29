# Matrix 2*2  Listas de Listas
# Ciclo For
matrix = []
for i in range(3):
    matrix.append([])
    
    for j in range(5):
        matrix[i].append(j)
    

print(matrix)

# LIST_COMPREHENSION
matrix_lc = [[j for j in range(5)] for i in range(3)]
print(matrix_lc)


# Ver como se genera la lista contenida
listas_contenidas = [j for j in range(5)]
print(listas_contenidas)

# Ver lista contenedora

matrix_lc = [[] for i in range(3)]
print(matrix_lc)