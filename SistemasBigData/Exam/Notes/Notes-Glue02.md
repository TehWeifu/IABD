Para realizar una ETL (Extract, Transform, Load) utilizando AWS Glue con un Job Visual, y automatizar su ejecución mediante una función Lambda en respuesta a la carga de archivos en S3, sigue los siguientes pasos:

### 1. Preparación de los datos en Amazon S3

1. **Crear un bucket en S3**: Ve a la consola de Amazon S3 y crea un nuevo bucket, si aún no tienes uno, con un nombre único.
2. **Crear dos carpetas dentro del bucket**: Una para los datos de entrada (`entrada`) y otra para los datos procesados (`procesados`).

### 2. Cargar los datos de ciclistas

1. **Subir el archivo CSV**: Sube tu archivo CSV con los datos de ciclistas a la carpeta `entrada` del bucket S3 creado.

### 3. Crear un Crawler de AWS Glue

1. **Crear un Crawler**: Dirígete a AWS Glue, ve a la sección de Crawlers, y crea uno nuevo que apunte a la carpeta `entrada` de tu bucket de S3. Este Crawler detectará y creará un esquema para tus datos.
2. **Ejecutar el Crawler**: Una vez configurado, ejecuta el Crawler para que los metadatos de tu archivo CSV se almacenen en el Catálogo de Datos de Glue.

### 4. Crear un Job de Glue

1. **Crear un nuevo Job de Glue**: En la consola de AWS Glue, selecciona "Jobs" y luego "Add job". Elige "A new script to be authored by you" y selecciona "Visual" como tipo de script.
2. **Configurar el origen de datos**: Selecciona el origen de datos que el Crawler ha catalogado en el Catálogo de Datos.
3. **Transformar los datos**: Utiliza las herramientas visuales para:
   - Eliminar duplicados.
   - Filtrar las filas donde el campo `Severity` sea igual a "Grave".
4. **Configurar el destino de los datos**: Elige la carpeta `procesados` dentro de tu bucket de S3 como destino de los datos transformados.
5. **Guardar y ejecutar el Job**: Completa la configuración del Job y guárdalo. Puedes ejecutarlo manualmente para probar la transformación.

### 5. Automatizar la ejecución del Job con una función Lambda

1. **Crear una función Lambda**: Ve a la consola de AWS Lambda y crea una nueva función que se dispare en respuesta a eventos de carga de archivos CSV en la carpeta `entrada` de tu bucket S3.
2. **Configurar el trigger**: En la configuración de la función Lambda, selecciona S3 como el origen del evento y especifica el bucket y la carpeta `entrada` como el punto de activación.
3. **Escribir el código de la función**: En el editor de la función, escribe el código necesario para iniciar el Job de Glue cuando se suba un nuevo archivo. Puedes utilizar la SDK de AWS para Python (boto3) para esto.
   ```python
   import boto3

   def lambda_handler(event, context):
       glue = boto3.client('glue')
       job_name = 'tu_nombre_de_job_de_glue'
       glue.start_job_run(JobName=job_name)
   ```
4. **Configurar los permisos de IAM**: Asegúrate de que la función Lambda tenga un rol de IAM con los permisos necesarios para ejecutar Jobs de Glue y acceder al bucket S3.
5. **Apretar el botón de deploy**

### 6. Monitoreo de Jobs y funciones Lambda

- **Monitoreo de Jobs de Glue**: Puedes monitorear el estado de ejecución, historial de ejecuciones, y logs de tus Jobs de Glue directamente desde la consola de AWS Glue.
- **Monitoreo de funciones Lambda**: Utiliza la consola de AWS Lambda y los servicios de CloudWatch para monitorear las invocaciones de tu función, revisar logs, y configurar alertas basadas en métricas específicas.

Con estos pasos, habrás configurado un flujo de trabajo de ETL automatizado que transforma y filtra datos en respuesta a la carga de archivos en S3, todo ello utilizando AWS Glue y AWS Lambda.