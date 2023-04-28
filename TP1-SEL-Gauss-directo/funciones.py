import pandas as pd




# RECIBE DOS LISTAS Y DEVUELVE SU PRODUCTO ESCALAR

def producto_escalar(x,y):
  if len(x) != len(y):
    return None
  sum = 0
  for i in range(len(x)):
    sum += x[i]*y[i]
  return sum




# RECIBE UN NUMERO Y DEVUELVE EL LOG_10 DE SU INVERSO

def max_digitos(x):
  return math.log(1/x if x != 0 else 1E16, 10)




# RECIBE UNA LISTA DE NUMEROS (DE ORDEN NEGATIVO) Y UNA SEMILLA (0)
# ENLISTA LOS RESULTADOS DE SUMARLE Y LUEGO RESTARLE 1 A ESOS NUMEROS
# SE DETIENE CUANDO EL RESULTADO ES NULO

def hallar_maxima_precision(e, i, prec=16):
  a = round(e[i], prec)+1
  a = round(a-1, prec)
  print(str(e[i]) + ": "+ str(a))
  if a == 0:
    return a
  else:
    if hallar_maxima_precision(e, i+1, prec) == 0:
      max_prec = round(max_digitos(e[i]))
      print("Máxima cantidad de decimales = " + str(max_prec))




# RECIBE UN NUMERO Y UNA LISTA
# DEVUELVE UNA NUEVA LISTA MULTIPLICADA POR DICHO NÚMERO

def lista_por_escalar(fila, x):
  return [x*i for i in fila]




# RECIBE DOS LISTAS
# DEVUELVE SU SUMA, O NO DEVUELVE NADA SI NO COINCIDEN SUS LARGOS

def sumar_filas(l1, l2):
  if len(l1) != len(l2):
    return None
  return [l1[i] + l2[i] for i in range(len(l1))]




# RECIBE DOS LISTAS
# DEVUELVE SU RESTA, O NO DEVUELVE NADA SI NO COINCIDEN SUS LARGOS

def restar_listas(l1, l2):
  if len(l1) != len(l2):
    return None
  return [l1[i] - l2[i] for i in range(len(l1))]




# RECIBE:
# TABLA MATRIZ
# TABLA VECTOR
# DIMENSIÓN
# PRECISIÓN (OPCIONAL)
# DEVUELVE EL RESULTADO DE MULTIPLICAR LA MATRIZ POR EL VECTOR EN FORMA DE TABLA

def matriz_por_vector(A,x,n, prec=16):

  b = nueva_tabla((n,1))

  for i in range(1, n+1):
    prod = producto_escalar(tabla_fila(A,i),tabla_columna(x,1))
    editar_celda(b, (i,1), round(prod, prec))

  return b




# WRAPPER RECURSIVO DE LA FUNCIÓN DE LA ELIMINACIÓN GAUSSIANA
# EN CADA ITERACIÓN SE ELIMINAN ELEMENTOS DEBAJO DE LA DIAGONAL PRINCIPAL DE A, MODIFICANDO A y b
# j ∈ ℕ[1,n] {j++}

def _eliminacion_gaussiana(A, b, n, j, prec=16, LU=False, L=None):
  if LU and j == 1:
    L = nueva_tabla((n,n))
  if j > n:
    if not LU:
      return
    else:
      U = copiar_tabla(A)
      for i in range(1,n+1):
        editar_celda(L, (i,i), 1)
        for k in range(i+1,n+1):
          editar_celda(U, (k,i), 0)
      return L, U
  for i in range(j+1, n+1):
    mu = tabla_celda(A, (i,j))/tabla_celda(A, (j,j)) # Multiplicador

    fila_mu = tabla_fila(A, j)[j:] # Fila fija de A (j)
    fila = tabla_fila(A, i)[j:] # Fila a editar de A (i)
    operacion = restar_listas(fila, lista_por_escalar(fila_mu, mu))
    operacion = [round(i, prec) for i in operacion]
    editar_subtabla(A, (i,j+1), (i,n), operacion)

    if not LU:
      b_mu = tabla_celda(b, (j,1))  # Celda fija de b (j)
      b_celda = tabla_celda(b,(i,1)) # Celda a editar de b (i)
      operacion = round(b_celda - mu*b_mu, prec)
      editar_celda(b, (i,1), operacion)
    else:
      editar_celda(L, (i,j), mu)

  return _eliminacion_gaussiana(A, b, n, j+1, prec, LU, L)




# RECIBE:
# -TABLA MATRIZ DE COEFICIENTES
# -TABLA VECTOR DE TÉRMINOS INDEPENDIENTES
# -DIMENSIÓN DEL PROBLEMA
# -NÚMERO DE COLUMNA DE ITERACIÓN
# -PRECISIÓN (OPCIONAL)
# -LU = True (OPCIONAL)
# DEVUELVE UNA DUPLA (L,U) SI SE ACTIVA EL PARÁMETRO LU
# DE LO CONTRARIO, NO DEVUELVE NADA, PERO A y b SE VEN MODIFICADOS

def eliminacion_gaussiana(A, b, n, prec=16, LU=False, L=None):
  if LU:
    return _eliminacion_gaussiana(A, b, n, 1, prec, LU, L)
  else:
    _eliminacion_gaussiana(A, b, n, 1, prec, LU, L)




