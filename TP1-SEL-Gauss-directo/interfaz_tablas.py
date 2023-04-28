# RECIBE: 
# - EL TAMAÑO DE LA TABLA COMO UNA DUPLA (f,c)
# - UN DICCIONARIO DE LA FORMA {nombre_columna: lista_columna} (OPCIONAL, SINO SE CREA UNA TABLA DE CEROS)
# - UNA LISTA CON LOS NOMBRES DE LAS FILAS (OPCIONAL, SINO SE ENUMERAN CONVENCIONALMENTE)
# - UNA LISTA CON LOS NOMBRES DE LAS COLUMNAS (OPCIONAL, SINO SE ENUMERAN CONVENCIONALMENTE)
# DEVUELVE UNA TABLA CON CELDAS nulas

def nueva_tabla(dim=None, data=None, nombres_filas=None, nombres_columnas=None):
  if data:
    tabla = pd.DataFrame(data=data, dtype=float)
  else:
    tabla = pd.DataFrame(data={i: [0 for j in range(dim[0])] for i in range(dim[1])}, dtype=float)
  if nombres_columnas:
    tabla.columns = nombres_columnas
  else:
    if not data:
      tabla.columns = tabla.columns + 1
  if nombres_filas:
    tabla.index = nombres_filas
  else:
    tabla.index = tabla.index + 1
  return tabla 


# RECIBE UNA TABLA Y DEVUELVE UNA COPIA

def copiar_tabla(tabla):
  return tabla.copy()


# RECIBE: 
# -UNA TABLA
# -LA CELDA COMO UNA DUPLA (f,c)
# -EL NUEVO VALOR A INSERTAR 

def editar_celda(tabla, celda, nuevo):
  tabla.loc[celda[0],celda[1]] = nuevo


# RECIBE: 
# -UNA TABLA
# -EL INICIO DE LA SUBTABLA COMO UNA DUPLA (f,c)
# -EL FIN DE LA SUBTABLA COMO UNA DUPLA (f,c)
# -EL NUEVO VALOR A INSERTAR EN TODAS ESAS CELDAS
def editar_subtabla(tabla, ini, fin, nuevo):
  tabla.loc[ini[0]:fin[0], ini[1]:fin[1]] = nuevo

def editar_subtabla_por_indice(tabla, ini, fin, nuevo):
  tabla.iloc[(ini[0]-1):ini[1], (fin[0]-1):fin[1]] = nuevo


# RECIBE UNA TABLA, UN NOMBRE DE FILA Y UNA LISTA
# ACTUALIZA LA FILA EN LA TABLA CON LA LISTA PASADA

def asignar_fila(tabla, fila, nueva_fila):
  tabla.loc[fila, :] = nueva_fila


# RECIBE UNA TABLA, UN NOMBRE DE COLUMNA Y UNA LISTA
# ACTUALIZA LA COLUMNA EN LA TABLA CON LA LISTA PASADA

def asignar_columna(tabla, columna, nueva_columna):
  tabla.loc[:, columna] = nueva_columna


# RECIBE UNA LISTA DE TABLAS Y DEVUELVE UNA NUEVA TABLA CONCATENÁNDOLAS HORIZAONTALMENTE

def concatenar_tablas_hor(lista_tablas):
  return pd.concat(lista_tablas, axis=1)


# RECIBE:
# -UNA TABLA
# -DOS LISTAS: FILAS Y COLUMNAS (OPCIONALES, DEBE ESPECIFICARSE EL NOMBRE DE LOS PARÁMETROS EN LA LLAMADA)
# Y MODIFICA LOS NOMBRES DE LAS FILAS Y COLUMNAS DE UNA TABLA

def renombrar_tabla(tabla, filas=None, columnas=None):
  if filas:
    tabla.index = filas
  if columnas:
    tabla.columns = columnas


# RECIBE UNA LISTA DE RESULTADOS (VECTORES) Y UN PATH Y GUARDA LOS RESULTADOS EN DICHO PATH

def guardar_resultados_como_csv(res, dir):

  df = pd.DataFrame()

  for i in range(len(res)):
    if type(res[i])==list:
      df = pd.concat([df, pd.Series(res[i])], axis=1)
    else:
      df = pd.concat([df, res[i]], axis=1)

  # Guardar el dataframe en un archivo CSV
  df.transpose().to_csv(dir, index=False, header=False, sep=";")


# RECIBE UNA TABLA Y UN STRING Y LA GUARDA COMO ARCHIVO CSV CON ESE NOMBRE

def tabla_a_csv(tabla, dir):
  tabla.to_csv(dir, index=False)

# RECIBE UNA TABLA Y DEVUELVE SUS DIMENSIONES EN FORMA DE DUPLA

def tabla_dimension(tabla):
  return tabla.shape


# RECIBE UNA TABLA Y UNA CELDA EN FORMA DE DUPLA
# DEVUELVE EL VALOR EN DICHA POSICIÓN

def tabla_celda(tabla, celda):
  return tabla.loc[celda[0],celda[1]]


# RECIBE:
# -UNA TABLA 
# -UN NOMBRE/INDICE DE FILA
# -TRUE (OPCIONAL) INDICANDO SI ES POR INDICE
# DEVUELVE LA FILA EN ESA POSICIÓN EN FORMA DE LISTA

def tabla_fila(tabla, f, por_indice=False):
  return tabla.loc[f,:].tolist() if not por_indice else tabla.iloc[f-1,:].tolist()


# RECIBE:
# -UNA TABLA 
# -UN NOMBRE/INDICE DE COLUMNA
# -TRUE (OPCIONAL) INDICANDO SI ES POR INDICE
# DEVUELVE LA COLUMNA EN ESA POSICIÓN EN FORMA DE LISTA

def tabla_columna(tabla, c, por_indice=False):
  return tabla.loc[:,c].tolist() if not por_indice else tabla.iloc[:,c-1].tolist()


# RECIBE UNA TABLA Y DEVUELVE UNA LISTA ORDENADA CON LOS NOMBRES DE SUS FILAS

def tabla_cantidad_filas(tabla):
  return tabla.index.size


# RECIBE UNA TABLA Y DEVUELVE UNA LISTA ORDENADA CON LOS NOMBRES DE SUS COLUMNAS
def tabla_cantidad_columnas(tabla):
  return tabla.columns.size
