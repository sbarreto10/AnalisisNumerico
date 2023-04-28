import matplotlib.pyplot as plt



# PREPARADO PREVIO DE A, b y x

# A_n es una lista con las matrices A ∈ R[nxn] (desde la de R3x3 hasta la de R12x12)
A_n = []
# exactos es una lista con los x exactos ∈ Rn (desde el de R3 hasta el de R12)
exactos = []
# b_n es una lista con los vectores b ∈ Rn (desde el de R3 hasta el de R12)
b_n = []

for n in range(3, 13):

  A, x = nueva_tabla((n,n)), nueva_tabla((n,1))

  # Llenado de A
  for i in range(1,n+1):
    for j in range(1,n+1):
      editar_celda(A, (i,j), 1/(i+j-1))

  # Llenado de x
  for i in range(1, n+1):
    elemento = math.cos((2*math.pi)/(n-1))*(i-1)
    editar_celda(x, (i,1), round(elemento, 15))

  # Cálculo de b
  b = matriz_por_vector(A, x, n)

  A_n.append(A)
  b_n.append(b)
  exactos.append(x)
  

  
# a) MÁXIMA CANTIDAD DE DECIMALES CON DOBLE PRECISIÓN
  
prec = [pow(10, -n) for n in range(32)]

print("Hallando máxima cantidad de decimales con doble precisión...")
print("\n\n\n\n\n")
hallar_maxima_precision(prec, 1)
print("\n\n\n\n\n")



# b) ESTIMACIÓN DE X POR GAUSS CON DOBLE PRECISIÓN

print("Estimando solución por Gauss con doble precisión...")
print("\n\n\n\n\n")
estimados_2p = [resolver_por_Gauss(A_n[i], b_n[i]) for i in range(10)]



# c)a) MÁXIMA CANTIDAD DE DECIMALES CON SIMPLE PRECISIÓN

prec = [pow(10, -n) for n in range(32)]

print("Hallando máxima cantidad de decimales con simple precisión...")
print("\n\n\n\n\n")
hallar_maxima_precision(prec, 1, 8)
print("\n\n\n\n\n")



# c)b) ESTIMACIÓN DE X POR GAUSS CON SIMPLE PRECISIÓN

print("Estimando solución por Gauss con simple precisión...")
print("\n\n\n\n\n")
estimados_1p = [resolver_por_Gauss(A_n[i], b_n[i], 8) for i in range(10)]



# d) GRÁFICOS DE COMPARACIONES DE VALORES EXACTOS E INEXACTOS DE LAS COMPONENTES DE LA SOLUCIÓN

fig, axs = plt.subplots(nrows=5, ncols=2, figsize=(10,18), dpi=140, gridspec_kw={'hspace': 0.25, 'wspace': 0.2})

for i, ax in enumerate(axs.flat):
  if i > 9:
    break
  xlim = (0,13)
  ymin , ymax = min(estimados_1p[i][1]), max(estimados_1p[i][1])
  ylim = (-6 if abs(ymin)<5 else ymin-1, 6 if abs(ymax)<5 else ymax+1)
  ax.plot(estimados_1p[i], lw=2.6, label='Simple precisión', linestyle='dashed', marker='o', dashes=(0.75, 0.75), color="red")
  ax.plot(estimados_2p[i], lw=2.5, label='Doble precisión', linestyle='dashed', marker='o', markersize=5, dashes=(0.75, 1.5), color="#01C752")
  ax.plot(exactos[i], lw=2.3, label='Solución exacta', linestyle='dashed', marker='o', markersize=3, dashes=(0.75, 1.25), color="blue")
  ax.grid(True, alpha=0.5)
  ax.set_title(f"n = {i+3}", fontsize=15)
  ax.set_xlim(xlim)
  ax.set_ylim(ylim)
  ax.set_xticks(range(xlim[1]))
  ax.set_yticks(range(int(ylim[0]), int(ylim[1]), int((ylim[1]-ylim[0])/10)))
  ax.legend(fontsize=5)

plt.show()

print("\n\n\n\n\n")



# e) CÁLCULO DEL RESIDUO RELATIVO Y EL ERROR RELATIVO EN SIMPLE Y DOBLE PRECISIÓN

print("Estimando errores relativos y residuos relativos en simple y doble precisión...")
print("\n\n\n\n\n")

# Estimación de los todos los b aproximados con simple precisión
b_1p = [matriz_por_vector(A_n[i], estimados_1p[i], i+3, 8) for i in range(10)]

# Estimación de los todos los b aproximados con doble precisión
b_2p = [matriz_por_vector(A_n[i], estimados_2p[i], i+3) for i in range(10)]

# Estimación de todos los residuos relativos con simple precisión
rr_1p = [variacion_relativa(b_n[i], b_1p[i]) for i in range(10)]

# Estimación de todos los residuos relativos con doble precisión
rr_2p = [variacion_relativa(b_n[i], b_2p[i]) for i in range(10)]

# Estimación de todos los errores relativos con simple precisión
er_1p = [variacion_relativa(exactos[i], estimados_1p[i]) for i in range(10)]

# Estimación de todos los errores relativos con doble precisión
er_2p = [variacion_relativa(exactos[i], estimados_2p[i]) for i in range(10)]

# Creación de la tabla con errores y residuos en diferentes precisiones
tabla_er_rr = [[er_1p[i], er_2p[i], rr_1p[i], rr_2p[i]] for i in range(10)]



# GRÁFICOS DE EVOLUCIONES DE LOS ERRORES Y RESIDUOS RELATIVOS CON DIFERENTES PRECISIONES

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(7.5,7.5), dpi=130, gridspec_kw={'hspace': 0.3, 'wspace': 0.2})

