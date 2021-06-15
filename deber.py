
#Ingresar las medidas de las matrices
dimensionx1 = int(input("Ingrese la dimensión x de la matriz 1: "))
dimensiony1 = int(input("Ingrese la dimension y de la matriz 1: "))
dimensionx2 = int(input("Ingrese la dimensión x de la matriz 2: "))
dimensiony2 = int(input("Ingrese la dimension y de la matriz 2: "))

#Ingresar los datos de las matrices
print("Ingresar los datos de la primera matriz")
matriz = []
matriz2 = []
for i in range(dimensionx1):
    matriz.append([])
    for j in range(dimensiony1):
        matriz[i].append(int(input()))


print("Ingresar los datos de la segunda matriz")
for i in range(dimensionx2):
    matriz2.append([])
    for j in range(dimensiony2):
        matriz2[i].append(int(input()))
#Mostrar las matrices
print(matriz2)
print(matriz)

#Multiplicacion de matrices

def producto_matrices(a, b):
    filas_a = len(a)
    filas_b = len(b)
    columnas_a = len(a[0])
    columnas_b = len(b[0])
    if columnas_a != filas_b:
        return None
    # Asignar espacio al producto. Es decir, rellenar con "espacios vacíos"
    producto = []
    for i in range(filas_b):
        producto.append([])
        for j in range(columnas_b):
            producto[i].append(None)
    # Rellenar el producto
    for c in range(columnas_b):
        for i in range(filas_a):
            suma = 0
            for j in range(columnas_a):
                suma += a[i][j]*b[j][c]
            producto[i][c] = suma
    return producto

producto = producto_matrices(matriz, matriz2)
if producto:
    # Imprimir resultado
    for fila in producto:
        for valor in fila:
            # imprimir sin salto de línea. Usando un espacio al final
            print(valor, end=" ")
        print("")
else:
    print("El número de columnas de A es distinto al número de filas de B")