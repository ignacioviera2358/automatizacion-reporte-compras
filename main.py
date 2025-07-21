import pandas as pd



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


def reporteVaLido(reporte, nombre_proveedor):
    for index, fila in reporte.iterrows(): 
        fecha = fila["Fecha"]
        proveedor = fila["Proveedor"]
        producto = fila["Producto"]
        cantidad = fila["Cantidad"]
        precio_unitario = fila["PrecioUnitario"]
        precio_total = fila["PrecioTotal"]

        try: 
            pd.to_datetime(fecha, dayfirst=True)
            # Se usa .strip() para eliminar espacios al inicio y final del nombre del proveedor
            if (proveedor.strip() == nombre_proveedor) and (isinstance(producto, str)) and (isinstance(cantidad, int)) and (isinstance(precio_unitario, (int, float))) and (precio_unitario > 0) and (isinstance(precio_total, (int, float))) and (precio_total > 0):
                continue  # Esta fila es válida, continúa con la siguiente
            else:
                print(f"Fila {index} falló:")
                return False  # Si alguna fila es inválida, retorna False

        except: 
            print("ARCHIVO NO VALIDO.")
            return False  # Si hay error en fecha, retorna False
    
    return True  # Si todas las filas son válidas, retorna True



#Validacion de reportes
LogiMaxValido = reporteVaLido(df_LogiMax, "LogiMax")
print(f"LogiMax valido: {LogiMaxValido}")

MegaToolsValido = reporteVaLido(df_MegaTools, "MegaTools")
print(f"MegaTools valido: {MegaToolsValido}")

NovaIndustriasValido = reporteVaLido(df_NovaIndustrias , "NovaIndustrias")
print(f"NovaIndustrias valido: {NovaIndustriasValido}")

TechPartsValido = reporteVaLido(df_TechParts, "TechParts")
print(f"TechParts valido: {TechPartsValido}")

#Va a dar false porque es el reporte con errores
compra_error_Valido = reporteVaLido(df_compra_con_error, "ACME Supplies")
print(f"ACME Supplies validacion: {compra_error_Valido}")






        
        

    

