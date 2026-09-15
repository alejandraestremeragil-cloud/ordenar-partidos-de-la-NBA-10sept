import pandas as pd
def merge_sort(arr, key):  # definimos la clave por la que se va a ordenar
    if len(arr) <= 1:    # caso base: si la lista tiene 1 o menos elementos, ya está ordenada
        return arr

    mid = len(arr) // 2     # parte la lista recursivamente en dos mitades
    left = merge_sort(arr[:mid], key)   # aplica la función recursivamente a la mitad izquierda
    right = merge_sort(arr[mid:], key)  # aplica la función recursivamente a la mitad derecha

    return merge(left, right, key)     # combina las sublistas en una lista ordenada


def merge(left, right, key):
    result = []    # crea una lista vacía para almacenar los elementos ordenados
    i = j = 0     # i para recorrer la lista izquierda y j para recorrer la lista derecha

    while i < len(left) and j < len(right):
        # compara el dato de la izquierda con el de la derecha en orden descendente
        if left[i][key] >= right[j][key]:
            result.append(left[i])
            i += 1
        else:                            # compara los datos y va avanzando posiciones
            result.append(right[j])
            j += 1

    result.extend(left[i:])    # si quedan elementos en la lista izquierda, los añade al final de la nueva lista
    result.extend(right[j:])   # lo mismo para la derecha
    return result


# Cargar los datos completos
df = pd.read_csv("games.csv")

# Calcular la diferencia de puntos
df["DIFF_POINTS"] = (df["PTS_home"] - df["PTS_away"]).abs()

# Convertir todo el conjunto de datos a lista de diccionarios donde cada elemento representa un partido
all_games = df.to_dict("records")

# Ejecutar Merge Sort O(n log n)
sorted_games = merge_sort(all_games, "DIFF_POINTS")

# Mostrar el Top 10 de palizas de toda la historia
print(" TOP 10 PALIZAS HISTÓRICAS (Merge Sort O(n log n)) ")
for g in sorted_games[:10]:
    print(
        f"Fecha: {g['GAME_DATE_EST']} | Diferencia: {g['DIFF_POINTS']} pts ({g['PTS_home']} - {g['PTS_away']})"
    )