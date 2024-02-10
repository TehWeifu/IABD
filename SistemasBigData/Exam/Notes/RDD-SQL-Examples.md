Aquí tienes los apuntes revisados y corregidos, incluyendo ejemplos para cada sección:

```python
# Importar SparkSession
from pyspark.sql import SparkSession

# Crear una sesión de Spark
spark = SparkSession.builder.appName("EjemploAplicacion").getOrCreate()

# Leer un archivo CSV en un DataFrame
df = spark.read.csv("path/to/file.csv", header=True)

# Registrar el DataFrame como una vista temporal
df.createOrReplaceTempView("vista_temporal")

# Ejecutar una consulta SQL simple
resultado = spark.sql("""
    SELECT * FROM vista_temporal
""")
# El código anterior asume que el archivo CSV y la consulta SQL están correctamente formados.

# Crear una sesión de Spark para cargar un archivo de texto
spark = SparkSession.builder.appName("CargarArchivoTexto").getOrCreate()
file = spark.read.text("path/to/textfile.txt")

# Registrar el DataFrame como una vista temporal
file.createOrReplaceTempView("vista_texto")

# Ejecutar una consulta SQL para seleccionar todo
resultado_texto = spark.sql("SELECT * FROM vista_texto")

# Convertir una columna a tipo date
from pyspark.sql.functions import to_date, col

file = spark.read.text("path/to/textfile.txt")
formattedFile = file.withColumn("fecha", to_date(col("nombre_de_la_columna"), "yyyy-MM-dd"))
formattedFile.show()

# Contar los registros en una tabla
table = spark.table("nombre_de_la_tabla")
count = table.count()
print(f"Cantidad de registros: {count}")

# Filtrar registros en una tabla
filteredTable = table.filter("columna = 'valor'")
filteredTable.show()

# Realizar una operación de agregación
from pyspark.sql.functions import sum

sumColumn = table.select(sum("columna").alias("suma_total"))
sumColumn.show()

# Escribir un DataFrame en un archivo CSV
table.write.csv("path/to/output.csv")

# Unir dos tablas por una columna común
tabla1 = spark.table("nombre_tabla1")
tabla2 = spark.table("nombre_tabla2")

tablaUnida = tabla1.join(tabla2, "columna_comun")
tablaUnida.show()

# Trabajar con GraphFrames
from graphframes import GraphFrame

vertices = spark.createDataFrame([
    ("A", "Alice", 34),
    ("B", "Bob", 36),
    ("C", "Charlie", 30),
    ("D", "David", 29),
], ["id", "name", "age"])

edges = spark.createDataFrame([
    ("A", "B", "friend"),
    ("B", "C", "follow"),
    ("C", "B", "follow"),
    ("C", "D", "friend"),
    ("D", "A", "friend"),
], ["src", "dst", "relationship"])

graph = GraphFrame(vertices, edges)

graph.vertices.show()
graph.edges.show()

followers = graph.edges.filter("relationship = 'follow'").count()
print(f"Número de seguidores: {followers}")
```

He corregido los errores tipográficos y formateado el código para una mejor comprensión. Los ejemplos asumen que los
archivos y tablas existen y están accesibles en la ruta especificada. Además, para el ejemplo de GraphFrames, es
necesario tener el paquete `graphframes` instalado y disponible en el entorno de Spark.
