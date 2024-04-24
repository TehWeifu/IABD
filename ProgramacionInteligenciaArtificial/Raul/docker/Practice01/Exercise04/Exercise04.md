Preguntas de seguimiento:

1. ¿Cuáles son los beneficios de utilizar redes personalizadas en Docker?
    - Una red personalizada nos permite aislar un entorno del host y otros entornos. De esta forma, se evita que una
      imagen con código malicioso pueda acceder al host.
2. Explica cómo el aislamiento de red puede mejorar la seguridad en aplicaciones Dockerizadas.
    - Al aislar una red, se evita que una imagen pueda acceder a recursos a los que no debería tener acceso ya sea
      porque pertenecen a otra red o al propio host. De esta forma, se puede evitar que o bien por error o de forma
      intencionada, un contenedor puede manipular datos que no debería.
