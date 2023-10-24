# Detalles de proceso de ETL

Todo el manejo que se hace , se a conciencia de que ya se leyó la documentación brindada por la letra de la propuesta.

En nuestro script ETL.py ,  se recompila todos los procesamientos que entendemos necesarios para poder almacenar los datos en la base de datos. 

## Observaciones generales:
Se diseña el script de ETL para que sea ejecutado desde el archivo "ETL.py". No esta pensado para ser ejecutado en sub-etapas de forma secuencial abriendo el script, sino haciendo una ejecucion del mismo. 
Para la explicacion de los pasos se recomienda leer este readme y acceder al contenido de las funciones que se ejecutan.

## ETL : Lectura de datos
("Extraccion"):
- Se nos hes dada la data de origen en un archivo csv. Se procede a hacer la carga . Se generan las direcciones relativas para que cualquier usuario que quiera replicar el ETL pueda hacerlo si clona el repositorio en cuestión ( es decir seteamos la busqueda del archivo CSV en la carpeta principal de prueba_interna_data parrtiendo de que ETL.py esta en la subcarpeta ETL).
- Se hace la carga habiendo identificado a priori que el separador es un ";".
- Se imprime la estructura inicial de los datos cargados (para evidenciar problemas claros de calidad de datos, como los que se ven en site_id) y una descripcion inicial de los tipos de datos de las columnas y conteo de no nulos.


## ETL: Limpieza y transformación de datos
("Transformacion")
- Se procede a hacer input de los unicos datos nulos, que son valores de la columna site_id. Se decide inputarlos como 'unknown' bajo la metodologia de tratamiento de nulos que en este contexto( de un 20% de registros 
con esa variable nula) entiendo conveniente.
Es la metodologia (que en comparacion con eliminar los registros o imputarlos con una prediccion)  que es mas conservadora con respecto los sesgos en las otras variables que podemos generrar en un posterior analisis estadistico o predictivo.
Dicho de otro modo, es en la que somos menos propensos a generar sesgos; y en los peores escenarios lo que se tendria es una perdida de la potencia estadistica a la hora de sacar conclusiones (en pruebas de hipotesis podriamos tener una mayor tendencia a no rechazar H0) , o en modelos podriamos estar perdiendo algo de precision, pero no llegando necesariamente a conclusiones sesgadas por la manipulacion de esta variable.
**OBS importante: Teniendo en cuenta que mas allá del tratamiento de dicha variable; es recomendable para alguien en mi posición, ir al proveedor de dicho dato, para entender si podemos mejorar tanto para los datos ya disponibles, como para futuros datos, la sanidad de dichos datos y tener un porcentaje mas bajo de datos nulos.**

- Se procede a revisarr duplicados y no se encuentran.

- Se procede a rervisar las variables de tipo object (potencialmente categoricas) para entender los valores distintos de cada una de ellas. La idea es encontrar problema de calidad en los datos (ej: site_id escrritos de diferentes maneras) y/o errores en los tipos de columnas( columna y es potencialmente una dummie que esta como "yes"/"no" y deberia ser numerica 1 /0 .

- A partir de lo evidenciado se procede a hacer transformaciones para seguir mejorando la calidad de los datos.
  - Transformacion de y de "yes"/"no" a 1 / 0.
  - Transformacion de site : homologacion de capitalizacion, y adecuacion a nomenclatura MELI con sites tipo "MLA" , "MLU"  , etc.
  - Transformacion month:  de texto a numerica
  - Transformacion day_of_week : de texto a numerica
  - Transformacion duration: de segundos a minutos ( mejor interpretabilidad para el rango de la variable).
  - Se crera verification_date_dt para tener una columna en formato DATE (la original esta en unix). Vamos posteriormente a utilizar este formato para la tabla que guardaremos en la BD para analisis de negocio; mientras que mantendrermos la formato unix (numerico) por conveniencia en la tabla de analisis estadistico.
  - Pdays tiene la particularidad de muchos valores en 999 que reprersentan que no se ha contactado antes al usuario. Para no perder esa informacion es que se genera una nueva variable dummy que indique si hubo un contacto anterior o no. En la misma linea de las decisiones conservadoras con respecto a posibles sesgos y para evitar valores nulos en nuestra tabla de valore estadisticos; a costa segurmente de un poco de detalle de la informacion , se discretiza pdays en intervalos de tiempo del ultimo contacto. 
OBS: la decisión anterior debe ser correctamente documentada, para que posibles futuros usuarios en caso de creerlo conveniente, puedan solicitar otra disposicion de la informacion de esta variable.

- A continuación se genera una copia del dataframe con las transformaciones mencionadas y previo a la binarizacion de las variables categoricas,  para que se pueda utilizar para su almacenamiento posterior en una tabla de "analisis de negocio" en un formato mas "legible" de las variables categoricas. 

- Continuando con nuestras transformaciones de nuestro dataframe principal con fines de analisis estadistico, procedemos a binarizar variables categoricas, para una mejor manipulacion en los analisis que vamos a continuar.


## ETL: Almacenamiento de datos
("Load")
- Nos inclinamos por una eleccion de BD de SQLite, por dominio de la misma y simplicidad en el contexto de esta prueba en la que no quisimos disponer de servicios "de produccion" de MELI , como podia ser BQ.
- En la recien creada BD, se almacenan las 2 tablas mencionadas; con misma informacion pero distinta disposición (analisis de negocio y analsis estadistico).
