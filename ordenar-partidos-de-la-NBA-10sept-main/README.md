
1. Algoritmo O(n^2) (Bubble Sort)

Cómo funciona: Compara los elementos de dos en dos y los va intercambiando. Para ordenar una lista, tiene que recorrerla entera una y otra vez.

Problema de eficiencia: Cuantos más datos hay, el trabajo se multiplica al cuadrado. Para 50.000 partidos, necesita hacer 2.500 millones de operaciones. Es tan lento que el ordenador se bloquea si intentas procesar todos los datos juntos.


2. Algoritmo O(n log n) (Merge Sort)

Cómo funciona: Usa la estrategia de "divide y vencerás". Parte la lista por la mitad repetidamente hasta tener trozos pequeños, los ordena y los vuelve a juntar.

Ventaja de eficiencia: El número de operaciones crece de forma muy lenta. Para los mismos 50.000 partidos, solo necesita unas 750.000 operaciones.



3. Conclusión:

Con O(n^2), el ordenador tarda minutos u horas en procesar listas grandes.
Con O(n \log n), procesa exacto el mismo volumen de datos en menos de un segundo.