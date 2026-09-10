import pandas as pd
def merge_sort(arr, key):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)

    return merge(left, right, key)


def merge(left, right, key):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        # Orden descendente (de mayor a menor diferencia)
        if left[i][key] >= right[j][key]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Cargar los datos completos
df = pd.read_csv("games.csv")

# Calcular la diferencia de puntos
df["DIFF_POINTS"] = (df["PTS_home"] - df["PTS_away"]).abs()

# Convertir todo el conjunto de datos (+50.000 registros) a lista de diccionarios
all_games = df.to_dict("records")

# Ejecutar Merge Sort O(n log n)
sorted_games = merge_sort(all_games, "DIFF_POINTS")

# Mostrar el Top 10 de palizas de toda la historia
print(" TOP 10 PALIZAS HISTÓRICAS (Merge Sort O(n log n)) ")
for g in sorted_games[:10]:
    print(
        f"Fecha: {g['GAME_DATE_EST']} | Diferencia: {g['DIFF_POINTS']} pts ({g['PTS_home']} - {g['PTS_away']})"
    )