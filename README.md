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

### Pruebas en vivo
Nosotros desplegamos el API del laboratorio en un servidor público, puedes probarlo en vivo en la siguiente dirección: [http://lab4api.bushidoway.net:6969](http://lab4api.bushidoway.net:6969/docs)

Endpoints:
- `/` - Página principal
- `/predict` - Endpoint para hacer predicciones
- `/fit` - Endpoint para entrenar el modelo
- `/docs` - Documentación del API

## Ejemplos de uso del API
### /predict
El endpoint de predict recibe una lista de elementos para predecir y devuelve un arreglo que contiene las predicciones en el mismo orden que fueron recibidas. Es decir, la primera predicción corresponderá al primer elemento, la segunda al segundo, etc.

Ejemplo del body de predict:
```json
[
    {
        "serial_no": 312,
        "gre_score": 328,
        "toefl_score": 108,
        "university_rating": 4,
        "sop": 4.5,
        "lor": 4.0,
        "cgpa": 9.18,
        "research": 1
    },
    {
        "serial_no": 239,
        "gre_score": 326,
        "toefl_score": 110,
        "university_rating": 4,
        "sop": 4.31,
        "lor": 3.44,
        "cgpa": 9.15,
        "research": 1
    }
]
```
Respuesta del endpoint:
```json
{
  "results": [
    85.89347820319347,
    84.57717283305547
  ]
}
```

### /fit
Al igual que con el endpoint de predict, `/fit` también recibe una lista de elementos por parámetro del body, pero en este caso retorna métricas de error del entrenamiento del modelo. Las métricas que son devueltas son:
- Mean Absolute Error
- Root Mean Squared Error
- R^2 Score

Ejemplo del body de fit:
```json
[
    {
        "serial_no": 312,
        "gre_score": 328,
        "toefl_score": 108,
        "university_rating": 4,
        "sop": 4.5,
        "lor": 4.0,
        "cgpa": 9.18,
        "research": 1,
        "admission_points": 135
    },
    {
        "serial_no": 239,
        "gre_score": 326,
        "toefl_score": 110,
        "university_rating": 4,
        "sop": 4.31,
        "lor": 3.44,
        "cgpa": 9.15,
        "research": 1,
        "admission_points": 125
    }
]
```

Respuesta del endpoint
```json
{
  "Mean_Absolute_Error_Train": 7.244319918131911,
  "Root_Mean_Squared_Error_Train": 95.69921817076069,
  "R2_Score_Train": 0.7512890220437747,
  "Mean_Absolute_Error_Test": 7.201588344936084,
  "Root_Mean_Squared_Error_Test": 85.57499337118385,
  "R2_Score_Test": 0.7264234692848139
}
```