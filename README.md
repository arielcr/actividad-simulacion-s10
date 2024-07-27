# Proyecto de Pruebas Automatizadas con Selenium

Este proyecto contiene un conjunto de pruebas automatizadas para la página web de Wikipedia, utilizando Selenium WebDriver y Python. Las pruebas incluyen la verificación de títulos de página, búsqueda de términos, y la validación de enlaces importantes en la página de Wikipedia.

## Estructura del Proyecto

- `test.py`: Contiene el conjunto de pruebas automatizadas.
- `chromedriver`: Ejecutable del ChromeDriver necesario para ejecutar las pruebas en el navegador Chrome.

## Pruebas Incluidas

1. **Test Case 1**: Verificar que el título de la página principal es correcto.
2. **Test Case 2**: Buscar un término y verificar que la página de resultados muestra el término buscado.
3. **Test Case 3**: Verificar que el enlace "Wikispecies" en el pie de página redirige correctamente.
4. **Test Case 4**: Verificar que se puede cambiar el idioma de la página.
5. **Test Case 5**: Verificar que el enlace a donaciones lleva a la página correcta.
6. **Test Case 6**: Verificar que el enlace del App Store funciona correctamente.

## Requisitos

- Python 3.x
- Selenium
- ChromeDriver

## Instalación

1. Clonar el repositorio desde GitHub:
    ```bash
    git clone https://github.com/tu-usuario/nombre-del-repositorio.git
    cd nombre-del-repositorio
    ```

2. Crear un entorno virtual e instalar las dependencias:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install selenium
    ```

3. Descargar y colocar el ejecutable de ChromeDriver en la ruta especificada en el archivo `test.py`:
    ```plaintext
    /Users/arielorozco/code/chrome/chromedriver
    ```

## Ejecución de las Pruebas

Para ejecutar las pruebas, simplemente corre el archivo `test.py`:

```bash
python test.py
