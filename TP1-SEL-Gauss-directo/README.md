# ANÁLISIS NUMÉRICO I

###### FACULTAD DE INGENIERÍA, UNIVERSIDAD DE BUENOS AIRES
#### TRABAJO PRÁCTICO Nº 1, 1C2023

*Efecto del condicionamiento de la matriz sobre la relación entre residuo
y error al resolver sistemas de ecuaciones lineales por métodos directos*

___

**Introducción**

El concepto de que una solución que satisface el sistema de ecuaciones (o sea que tiene residuo
pequeño) es precisa se encuentra muy arraigado. Sin embargo lo anterior solamente es cierto
si el sistema de ecuaciones se encuentra bien condicionado. Para que se pueda corroborar esta
situación en forma experimental se propone la resolución de sistemas de ecuaciones cuyas
matrices tienen un mal condicionamiento que crece exponencialmente con su dimensión. A su
vez se eligen problemas simétricos y definidos positivos con lo cual se simplifica el trabajo de
programación dado que en este caso no es necesario programar el intercambio de filas en la
eliminación de Gauss. A los efectos de que se pueda cuantificar el error cometido, la solución
es propuesta en el enunciado de modo que el correspondiente vector de términos
independientes pueda calcularse. Asimismo se propone resolver dichos sistemas usando
variables de distinta precisión para observar el efecto sobre el error de redondeo.

___

**Desarrollo**

a) Codificar una rutina que resuelva un sistema de ecuaciones 𝐴 ∙ 𝑥 = 𝑏 por eliminación de
Gauss sin pivoteo utilizando la máxima precisión disponible. Como la cantidad de dígitos
de precisión depende del compilador que se este utilizando, se recomienda estimarla
inicializando una variable en uno, sumándole luego un número pequeño, restándole luego
uno y comparando el resultado con el número pequeño previamente sumado. De esta forma
se encontrará cuál es el número mas pequeño que puede ser sumado a uno. Se considerará
que los resultados obtenidos en este punto correspondan a ”doble precisión”.

&nbsp;
&nbsp;

b) Para 𝑛 = 3, 4, … , 12 resolver un sistema de ecuaciones lineales donde

$$a_{ij} = \frac{1}{i+j-1}$$

El vector de términos independientes será calculado de forma tal que la solución x del sistema
sea:

$$x_i = \cos\left(\frac{2\pi}{n-1} \cdot (i-1)\right) \quad \text{con } i = 1, 2, \ldots, n
$$

&nbsp;
&nbsp;

c) Repetir los dos puntos anteriores utilizando “simple precisión”. Para lograr este efecto,
después de cada cálculo forzar un redondeo a la mitad de dígitos que los utilizados en (a).

&nbsp;
&nbsp;

d) Para cada valor de 𝑛 graficar las componentes de las soluciones numéricas 𝑥̃ obtenidas
utilizando diferentes precisiones, y las de la solución exacta 𝑥 tomando como abscisa el
indice 𝑖.

&nbsp;
&nbsp;

e) Calcular el residuo relativo 𝑟 y el error relativo 𝑒 utilizando las siguientes expresiones:

$$r = \frac{\left\| \mathbf{b} - \mathbf{A} \mathbf{\tilde{x}} \right\|_2}{\left\| \mathbf{b} \right\|_2}$$

$$e = \frac{\left\| \mathbf{\tilde{x}} - \mathbf{x} \right\|_2}{\left\| \mathbf{x} \right\|_2}$$

Presentar estos resultados en una tabla con el siguiente formato:

| n | e simple | e doble | r simple | r doble |
|-|-|-|-|-|
|3|||||
|4|||||
|...|||||
|12|||||

&nbsp;
&nbsp;

f) Estimar el número de condición de la matriz utilizando la expresión empírica

$$K(\mathbf{A}) = \frac{\left\| \delta \mathbf{x} \right\|_2}{\left\| \mathbf{\tilde{x}} \right\|_2} \cdot 10^t$$

utilizando la factorización LU de la matriz calculada en simple precisión y el residuo
absoluto calculado en doble precisión a los efectos de resolver el sistema 𝐴 ∙ 𝛿𝑥 = 𝑟. Si
bien esta expresión es aproximada, con la misma se puede estimar el $\log_{10} K(\mathbf{A})$.
Corroborar los resultados obtenidos con los valores exactos de los números de condición
provistos a continuación:

| n | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|-|-|-|-|-|-|-|-|-|-|-|
|K(A)|5.2E2|1.6E4|4.8E5|1.5E7|4.8E8|1.5E10|4.9E11|1.6E13|5.2E14|1.7E16|

&nbsp;
&nbsp;

g) Discutir los resultados obtenidos utilizando los conceptos teóricos vistos en el curso. Dicho
análisis debería cubrir los siguientes temas:
• La relación entre error, residuo y condicionamiento de la matriz para todos los sistemas
resueltos. Soportar los comentarios con los datos previamente graficados y tabulados.
• Efecto de la precisión adoptada para efectuar los cálculos. 

___

#### El proyecto tiene como objetivo principal la implementación y análisis numérico del método directo de resolución de sistemas de ecuaciones lineales de Gauss. Para facilitar la comprensión y la edición de las operaciones y procedimientos que se llevarían a cabo en el TP, se ha desarrollado una interfaz improvisada en español que emula operaciones con tablas al estilo Excel. Esta interfaz tenía como objetivo evitar que quien manipulara el código tuviera que aprender a manejar estructuras complejas, como dataframes de pandas.
