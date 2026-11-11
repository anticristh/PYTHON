
# ==========================================
# ARCHIVO: 04_calculadora.py
# Tema: Cálculo del tiempo de concentración
# Métodos: Kirpich y Giandotti
# ==========================================

# 1. Datos de entrada
longitud_km = 12.5
desnivel_m = 250.0
area_km2 = 45.0

# 2. Conversiones y parámetros
longitud_m = longitud_km * 1000
pendiente = desnivel_m / longitud_m

# 3. Tiempo de concentración - Método Kirpich
tc_kirpich_min = 0.0195 * (longitud_m ** 0.77) * (pendiente ** -0.385)

# Convertir minutos a horas
tc_kirpich_hr = tc_kirpich_min / 60

# 4. Tiempo de concentración - Método Giandotti
tc_giandotti = (4 * (area_km2 ** 0.5) + 1.5 * longitud_km) / (0.8 * (desnivel_m ** 0.5))

# 5. Mostrar resultados
print("Tiempo de concentración - Kirpich:", f"{tc_kirpich_hr:.2f} horas")
print("Tiempo de concentración - Giandotti:", f"{tc_giandotti:.2f} horas")
