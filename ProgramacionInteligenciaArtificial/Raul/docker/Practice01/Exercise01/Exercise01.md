Preguntas de seguimiento:

1. ¿Qué hace cada instrucción en el Dockerfile?

    - La instrucción `FROM node:14-alpine` indica la imagen base de la que parte el Dockerfile.
    - La instrucción `WORKDIR /app` cambia el directorio de trabajo a la ruta `/app`.
    - La instrucción `COPY package.json .` copia el archivo local `package.json` al contenedor.
    - La instrucción `RUN npm install` ejecuta el comando `npm install`.
    - La instrucción `COPY . .` todos los archivos locales al contenedor.
    - La instrucción `EXPOSE 3000` expone el puerto 3000 para que pueda ver desde fuera.
    - La instrucción `CMD ["node", "index.js"]` hará que se ejecute el comando `node index.js` cuando se ejecute el
      contenedor.

2. ¿Cómo construirías esta imagen?

    - Para construir la imagen se ejecuta el siguiente comando: ```docker build -t node-exercise01 .```

3. ¿Cómo ejecutarías un contenedor basado en esta imagen?

    - Para ejecutar el contenedor se utiliza el siguiente comando: ```docker run node-exercise01```
