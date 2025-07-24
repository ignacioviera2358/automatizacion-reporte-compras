# 🛠️ Automatización de Reportes de Compras con Validación y Base de Datos

Este proyecto automatiza la validación, almacenamiento y consolidación de reportes de compras provenientes de distintos proveedores.  
Procesa archivos Excel, valida los datos por tipo y contenido, los almacena en una base de datos local SQLite y genera un archivo Excel final consolidado directamente desde la base.

Está orientado a departamentos de compras o análisis financiero que trabajen con múltiples reportes externos y necesitan eficiencia, trazabilidad y robustez en la consolidación de datos.

---

## 🚀 Funcionalidades principales

- ✅ Lectura de archivos Excel por proveedor
- ✅ Validación de campos críticos: fechas, tipos numéricos, consistencia de proveedor
- ✅ Inserción de datos válidos en una base SQLite (`.db`)
- ✅ Generación automática de `reporte_final.xlsx` desde la base de datos
- ✅ Control de errores y filas rechazadas
- ✅ Estructura preparada para crecer (consultas por proveedor, filtros, etc.)

---

## 🧰 Tecnologías utilizadas

- **Python 3**
- **pandas** – Para manipulación de datos
- **sqlite3** – Base de datos embebida
- **openpyxl** – Para exportación a Excel

---

## 📁 Estructura del proyecto

```
📦 automatizacion-reporte-compras/
├── 📁 datos_de_entrada/             # Archivos de proveedores (Excel)
│   ├── compras_LogiMax.xlsx
│   ├── compras_MegaTools.xlsx
│   ├── compras_Nova_Industrias.xlsx
│   ├── compras_TechParts.xlsx
│   └── compras_con_error.xlsx
├── 📄 main.py                       # Script principal
├── 📄 reporte_final.xlsx           # Archivo consolidado generado
├── 📄 reporte_compras.db           # Base de datos SQLite local
└── 📄 README.md                    # Documentación del proyecto
```

---

## ⚙️ Cómo usar el proyecto

1. 📥 Cloná este repositorio o descargalo.
2. 📁 Colocá tus archivos `.xlsx` dentro de la carpeta `datos_de_entrada/`.  
   Los archivos deben tener las columnas:

   - `Fecha`
   - `Proveedor`
   - `Producto`
   - `Cantidad`
   - `PrecioUnitario`
   - `PrecioTotal`

3. 🧪 Ejecutá el script desde la terminal:

```bash
python main.py
```

4. 📄 Se generará automáticamente el archivo `reporte_final.xlsx` con todos los datos **válidos**, extraídos desde la base de datos `reporte_compras.db`.

---

## 📌 Ejemplo de salida (Excel final)

| Fecha       | Proveedor   | Producto       | Cantidad | Precio Unitario | Precio Total |
|-------------|-------------|----------------|----------|------------------|--------------|
| 2025-07-24  | LogiMax     | Monitor LED    | 3        | 200              | 600          |
| 2025-07-25  | MegaTools   | Disco rígido   | 2        | 150              | 300          |

---

## ❌ Ejemplos de errores detectados automáticamente

- Fechas inválidas (`15/13/2025`)
- Texto en campos numéricos (`"cien"` en lugar de `100`)
- Valores negativos o vacíos
- Proveedor inconsistente

---

## 💡 Posibles mejoras futuras

- Exportación de reportes filtrados por proveedor
- Dashboard gráfico con estadísticas
- Registro de errores en archivo `.log`
- Carga de datos desde formularios web o CSV

---

## 👨‍💻 Autor

**Ignacio Viera**  
📍 Montevideo, Uruguay  
📧 ignacioviera2358@gmail.com  
💼 Estudiante de Ingeniería en Sistemas  
🎯 Enfocado en automatización, análisis de datos y soluciones prácticas para empresas

---

## 🧪 Licencia

Este proyecto es de uso libre para fines educativos y profesionales. Podés modificarlo, mejorarlo y reutilizarlo.