# WRAPPER RECURSIVO DE LA FUNCIÓN DE LA TRIANGULACION INVERSA
# CADA PASO CALCULA UNA INCÓGNITA Xi
# i ∈ ℕ[n,1] {i--}

def _triangulacion_inversa(A, b, x, n, i, prec=16):
  if i < 1:
    return x

  # Xi = Bi
  xi = tabla_celda(b, (i,1))

  # Xi -= Σ(Aij*Xj) {desde i+1 hasta n}
  for j in range(i+1, n+1):
    Aij_xj = tabla_celda(A, (i,j)) * tabla_celda(x, (j,1))
    xi = xi - Aij_xj

  # ⁂ Xi = Bi - Σ(Aij*Xj)

  # Xi = Xi/Aii
  Aii = tabla_celda(A, (i,i))
  editar_celda(x, (i,1), round(xi/Aii, prec))

  return _triangulacion_inversa(A, b, x, n, i-1, prec)




# RECIBE LAS TABLAS:
# -MATRIZ DE COEFICIENTES TRIANGULAR SUPERIOR 
# -VECTOR DE TÉRMINOS INDEPENDIENTES
# -VECTOR DE INCÓGNITAS (VACÍA)
# -LA DIMENSIÓN DEL PROBLEMA
# DEVUELVE LA SOLUCIÓN DEL VECTOR DE INCÓGNITAS

def triangulacion_inversa(A, b, n, prec=16):
  x = nueva_tabla((n,1))
  return _triangulacion_inversa(A, b, x, n, n, prec)




# RECIBE LAS TABLAS:
# -MATRIZ DE COEFICIENTES (n*n)
# -VECTOR DE TÉRMINOS INDEPENDIENTES (n*1)
# DEVUELVE EL VECTOR DE INCÓGNITAS RESUELTO POR GAUSS (EN FORMA DE TABLA)

def resolver_por_Gauss(coef, indep, prec=16):
  A = copiar_tabla(coef)
  b = copiar_tabla(indep)
  n = tabla_cantidad_filas(A)

  eliminacion_gaussiana(A, b, n, prec)

  # ⁂ A es triangular superior

  x = tabla_columna(triangulacion_inversa(A, b, n, prec), 1)
  return nueva_tabla(data={1: x})




# RECIBE UNA LISTA Y DEVUELVE SU NORMA EUCLIDEANA ( √(Σx_i^2) )

def norma_2(x, i=0, sum=0):
  if i == len(x):
    return math.sqrt(sum)
  sum += pow(x[i],2)
  return norma_2(x, i+1, sum)




# RECIBE UN VECTOR EXACTO (v) Y UN VECTOR APROXIMADO (𝓥), EN FORMA DE TABLAS
# DEVUELVE LA VARIACIÓN RELATIVA (| v - 𝓥 | / | v |)
# ESTA FUNCIÓN SE USA PARA CALCULAR TANTO EL ERROR RELATIVO COMO EL RESIDUO RELATIVO
# Obs: (LA VARIACIÓN RELATIVA DE LA COMPONENTE i SE CALCULA CON EL VALOR EXACTO x_i EN EL DENOMINADOR,
# PARA EVITAR LA DIVISIÓN POR CERO, CUANDO x_i = 0, LO CONVERTIMOS EN UN ɛ PEQUEÑO)

def variacion_relativa(v, v_aprox):
  norma_v = norma_2(tabla_columna(v, 1))
  denom = norma_v if norma_v != 0 else 1E-15
  return norma_2(tabla_columna(v - v_aprox, 1)) / denom




# RECIBE UNA MATRIZ DE COEFICIENTES (EN FORMA DE TABLA) Y DEVUELVE SU FACTORIZACIÓN LU EN FORMA DE DUPLA (L,U)

def LU(coef, prec=16):
  A = copiar_tabla(coef)
  n = tabla_cantidad_filas(A)
  return eliminacion_gaussiana(A, None, n, prec, LU=True)




# RECIBE DOS TABLAS Y DEVUELVE UNA TABLA RESULTADO DE SU MULTIPLICACIÓN MATRICIAL

def multiplicar_matrices(A,B):
  n = tabla_cantidad_filas(A)
  C = nueva_tabla((n,n))
  for i in range(1,n+1):
    B_i = nueva_tabla(data={1: tabla_columna(B,i)})
    A_Bi = matriz_por_vector(A,B_i,n)
    asignar_columna(C,i,A_Bi)
  return C




# RECIBE UN ERROR ABSOLUTO DEL VECTOR SOLUCIÓN Y EL VECTOR SOLUCIÓN (DE ALGÚN SISTEMA Ax = b)
# DEVUELVE EL CONDICIONAMIENTO DE LA MATRIZ A ASOCIADA

def condicionamiento(dx, x, t=16):
  norma_dx = norma_2(tabla_columna(dx, 1))
  norma_x = norma_2(tabla_columna(x, 1))
  escala = pow(10,t)
  norma_x = max(norma_x, 1/escala) if norma_x == 0 else norma_x
  return (norma_dx/norma_x)*escala
