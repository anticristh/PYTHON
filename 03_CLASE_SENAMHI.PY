# 1. iMPORTACIÓN DE LIBRERÍAS
import pandas as pd # Se importa la librería pandas para el manejo de datos en estructuras como Series y DataFrames

# 2. Creación de una Serie (Una sola columna, como un vector de precipitaciones)
serie_precip = pd.Series([0.0, 12.5, 5.0, 0.0], name="Precipitacion_mm")

print("--- Ejemplo de Serie ---")
print(serie_precip)


# 3. Creación de un DataFrame (Tabla completa bidimensional)
datos = {
    "Fecha": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04"],
    "Precipitacion_mm": [0.0, 12.5, 5.0, 0.0],
    "Estacion": ["Tarija_Aero", "Tarija_Aero", "Tarija_Aero", "Tarija_Aero"]
}

df_ejemplo = pd.DataFrame(datos)
print("\n--- Ejemplo de DataFrame ---")
print(df_ejemplo)

import pandas as pd

# Lectura de un archivo Excel del SENAMHI
# El parámetro skiprows=11 omite las primeras 11 filas de encabezado/metadatos
df = pd.read_excel('datos_senamhi_real.xlsx', sheet_name='datos_senamhi_real', skiprows=11)

print("\n--- Primeras 5 filas del registro ---")
print(df.head())
print(df)
