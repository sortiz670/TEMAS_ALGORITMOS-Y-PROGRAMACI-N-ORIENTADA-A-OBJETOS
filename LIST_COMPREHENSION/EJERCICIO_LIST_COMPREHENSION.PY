# CICLO FOR
cuadrados = []
for x in range(10):
    cuadrados.append(x**2)

print(cuadrados)

# LIST_COMPREHENSION
# cuadrados_con_lc = expresion for elemento in iterable

cuadrados_con_lc = [x**2 for x in range(10)]
print(cuadrados_con_lc)