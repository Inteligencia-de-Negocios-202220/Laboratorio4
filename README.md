# Laboratorio 4 - BI - Grupo 18
Laboratorio 4 realizado por:
- Gabriela Cagua Bolívar - 201812944
- Juan Andrés Méndez Galvis -  20181580138
- Juan Andrés Romero Colmenares - 202013449

## Instrucciones de Despliegue del API

1. **Instalar Python 3.10**  
Python 3.10 es necesario para poder correr la API. Se puede obtener aquí: [Python 3.10](https://www.python.org/downloads/release/python-3108/)

2. **Creación un ambiente virtual**  
Se recomienda la creación de un ambiente virtual para el manejo de dependencias locales del API  
    - `python -m venv .venv` (Windows)
    - `python3 -m venv .venv` (Unix)

3. **Activar el ambiente**

    - `.venv\Scripts\activate` (Windows)
    - `source .venv\bin\activate` (Unix)

4. **Instalar los requerimientos**  
Después de activar el ambiente, se deben instalar los requerimientos del API con el siguiente comando:
    - `pip install -r requirements.txt` (Windows)
    - `pip3 install -r requirements.txt` (Unix)

5. **Ejecutar el API**  
Una vez instalados los requerimientos ya se puede ejecutar el API utilizando los siguientes comandos:
    - `python main.py` (Windows)
    - `python3 main.py` (Unix)

6. **Probar el API**  
El API estará escuchando en el puerto 6969 por defecto, pero se puede cambiar en el archivo `main.py`

Para acceder a él se puede entrar por el navegador a la dirección `http://localhost:6969/`

## Descripción del API y ejemplos de consumo
Endpoints:
- `/` - Página principal
- `/predict` - Endpoint para hacer predicciones
- `/fit` - Endpoint para entrenar el modelo
- `/docs` - Documentación del API
