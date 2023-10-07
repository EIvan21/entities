## 1. Instalar Dependencias

1. fastapi: La biblioteca FastAPI para crear la API REST.
2. uvicorn: Un servidor ASGI (Asynchronous Server Gateway Interface) que se utiliza para ejecutar la aplicación FastAPI.
3. spacy: La biblioteca SpaCy que utilizamos para el procesamiento del lenguaje natural.
4. es_core_news_sm: El modelo preentrenado de SpaCy para el procesamiento de texto en español.

También están en el archivo requirements.txt

## 2. Clona o Descarga este Repositorio

## 3. Ejecuta la Aplicación FastAPI
Navegar a la carpeta donde se encuentra el archivo main.py utilizando una terminal o línea de comandos. Ejecuta el comando:

bash
Copy code
uvicorn main:app --reload
main:app le dice a Uvicorn que ejecute la aplicación FastAPI que se encuentra en el archivo main.py y se llama app.
--reload habilita la recarga automática de la aplicación cuando se realizan cambios en el código.

## 4. Realiza Solicitudes POST
