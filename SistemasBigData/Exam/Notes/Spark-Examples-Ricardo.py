# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 21:41:30 2023

@author: Ricardo_Alvaro
"""
#%%
# Definir una lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usar una función lambda para filtrar números pares
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

# Imprimir el resultado
print("Números pares:", numeros_pares)

#%%

# Definir una lista de números
numeros = [1, 2, 3, 4, 5]

# Usar una función lambda para calcular el cuadrado de cada número
cuadrados = list(map(lambda x: x**2, numeros))

# Imprimir el resultado
print("Cuadrados de los números:", cuadrados)

#%%

# Definir una lista de nombres
nombres = ["Juan", "Ana", "Carlos", "María", "Luisa", "Pedro", "Sofía"]

# Usar una función lambda para ordenar por longitud y luego por orden alfabético
nombres_ordenados = sorted(nombres, key=lambda x: (len(x), x))

# Imprimir el resultado
print("Nombres ordenados:", nombres_ordenados)

#%%

from pyspark import SparkContext

# Crear un SparkContext
sc = SparkContext("local", "EjemploRDD")

# Crear un RDD con una lista de números
datos = [1, 2, 3, 4, 5]
rdd = sc.parallelize(datos)

# Transformación: Elevar al cuadrado cada elemento
rdd_cuadrado = rdd.map(lambda x: x**2)

# Acción: Imprimir los resultados
resultado = rdd_cuadrado.collect()
print("Resultado:", resultado)

# Detener el SparkContext
sc.stop()

#%%
from pyspark import SparkContext

# Crear un SparkContext
sc = SparkContext("local", "EjemploRDD")

# Crear un RDD con una lista de números
datos = [1, 2, 3, 4, 5]
rdd = sc.parallelize(datos)

# Transformación: Filtrar números pares
rdd_pares = rdd.filter(lambda x: x % 2 == 0)

# Acción: Imprimir los resultados
resultado = rdd_pares.collect()
print("Números pares:", resultado)

# Detener el SparkContext
sc.stop()


#%%
from pyspark import SparkContext

# Crear un SparkContext
sc = SparkContext("local", "EjemploRDD")

# Crear un RDD con una lista de números
datos = [1, 2, 3, 4, 5]
rdd = sc.parallelize(datos)

# Transformación y Acción: Calcular la suma de los elementos
suma = rdd.reduce(lambda x, y: x + y)

# Imprimir el resultado
print("Suma de los elementos:", suma)

# Detener el SparkContext
sc.stop()


#%%
from pyspark import SparkContext

# Crear un SparkContext
sc = SparkContext("local", "EjemploRDD")

# Crear un RDD con una lista de números
datos = [1, 2, 3, 4, 5]
rdd = sc.parallelize(datos)

# Transformación y Acción: Calcular la suma de los elementos
suma = rdd.reduce(lambda x, y: x + y)

# Imprimir el resultado
print("Suma de los elementos:", suma)

# Detener el SparkContext
sc.stop()


#%%
from pyspark import SparkContext

sc = SparkContext("local", "EjemploGroupBy")
datos = [("A", 1), ("B", 2), ("A", 3), ("B", 4)]
rdd = sc.parallelize(datos)

grupos = rdd.groupBy(lambda x: x[0])
resultado = grupos.mapValues(list).collect()
print("Elementos agrupados:", resultado)

sc.stop()



#%%
from pyspark.sql import SparkSession

# Crear una sesión de Spark
spark = SparkSession.builder.appName("ConteoDePalabras").getOrCreate()

# Leer un archivo de texto distribuido
rdd = spark.sparkContext.textFile("ruta/del/archivo.txt")

# Tokenizar y contar palabras
conteo_palabras = rdd.flatMap(lambda line: line.split(" ")).countByValue()

# Imprimir el resultado
for palabra, conteo in conteo_palabras.items():
    print(f"{palabra}: {conteo}")

# Detener la sesión de Spark
spark.stop()


#%%

from pyspark.sql import SparkSession
from pyspark.sql.functions import window

# Crear una sesión de Spark
spark = SparkSession.builder.appName("ProcesamientoTemporal").getOrCreate()

# Leer datos con información temporal desde un archivo CSV
df = spark.read.csv("ruta/del/archivo.csv", header=True, inferSchema=True)

# Convertir a formato de tiempo
df = df.withColumn("timestamp", df["timestamp"].cast("timestamp"))

# Agrupar por ventanas de tiempo y calcular estadísticas
resultados = df.groupBy(window("timestamp", "1 hour")).agg({"valor": "mean"})

# Mostrar resultados
resultados.show()

# Detener la sesión de Spark
spark.stop()

#%%

from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

# Crear una sesión de Spark
spark = SparkSession.builder.appName("RegresionLineal").getOrCreate()

# Leer datos de un archivo CSV
df = spark.read.csv("ruta/del/archivo.csv", header=True, inferSchema=True)

# Crear un ensamblador de vectores
ensamblador = VectorAssembler(inputCols=["feature1", "feature2"], outputCol="features")

# Transformar los datos
df = ensamblador.transform(df)

# Dividir los datos en conjuntos de entrenamiento y prueba
train_data, test_data = df.randomSplit([0.8, 0.2], seed=123)

# Crear el modelo de regresión lineal
modelo = LinearRegression(featuresCol="features", labelCol="label")

# Entrenar el modelo
modelo_entrenado = modelo.fit(train_data)

# Hacer predicciones en el conjunto de prueba
predicciones = modelo_entrenado.transform(test_data)

# Evaluar el rendimiento del modelo
evaluador = RegressionEvaluator(labelCol="label", predictionCol="prediction", metricName="rmse")
rmse = evaluador.evaluate(predicciones)
print(f"RMSE: {rmse}")

# Detener la sesión de Spark
spark.stop()

#%%


#%%


#%%


#%%