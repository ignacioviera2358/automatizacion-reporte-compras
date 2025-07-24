import pandas as pd
import sqlite3

conn = sqlite3.connect("reporte_compras.db")

cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS compras(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               fecha TEXT, 
               proveedor TEXT,
               producto TEXT,
               cantidad INTEGER,
               precio_unitario REAL,
               precio_total REAL)
               """)

# Limpiar datos previos para evitar duplicados
cursor.execute("DELETE FROM compras")
conn.commit()

#Inicializo los Data Frame para cada reporte de compra
df_LogiMax = pd.read_excel("datos_de_entrada/compras_LogMax.xlsx")
df_MegaTools = pd.read_excel("datos_de_entrada/compras_MegaTools.xlsx")
df_NovaIndustrias = pd.read_excel("datos_de_entrada/compras_Nova_Industrias.xlsx")
df_TechParts = pd.read_excel("datos_de_entrada/compras_TechParts.xlsx")
df_compra_con_error = pd.read_excel("datos_de_entrada/compras_con_error.xlsx")

#Limpio espacios en blanco que puedan haber por error
for df in [df_LogiMax, df_MegaTools, df_NovaIndustrias, df_TechParts, df_compra_con_error]:
    df.columns = df.columns.str.strip()


#Se validan que todos los campos de los reportes sean validos

LogiMaxValido = False
MegaToolsValido = False
NovaIndustriasValido = False
TechPartsValido = False
compra_error_Valido = False

dataFrames = []


def reporteVaLido(reporte, nombre_proveedor):
    for index, fila in reporte.iterrows(): 
        fecha = fila["Fecha"]
        proveedor = fila["Proveedor"]
        producto = fila["Producto"]
        cantidad = fila["Cantidad"]
        precio_unitario = fila["PrecioUnitario"]
        precio_total = fila["PrecioTotal"]

        try: 
            fecha_validada = pd.to_datetime(fecha, dayfirst=True, errors="raise")
            fecha_str = fecha_validada.strftime('%Y-%m-%d')  # Convertir a string
            # Se usa .strip() para eliminar espacios al inicio y final del nombre del proveedor
            if (proveedor.strip() == nombre_proveedor) and (isinstance(producto, str)) and (isinstance(cantidad, int)) and (isinstance(precio_unitario, (int, float))) and (precio_unitario > 0) and (isinstance(precio_total, (int, float))) and (precio_total > 0):
                cursor.execute("""
                    INSERT INTO compras(fecha, proveedor, producto, cantidad, precio_unitario, precio_total) VALUES (?, ?, ?, ?, ?, ?)
                               """, (fecha_str, proveedor.strip(), producto, cantidad, precio_unitario, precio_total))
                conn.commit()
                
            else:
                print(f"Fila {index} falló:")
                
                return False  # Si alguna fila es inválida, retorna False

        except Exception as e: 
            print(f"ARCHIVO NO VALIDO en fila {index}")
            return False  # Si hay error en fecha, retorna False
    
    dataFrames.append(reporte)
    return True  # Si todas las filas son válidas, retorna True



#Validacion de reportes
LogiMaxValido = reporteVaLido(df_LogiMax, "LogiMax")
MegaToolsValido = reporteVaLido(df_MegaTools, "MegaTools")
NovaIndustriasValido = reporteVaLido(df_NovaIndustrias , "NovaIndustrias")
TechPartsValido = reporteVaLido(df_TechParts, "TechParts")
#Va a dar false porque es el reporte con errores
compra_error_Valido = reporteVaLido(df_compra_con_error, "ACME Supplies")


df_final = pd.read_sql_query("SELECT fecha, proveedor, producto, cantidad, precio_unitario, precio_total FROM compras", conn)
df_final.to_excel("reporte_final.xlsx", index=False)

conn.commit()
conn.close()
