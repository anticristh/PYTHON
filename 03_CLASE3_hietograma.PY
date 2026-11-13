import pandas as pd
import matplotlib.pyplot as plt

# 1. Leer el archivo Excel del SENAMHI plotear en barras hietograma
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
plt.bar(lluvia_mensual.index, lluvia_mensual["Precipitacion"], width=20, color="cyan")
plt.title("Hietograma de Precipitación Mensual - Tarija Aeropuerto", fontsize=14, fontweight="bold")
plt.xlabel("Fecha", fontsize=12, fontweight="bold")
plt.ylabel("Precipitación (mm)",fontsize=12, fontweight="bold")  # <-- Etiqueta en negrita)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()