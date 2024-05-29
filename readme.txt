# **Manual del desarrollador**

A continuación, se dictarán una serie de recomendaciones para la correcta ejecución del
proyecto, permitiendo obtener una copia del mismo en funcionamiento en una máquina
local con los propósitos de continuar con el desarrollo.

* **
## Herramientas recomendadas:

El software y las herramientas que se recogen en la siguiente lista ayudarán a los desarrol-
ladores a conseguir tener una copia funcional en su máquina local. Dichas recomendaciones
están pensadas para una máquina local con el sistema operativo Windows, existiendo
herramientas similares para el resto de sistemas operativos disponibles en el mercado.

* **Docker** (https://www.docker.com/), siendo más recomendable **Docker Desktop** (https://www.docker.com/products/docker-desktop) por su facilidad de uso.
* **Python** (https://www.python.org/)
* **GIT** (http://git-scm.com/)
* **Visual Studio Code** (https://code.visualstudio.com/) u otro editor de texto.

Es necesario que el usuario, que requiera de una copia funcional del proyecto en una
máquina local, instale el software mencionado u similar para su correcto funcionamiento
y poder realizar posibles modificaciones o ampliaciones del mismo sin complicaciones, así
como para poder desplegar una versión de producción.

## Obtención de copia de repositorio:
El usuario que desee obtener una copia del proyecto en su máquina local para realizar
modificaciones o ampliaciones del mismo deberá clonar el repositorio donde está disponible
a través del siguiente comando de Git:

```
git clone https://github.com/tamestevez/tfg_cuidapet.git
```

## Ejecución del proyecto:

Como se ha mencionado en los apartados anteriores, el proyecto está pensado para ser
desplegado de forma automatizada dentro de contenedores de software y, para ello, se
emplea la tecnología de Docker. Por ello es necesario lanzar sentencias de creación y
arranque de contenedores Docker para tener funcional una copia del proyecto.

```
docker - compose -f docker - compose . yaml up -- build
```

El comando anterior implica la ejecución de los contenedores según las sentencias de
configuración recogidas en los ficheros correspondientes, conocidos como Dockerfile y
los terminados con las extensiones *.yaml o *.yml. 

## Gestión de migraciones con Django:

En el entorno local se aplican las migraciones pendientes de forma automática antes de
realizar el arranque de los servicios que conforman el backend de la plataforma. De surgir
algún error por falta de migraciones o realizar cambios en el ORM, que generen cambios
en la base de datos, el usuario debe conectarse al contenedor del backend a través de línea
de comandos o de la herramienta Docker Desktop y ejecutar los comandos recogidos en el
siguiente código para generar las migraciones correspondientes.

```
python manage.py makemigrations
python manage.py migrate
```

Si todo se ha realizado correctamente, la ejecución de los anteriores comandos resultará
en cambios en el esquema de la base de datos y en los ficheros correspondientes situados
dentro de los directorios migrations del proyecto. Dichos archivos deben incluirse al control
de versiones del proyecto, acompañando a los cambios en el código que los han generado.

## Creación de un usuario del tipo superadministrador:

Un usuario superadministrador es un usuario que tiene acceso al panel de administración
de la plataforma que proporciona Django por defecto. Para que un usuario se considere de
este tipo, la variable is_staff del modelo tiene que estar activada, es decir, su valor debe
de ser verdadero. Desde la aplicación web no se puede dar de alta usuarios de este tipo
específico, por ello, es necesario realizarlo a través de la ejecución del siguiente comando
en el terminal del contenedor con el servicio de backend.

```
python manage.py createsuperuser
```

Una vez ejecutado dicho comando, en la misma línea de comandos aparecerá un formulario
para cubrir con la información correspondiente al usuario que se quiere dar de alta en la
plataforma con el rol indicado. Si el alta ha sido correcta, se puede acceder a la URL que
corresponde al panel de administración e introducir las credenciales, comprobando así
que se ha realizado el registro de forma correcta.

## Aplicaciones Django del proyecto:
Como se ha mencionado con anterioridad, el backend está construido a partir del framework
Django, lo que conlleva el uso de aplicaciones para dividir los diferentes módulos o secciones
que conforman el mismo. Dentro del proyecto se encuentran las siguientes aplicaciones
separando así los módulos pertinentes:

* **cuidapet**: considerada la aplicación raíz del proyecto, ya que en ella se recoge toda
la configuración que conforma el backend de la plataforma.
* **insurance_manager**: recoge todo lo referente al módulo conocido como "póliza de
seguro".
* **mecidal_manager**: se corresponde con la sección "médica" de la plataforma.
* **pet_manager**: contiene todo relacionado con el módulo de "animales".
* **users_manager** : engloba la sección de "usuario" en la aplicación web.

Como se puede observar en el código, las aplicaciones de Django, se corresponden con
carpetas dentro del directorio raíz del backend (django/cuidapet/) y, por lo tanto, contienen
dentro de sí mismas más directorios o ficheros. Los más importantes dentro de cada
aplicación son:

* **migrations**: contiene los archivos correspondientes a las migraciones a los cambios
realizados en los modelos de la plataforma.
* **serializers**: procesadores automáticos para la traducción de estructuras de datos o
objetos a un formato almacenables y viceversa.
* **admin.py**: contiene la información, funcionalidades, etc., para la construcción del
panel de administración de Django.
* **models.py**: contiene los modelos de las entidades necesarias para la plataforma, es
decir, consta de los modelos basados en fuentes únicas y definitivas de información
sobre los datos que conforman la plataforma.
* **views**: recoge los Endpoints con funcionalidades para el funcionamiento de la
plataforma.

## Comandos útiles

* Visualizar la lista de volumenes existentes:  ``` docker volume ls ```
* Borrar los contenedores:  ```docker rm -f $(docker ps -a -q) ```
* Borrar volumenes existentes: ``` docker volume rm $(docker volume ls -q) ```
* Copiar archivos del entorno de Windows al entorno de Linux: ```cp /mnt/ruta_origen_archivo_windows ruta_destino_archivo_linux ```

