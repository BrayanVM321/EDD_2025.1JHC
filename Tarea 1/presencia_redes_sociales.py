import pandas as pd

# leer el archivo CSV
archivo = "Presencia Redes Sociales - Presencia Redes Sociales.csv"
datos = pd.read_csv(archivo)

# convertir todas las columnas de interés a números
columnas_meses = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO"]
for columna in columnas_meses:
    datos[columna] = pd.to_numeric(datos[columna], errors="coerce")

# diferencia de seguidores en twitter 
diferencia_seguidores_twitter = datos.loc[datos["CONCEPTO"] == "SEGUIDORES", "JUNIO"].values[0] - datos.loc[datos["CONCEPTO"] == "SEGUIDORES", "ENERO"].values[0]
print(f"Diferencia de seguidores en Twitter entre enero y junio: {diferencia_seguidores_twitter}")

# Calcular el promedio de crecimiento de twitter y Facebook entre enero y junio
promedio_crecimiento_twitter = datos.loc[datos["CONCEPTO"] == "SEGUIDORES", ["ENERO", "JUNIO"]].mean(axis=1).values[0]
promedio_crecimiento_facebook = datos.loc[datos["CONCEPTO"] == "ME GUSTA", ["ENERO", "JUNIO"]].mean(axis=1).values[0]
print(f"Promedio de crecimiento de Twitter entre enero y junio: {promedio_crecimiento_twitter}")
print(f"Promedio de crecimiento de Facebook entre enero y junio: {promedio_crecimiento_facebook}")

# Calcular el promedio de Me gusta de YouTube, Twitter y Facebook
promedio_me_gusta_youtube = datos.loc[datos["CONCEPTO"] == "ME GUSTA", "ENERO":"JUNIO"].mean(axis=1).values[0]
promedio_me_gusta_twitter = datos.loc[datos["CONCEPTO"] == "RETUITS", "ENERO":"JUNIO"].mean(axis=1).values[0]
promedio_me_gusta_facebook = datos.loc[datos["CONCEPTO"] == "IMPACTOS", "ENERO":"JUNIO"].mean(axis=1).values[0]
print(f"Promedio de 'Me gusta' en YouTube: {promedio_me_gusta_youtube}")
print(f"Promedio de 'Me gusta' en Twitter: {promedio_me_gusta_twitter}")
print(f"Promedio de 'Me gusta' en Facebook: {promedio_me_gusta_facebook}")

# validar que es un mes
def pedir_mes(mensaje):
    while True:
        mes = input(mensaje).upper()
        if mes in columnas_meses:
            return mes
        else:
            print("Por favor, ingrese un mes válido.")

# permite calcular entre meses seleccionados por teclado 
mes_inicio = pedir_mes("Ingrese el mes de inicio (ENERO a JUNIO): ")
mes_fin = pedir_mes("Ingrese el mes de fin (ENERO a JUNIO): ")
diferencia_visualizaciones_youtube = datos.loc[datos["CONCEPTO"] == "VISUALIZACIONES", mes_fin].values[0] - datos.loc[datos["CONCEPTO"] == "VISUALIZACIONES", mes_inicio].values[0]
print(f"Diferencia de visualizaciones en YouTube entre {mes_inicio} y {mes_fin}: {diferencia_visualizaciones_youtube}")
