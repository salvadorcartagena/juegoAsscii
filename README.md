# juegoAsscii
    Proyecto de un juego con codigo Ascci para el curso de Python en Ada_school
    Repositorio
    Creo un repositorio en Github donde se subira y almacenara el proyecto
    primer paso
    crear un mensaje de bienvenida al jugador con el comando input.
    segundo repositorio
    Importar la libreria Readchar, aprender a usarlo.   
    Crear un bucle infinito  con While y solo podra salir presionando la tecla UP...

# Creacion del laberinto

    Se creo un nuevo archivo llamado laberinto.py

    Para iniciar el laberinto importamos las siguientes librerias
    os : Para limpiar pantalla al inicia el laberinto
    readchar : para capturar y poder uyilisar las teclas de flecha arriba, abajo , izquierda , derecha.
    typing: para poder manejar las listas, ya que nuestro laberinto es una cadena.

    Para que sea personalisado le pedimos al jugador ingresar su nombre, a si al final lo felicitara al concluir el laberinto.
    se nos pide completar paredes , a si que defino una funcio completar_paredes , filas y columnas , donde se le indica
    que agregue un '#' a si , todas las filas tengan la misma longitud y las columnas la misma altura.

    Tambien se nos pidio que se convierta la cadena del laberinto en una matriz de caracteres, donde divide la cadena en filas , para despues combertir cada fila  en una lista de caracteres. atraves de la funcion cadena_a_matriz.

    La funcion limpiar laberinto , limpia la pantalla del terminal para que imprima el laberinto y jugar.

    la funcion main_loop es donde se controla la logica del juego , aqui es donde su ubica 
    nuestro jugador '☻' y donde se lee las teclas de navegacion, indicandole , a donde navegara el jugador dentro del laberinto y para que no salga del laberinto las paredes segun su ubicacion px y py ,dentro del laberinto .'#'. Tambien , para que cada vez que pase por el camino definido con '.' ponga un espacio en blanco ' '
    asi actualiza la posicion del jugador y lo muestra nuevamente.

    El laberinto fue creado en https://www.dcode.fr/maze-generator en la medida de 30*30