dims = [str(i)+"x"+str(i) for i in range(3,13)]
axs[0,0].plot(dims, rr_2p, lw=2, color="grey")
axs[0,0].set_title('RR Doble precisión', fontsize=16)
axs[0,1].plot(dims, rr_1p, lw=2, color="grey")
axs[0,1].set_title('RR Simple precisión', fontsize=16)
axs[1,0].plot(dims, er_1p, lw=2, color="#4F3F36")
axs[1,0].set_title('ER Simple precisión', fontsize=16)
axs[1,1].plot(dims, er_2p, lw=2, color="#4F3F36")
axs[1,1].set_title('ER Doble precisión', fontsize=16)


for i, ax in enumerate(axs.flat):
  ax.set_xticklabels(dims, rotation=90, fontsize=8) 
  ax.grid(True, alpha=0.5)

plt.show()

print("\n\n\n\n\n")



# f) ESTIMACIÓN DE LOS NÚMEROS DE CONDICIÓN DE CADA MATRIZ USANDO LA FACTORIZACIÓN LU (LU CON SIMPLE PRECISIÓN)

# La idea es:

# A * δx = r   
# 1 ->   (obtener L y U de A en doble precisión): LU(A)
# 2 ->   (obtener residuo absoluto r de A en simple precisión): r = b - A𝑥̃ 

# L * U * δx = r   
# 3 ->   (obtener δy): L * δy = r   
# 4 ->   (obtener δx): U * δx = δy
# 5 ->   (obtener K(A)): K(A) = (‖δx‖/‖𝑥̃‖)*(10^t)

print("Estimando números de condición de las matrices...")
print("\n\n\n\n\n")

# 1 ->   (obtener L y U de A en doble precisión): LU(A)
L_n, U_n = [], []
for i in range(10):
  l, u = LU(A_n[i], 8)
  L_n.append(l)
  U_n.append(u)

# 2 ->   (obtener residuo absoluto r de A en simple precisión): r = b - A𝑥̃ 
r_n = [b_n[i] - b_2p[i] for i in range(10)]

# 3 ->   (obtener [todos los] δy): L * δy = r   
dy_n = [copiar_tabla(r_n[i]) for i in range(10)]
for i in range(10):
  eliminacion_gaussiana(copiar_tabla(L_n[i]), dy_n[i], i+3)

# 4 ->   (obtener [todos los] δx): U * δx = δy
dx_n = [triangulacion_inversa(U_n[i], dy_n[i], i+3) for i in range(10)]

# 5 ->   (obtener K(A)): K(A) = (‖δx‖/‖𝑥̃‖)*(10^t)
K_n = [condicionamiento(dx_n[i], estimados_2p[i], t=15) for i in range(10)] 

# Mostramos los valores
for i in range(10):
  print("K(A ∈", i+3, "x", i+3, ") = ", K_n[i])

print("\n\n\n\n\n")
  
# Graficamos los valores
dims = [str(i)+"x"+str(i) for i in range(3,13)]
plt.plot(dims, [i if i!=0 else 1E-15 for i in K_n], lw=2, label="A", color="red")
plt.title("Estimaciones de K(A ∈ nxn)", fontsize=16)
plt.xticks(dims, rotation=90, fontsize=10)
plt.yscale('log') 
plt.grid(True, alpha=0.5)

plt.show()

print("\n\n\n\n\n")



# ESTIMACIÓN DE LOS NÚMEROS DE CONDICIÓN DE CADA MATRIZ USANDO LA FACTORIZACIÓN LU (LU CON DOBLE PRECISIÓN)

L_n_2p, U_n_2p = [], []
for i in range(10):
  l, u = LU(A_n[i])
  L_n_2p.append(l)
  U_n_2p.append(u)
  
r_n = [b_n[i] - b_2p[i] for i in range(10)] 

dy_n = [copiar_tabla(r_n[i]) for i in range(10)]

for i in range(10):
  eliminacion_gaussiana(copiar_tabla(L_n_2p[i]), dy_n[i], i+3)
  
dx_n = [triangulacion_inversa(U_n_2p[i], dy_n[i], i+3) for i in range(10)]

K_n_b = [condicionamiento(dx_n[i], estimados_2p[i], t=15) for i in range(10)] 



# GRÁFICO LOGARÍTMICO DE COMPARACIÓN ( K ESTIMADOS / K EXACTOS )

K_exactos = [5.2E2, 1.6E4, 4.8E5, 1.5E7, 4.8E8, 1.5E10, 4.9E11, 1.6E13, 5.2E14, 1.7E16]

[str(i)+"x"+str(i) for i in range(3,13)]
plt.plot(dims, K_exactos, lw=3, label="Exacto")
plt.plot(dims, [i if i!=0 else 1E-15 for i in K_n], lw=3, label="Estimado (LU en SP)", color="red")
plt.plot(dims, [i if i!=0 else 1E-15 for i in K_n_b], lw=3, label="Estimado (LU en DP)", color="green", linestyle='dashed', dashes=(1, 2))
plt.title("Comparación entre las estimaciones y los valores exactos de referencia", fontsize=16)
plt.xticks(dims, rotation=90, fontsize=10)
plt.yscale('log') 
plt.grid(True, alpha=0.5)
plt.legend()

plt.show()



print("\n\n\n\n\n")



# GUARDAR TABLAS COMO .csv

guardar_resultados_como_csv(exactos, "exactos.csv")
guardar_resultados_como_csv(estimados_2p, "estimados2p.csv")
guardar_resultados_como_csv(estimados_1p, "estimados1p.csv")
guardar_resultados_como_csv(tabla_er_rr, "tabla_errores_y_residuos.csv")
guardar_resultados_como_csv([K_n], "K.csv")
