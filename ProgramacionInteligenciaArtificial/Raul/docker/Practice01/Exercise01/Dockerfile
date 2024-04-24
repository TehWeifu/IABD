# Tarea: Crear un Dockerfile para una aplicación web simple.
# Especificaciones:

# Base: Utiliza node:14-alpine como imagen base.
FROM node:14-alpine

# Trabajo: Establece un directorio de trabajo /app.
WORKDIR /app

# Dependencias: Copia un archivo package.json y ejecuta npm install.
COPY package.json .
RUN npm install

# Código fuente: Copia el resto del código fuente.
COPY . .

# Puerto: Expone el puerto 3000.
EXPOSE 3000

# Comando: Usa npm start para iniciar la aplicación.
CMD ["npm", "start"]
