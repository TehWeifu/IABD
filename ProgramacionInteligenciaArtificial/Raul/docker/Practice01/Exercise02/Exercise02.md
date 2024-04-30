Preguntas de seguimiento:

1. Explica el propósito de cada servicio en el archivo docker-compose.yml.
    - `web`: Este servicio es una aplicación web hecha con Node que hemos creado en el primer ejercicio. Se puede
      acceder a ella en el puerto 3000.
    - `redis`: Este servicio permite almacenar datos de manera sencilla

2. ¿Cómo levantarías todos los servicios con Docker Compose?

    - Para levantar los servicios, ejecutar el comando: `docker-compose up`

3. ¿Cómo detendrías todos los servicios y eliminarías los recursos creados?
    - Para parar los servicios, ejecutar el comando: `docker-compose down`
