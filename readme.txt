# **Configuración del entorno de desarrollo en WINDOWS**

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas. 

* **
## Pre-requisitos:
* **Docker Desktop** (https://www.docker.com/products/docker-desktop)
* **Visual Studio Code** (https://code.visualstudio.com/)
* **Python** (https://www.python.org/)
* **GIT** (http://git-scm.com/)

## Creación y arranque de los contenedores:

Abrimos otro terminal dentro del mismo VSCode y realizamos el siguiente comando:
```
docker-compose -f docker-compose.yaml up --build
```
Esto hace que los contenedores que conformen el proyecto se construyan sengún los ficheros de configuración (Dockerfile) y arranquen. 
Para comprobar que todo ha ido de forma correcta, se puede ver el estado de los contenedores desde el mismo VSCode (a través de la extensión Docker) o desde la aplicación de escritorio Docker Desktop. 
Si los contenedores que conforman la plataforma están en color verde, su estado y funcionamiento es el correcto. 

## Creación de un SUPERUSUARIO

Abrimos otro terminal dentro del mismo VSCode y realizamos el siguiente comando:
```
docker ps 
```
Este comando nos muestra los contenedores que están corriendo en el momento de su ejecución. 

El siguiente paso es ejecutar:
```
docker exec -it <3_primeros_digitos_container_ID> <1ª_palabra_command_names>
```
Con este comando lo que se consigue es acceder a la consola del contenedor que se desee para poder ejecutar instrucciones dentro del mismo. 
Como lo que se desea es crear un nuevo superusuario, es necesario acceder al contenedor de backend. Una vez dentro, se ejecuta el comando:
```
python manage.py createsuperuser
```
Y se cubre el formulario correspondiente. Una vez creado, si se accede a la URL: **localhost:8000/admin**, y se insertan las creedenciales, si todo se ha realizado correctamente, se accede a la web de gestión del usuario creado. 

** *

## Comandos útiles

* Visualizar la lista de volumenes existentes:  ``` docker volume ls ```
* Borrar los contenedores:  ```docker rm -f $(docker ps -a -q) ```
* Borrar volumenes existentes: ``` docker volume rm $(docker volume ls -q) ```
* Copiar archivos del entorno de Windows al entorno de Linux: ```cp /mnt/ruta_origen_archivo_windows ruta_destino_archivo_linux ```

