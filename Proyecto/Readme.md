# IE 0117 - Programación Bajo Plataformas Abiertas
### Profesor: Ismael Jiménez Carballo - B94009
### Proyecto de Python

---

## Instrucciones para probar la compilación del código

Este proyecto incluye una variedad de archivos necesarios para su correcta ejecución. Asegúrate de tener todos estos archivos en la misma carpeta:

### Archivos de sonido
- `Ambien_menu.wav`
- `Drop_piece.wav`
- `End_game.wav`
- `Quite_menu.mp3`
- `Start_game.wav`

### Archivos de imagen
- `Exit.png`
- `Star.png`

### Archivo de fuente de letra
- `Pixel_Bug.otf`

### Archivos principales
- `Cliente_P4inrow.py`
- `Server.py`

---

## Configuración del Juego

Para probar el juego, que solo tiene modalidad en línea en subred local, sigue estos pasos:

1. **Enciende el servidor** ejecutando `Server.py`.
2. **Abre dos terminales de bash** y en cada uno ejecuta el archivo `Cliente_P4inrow.py` para compilar dos clientes.

### Consideraciones

- Una vez iniciados los clientes, se mostrarán dos menús que permiten comenzar el juego presionando el botón `Star`.
- **Recomendación:** Conecta primero un cliente al servidor y dale a `Start`. Posteriormente, conecta el segundo cliente y dale a `Start`. Esto es para evitar el sonido ambiente simultáneo de ambos menús, que puede resultar desagradable.
- **Importante:** La funcionalidad está diseñada para funcionar solo en una subred local. Es necesario introducir la IP de la red privada, que puedes obtener mediante el comando `ifconfig`.

