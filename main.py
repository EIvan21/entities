from fastapi import FastAPI
from pydantic import BaseModel
import spacy
from typing import List

# Cargando el moleo spaCy en español
spacy_nlp = spacy.load("es_core_news_sm")

# instanciando nuestra app de FastAPI
app = FastAPI(
    title="Identificar Entidades"
)

# creando la clase Oraciones, que serán nuestros datos de entrada al endpoint,
# Definiendo como una lista de strings


class Oraciones(BaseModel):
    oraciones: List[str]


# Creamos la función para ubicar las entidades en cada oración

def identificar_entidades(oracion):
    # usamos eel modelo SspaCy para procesar cada oración

    # esta variable doc contiene la información linguistica de la oración
    doc = spacy_nlp(oracion)

    # Creamos el diccionario para posteriormente guardar las entidades identificaas
    entidades = {}

    # iteramos entee todas las entidades identificadas con ".ents" en el objeto doc
    for ent in doc.ents:

        # Finalmente almacenamos el texto de la entidad en el diccionario entidades, con su value que es el tipo de entidad
        entidades[ent.text] = ent.label_
    return entidades

# Creamos el endpoint para hacer el post request

# esta funcion recibe una lista de oraciones, (Objeto Oracion)


@app.post("/entidades/identificar-entidades")
async def identificar_entidades_oraciones(lista: Oraciones):

    # Creamos una lista para almacenar los resultados
    resultado = []

    # iteramos sobre la lista de oraciones que le pasemos de entrada
    for oracion in lista.oraciones:
        # Para cada oracion identificamos las entidades con la función creada anteriormente
        entidades = identificar_entidades(oracion)

        # Añadimos los resultados en la lista final
        resultado.append({"oracion": oracion, "entidades": entidades})
    return {"resultado": resultado}
    # return {"message": "HI"}
