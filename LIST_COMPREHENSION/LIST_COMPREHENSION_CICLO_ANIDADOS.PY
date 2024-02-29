
# Ciclo For
nums1 = [1,2,3]
nums2 = [4,5,6]
lista = []

for i in range(3):
    for j in range(3):
        lista.append((nums1[i], nums2[j]))

print(lista)


# List Comprehension
# [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
# [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]
lista1 = [1,2,3]
lista2 = ["a","b","c"]

lista_combinada = [(x,y) for x in lista1 for y in lista2]
print(lista_combinada)

