import pandas as pd

#Inicializo los Data Frame para cada reporte de compra
df_LogMax = pd.read_excel("datos_de_entrada/compras_LogMax.xlsx")

df_MegaTools = pd.read_excel("datos_de_entrada/compras_MegaTools.xlsx")

df_NovaIndustrias = pd.read_excel("datos_de_entrada/compras_Nova_Industrias .xlsx")

df_TechParts = pd.read_excel("datos_de_entrada/compras_TechParts.xlsx")

df_compra_con_error = pd.read_excel("datos_de_entrada/compras_con_error.xlsx")


#Se validan que todos los campos de los reportes sean validos

LogiMaxValido = False
MegaToolsValido = False
NovaIndustriasValido = False
TechPartsValido = False


def reporteVaLido(reporte, proveedor1):
    for index, fila in reporte.iterrows(): 
        fecha = fila["Fecha"]
        proveedor = fila["Proveedor"]
        producto = fila["Producto"]
        cantidad = fila["Cantidad"]
        precio_unitario = fila["Precio Unitario"]
        precio_total = fila["PrecioTotal"]

        try: 
            pd.to_datetime(fecha)
            # Se usa .strip() para eliminar espacios al inicio y final del nombre del proveedor
            if (proveedor.strip() == proveedor1) and (isinstance(producto, str)) and (isinstance(cantidad, int)) and (isinstance(precio_unitario, (int, float))) and (precio_unitario > 0) and (isinstance(precio_total, (int, float))) and (precio_total > 0):
                continue  # Esta fila es válida, continúa con la siguiente
            else:
                print(f"Validación falló en fila {index}")
                return False  # Si alguna fila es inválida, retorna False

        except: 
            print("ARCHIVO NO VALIDO.")
            return False  # Si hay error en fecha, retorna False
    
    return True  # Si todas las filas son válidas, retorna True




LogiMaxValido = reporteVaLido(df_LogMax, "LogiMax")
print(f"LogiMax válido: {LogiMaxValido}")




        
        

    

