# Proyecto N°2 - Base de datos II

## Integrantes

- Alfaro, Gonzalo
- Arróspide, Eduardo
- Domínguez, Pedro
- Rodríguez, Renato

| Lista de actividades Realizadas | Responsable                         | Participación |
|---------------------------------|-------------------------------------|------|
| Algoritmo SPIMI, búsqueda por similitud de coseno | Pedro Domínguez, Gonzalo Alfaro|  100%  |
| Frontend, Conexión a PostgreSQL                   | Renato Rodríguez               |  100%  |
| Conexión a MongoDB                                | Eduardo Arróspide              |  100%  |


## Introducción

El objetivo del proyecto es el aprendizaje de algoritmos y estructuras que permitan realizar consultas de búsqueda eficientes a un conjunto de documentos utilizando el método de *ranked retrieval*. 

Este proyecto utiliza el **algoritmo SPIMI** para la optimización de indexación, así como la **búsqueda por similitud de coseno** para realizar las consultas.


## Datos

Los datos utilizados son un conjunto de noticias obtenidas de la página [Kaggle](https://www.kaggle.com/datasets/snapcrack/all-the-news). El buscador del proyecto retornará el título y ranking de cada noticia, y a su vez utilizará su contenido para crear el índice invertido.

## Construcción del índice invertido

Para la construccón del índice está compuesta por dos etapas principalmente.

1. **Pre-Processing:**
  El contenido de cada noticia debe ser pre-procesado, ignorando "stop words", realizar el stemming y normalizando el texto en general. Específicamente, nuestra aplicación realiza un proceso como el descrito a continuación:
    - Lowercase: todas las palabras a letras minúsculas
    - Stop words: remover todos los stop words. Utilizamos los stop words de inglés de la librería [NLTK](https://www.nltk.org/)
    - Puntuación: Remover todo símbolo de puntuación, puesto que no son necesarios para la creación del índice invertido.
    - Apostrofes: Remove apostrofes (muy usados en inglés) ya que, al igual que la puntuación, no son relevantes.
    - Stemming: Convertir todas las palabras a su raíz. Para esta acción utilizamos el [Porter Stemmer](https://www.nltk.org/howto/stem.html) de NLTK.
    - Num2Words: Utilizamos la librería [num2words](https://pypi.org/project/num2words/) para convertir cada número a su contraparte como palabra en inglés. Ej: 15 a "fifteen".
2. **Cálculo del TF:** 
  Para el cálculo de la frecuencia de términos utilizamos la libreria NLTK, ya que nos proporciona la funcionabilidad de manera directa utilizando "word_tolenize". Para la construcción de este índice buscamos un archivo de texto dentro de la carpeta de indices "indexes", si no es encontrada se crea un nuevo documento y se agrega el título de la noticia (que se está tomando como "documento" de forma teorica) junto a su TF.

## Ejecución óptima de consultas



## PostgreSQL / MongoDB

## Video
