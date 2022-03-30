# Calendario escrito en python
<hr>

# Requisitos para ejecutar el archivo .py y .exe
<hr>

Debereís instalar varias librerias para poder ejecutar el archivo .py

<code>pip install platform python-vlc datetime</code>


Para poder tanto el archivo .py como el .exe debereís tener instalado el programa VLC (https://www.videolan.org/vlc/index.es.html)


# Como Funciona
<hr>

1. Ejecutas el archivo con extensión .py o .exe
2. Deberás elegir la segunda opción para registrar un usuario
3. El script te pedirá un usuario y una contraseña, cuando recibe esos datos, el script creará una carpeta con nombre del usuario introducido y varios archivo dentro de la carpeta
4. Entonces nos devolverá a la pantalla del principio, en este punto puedes iniciar sesión con ese usuario o registrar otro
5. Después de iniciar sesión correctamente, puedes añadir una "tarea" presionando 1
6. Si tiene fechas en el archivo calendario.txt, si presionas 2 verás las fechas que tenga ese archivo escrito, en caso de que no haya nada, no mostrará nada
7. Asi funciona el script


<h2>Debes cambiar los permisos de las carpetas para que solo pueda acceder ese usuario y el/los administrador(es) y con el archivo usuarios.txt, debereís hacer lo mismo.</h2>



Para que se os reproduzca cada vez que iniciemos el ordenador, debemos hacer lo siguiente:

1. Tecla Windows + R
2. Debeís escribir shell:startup
3. Entonces, debereís copiar o mover el archivo .bat hacia esa carpeta y modificar la ruta de donde teneís el archivo .py o .exe


# Espero que os sea de utilidad, un saludo.
