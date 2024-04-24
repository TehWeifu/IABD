Preguntas de seguimiento:

1. ¿Por qué es importante la persistencia de datos para un servicio como Redis?
    - Es importante porque Redis es una especie de base de datos, si los datos no se persisten en un volumen se pierden
      al parar el contenedor.

2. Describe cómo configurarías un volumen para otro tipo de servicio, como una base de datos SQL.
    - Para configurar un volumen para una base de datos SQL buscaría en la documentación de esa base de datos dónde se
      guardan los datos. Cuando cree el servicio de la base de datos, indicaría que el volumen creado se debe montar en
      la ruta que indica la documentación.
