import pandas as pd
import matplotlib.pyplot as plt

# === 1. LEER EL ARCHIVO REAL DEL SENAMHI ===
# skiprows=11: Ignoramos el carimbo/membrete de las primeras 11 filas
# sheet_name="datos_senamhi_real": Nombre de la hoja dentro del libro Excel
df = pd.read_excel(
    "datos_senamhi_real.xlsx",
    sheet_name="datos_senamhi_real",
    skiprows=11
)

# Convertimos la columna FECHA a formato fecha (día/mes/año) y la establecemos como índice
df["FECHA"] = pd.to_datetime(df["FECHA"], dayfirst=True)
df.set_index("FECHA", inplace=True)

# Rellenamos los vacíos (NaN) con 0.0
df_limpio = df.fillna(0.0)

print("Datos cargados correctamente:")
print(df_limpio.head())


import pandas as pd
import matplotlib.pyplot as plt

# 1. Leer el archivo Excel del SENAMHI
df = pd.read_excel(
    "datos_senamhi_real.xlsx",
    sheet_name="datos_senamhi_real",
    skiprows=11
)

# Convertir FECHA a formato datetime (día/mes/año) y asignarla como índice
df["FECHA"] = pd.to_datetime(df["FECHA"], dayfirst=True)
df.set_index("FECHA", inplace=True)

# 2. Agrupamos por mes ('ME' = Month End; con respaldo 'M' para versiones anteriores de pandas)
try:
    lluvia_mensual = df[["Precipitacion"]].fillna(0.0).resample("ME").sum()
except ValueError:
    lluvia_mensual = df[["Precipitacion"]].fillna(0.0).resample("M").sum()

# 3. Hietograma de barras
plt.bar(lluvia_mensual.index, lluvia_mensual["Precipitacion"], width=20, color="blue")
plt.title("Hietograma de Precipitación Mensual - Tarija Aeropuerto")
plt.xlabel("Fecha")
plt.ylabel("Precipitación (mm)")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()