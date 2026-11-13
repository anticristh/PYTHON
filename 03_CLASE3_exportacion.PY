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

# 3. Formato profesional
plt.figure(figsize=(10, 5))

plt.bar(
    lluvia_mensual.index,
    lluvia_mensual["Precipitacion"],
    color="#1f77b4",
    edgecolor="black",
    width=20
)

plt.title("Hietograma Mensual - Estación Tarija Aeropuerto", fontsize=14, fontweight="bold")
plt.xlabel("Fecha", fontsize=12)
plt.ylabel("Precipitación Acumulada (mm)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.5)

# 4. Exportar imagen de alta calidad
plt.savefig("Hietograma_Tarija.png", dpi=300, bbox_inches="tight")
print("¡Gráfico PNG de alta resolución guardado!")

plt.show()