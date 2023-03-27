# Filtrado de secuencias FASTA

Este programa permite filtrar secuencias en formato FASTA según diferentes criterios:

- Patrón "4C": se filtran todas las secuencias que contengan la secuencia "CCCC".
- Patrón "Patrón alfa": se filtran todas las secuencias que cumplan con el patrón alfa, que consiste en la presencia de dos cisteínas separadas por un número variable de aminoácidos.

El usuario puede indicar el número de espacios entre las dos cisteínas mediante dos cuadros de texto.

## Requisitos

El programa requiere la instalación de Python 3 y las siguientes librerías:
- Biopython
- Tkinter

## Uso

1. Ejecutar el archivo `main.py` con Python 3.
2. Seleccionar el archivo FASTA de entrada y la carpeta de salida.
3. Seleccionar el patrón de filtrado.
4. Opcionalmente, indicar el número de espacios entre las cisteínas para el patrón alfa.
5. Hacer clic en "Iniciar filtrado".

## Archivos

El programa consta de los siguientes archivos:
- `main.py`: archivo principal que contiene la interfaz gráfica y llama a las funciones necesarias.
- `file_utils.py`: archivo que contiene las funciones para seleccionar archivos y carpetas, así como la función para filtrar las secuencias.
- `filters.py`: archivo que contiene las funciones de filtrado según el patrón alfa.

## Compilación

Para compilar el programa en un archivo ejecutable de Windows, se puede utilizar la librería `pyinstaller` con el siguiente comando:
pyinstaller --onefile --noconsole main.py


Esto creará un archivo `main.exe` en la carpeta `dist/`.

## Autor

Este programa ha sido creado por Sergio Chulián Mantel.
