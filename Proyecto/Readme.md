## IE 0117 - Programación Bajo PLataformas Abiertas
## Ismael Jimenez Carballo - B94009
## Proyecto de Python


## Intrucciones para probar la compilación del código
> hay una gran variedad de archivos necesarios para la compilación que es necesario 
> que esten en la misma carpeta:
# Archivos de sonidos:
* Ambien_menu-wav
* Drop_piece.wav
* End_game.wav
* Quite_memu.mp3
* Start_game.wav 
# Archivos de imagen
* Exit.png
* Star.png
# Archivo de fuente de letra
* Pixel_Bug.otf
# Archivos principales
* Cliente_P4inrow.py
* Server.py

> Para la prueba del juego solo tiene una modalidad en linea de subred local, por lo que se debe 
> primero encender el server compilando el archivo Server.py. Luego se debe abrir dos
> terminales de bash diferentes y compilar solo dos clientes con el archivo Cliente_P4inrow.py.
> Una vez ya dentro se van a desplegar los dos menus los cuales permiten empezar el juego con el boton
> Star. 
- Nota: se recomienda conectar solo un cliente al server y darle a Start, luego conectar al segundo y darle Start, 
- principalmente porque el sonido ambiente de ambos menus al mismo tiempo no es agradable.
- Nota: la funcionalidad es para una sub red local solamente por lo que es necesario poner la IP de la red privada
- que se puede obtener con el comando ifconfig y poner la IP correspondiente.