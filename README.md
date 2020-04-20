## Geolocation Project
Este proyecto consiste en encontrar la localización ideal para una nueva empresa según los siguientes parámetros:
- Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design.
- 30% of the company have at least 1 child.
- Developers like to be near successful tech startups that have raised at least 1 Million dollars.
- Executives like Starbucks A LOT. Ensure there's a starbucks not to far.
- Account managers need to travel a lot
- All people in the company have between 25 and 40 years, give them some place to go to party.
- Nobody in the company likes to have companies with more than 10 years in a radius of 2 KM.
- The CEO is Vegan

Para ello hemos trabajado con una base de datos MongoDB a la que hemos añadido:
- Un dataset que contenía información sobre un gran número de compañias, a este dataset lo hemos llamado "companies".
- Otro dataset descargado de (www.kaggle.com) con información sobre cafeterias Starbucks, a este dataset lo hemos llamado "Starbucks"
- Información extraida de la API de foursquare, de este API hemos extraido información sobre aeropuertos, bares y restaurantes veganos.

A continuación pasamos a detallar el trabajo que se ha hecho con cada fuente de información.

# Companies

Este dataset lo hemos limpiado para adaptarlo a nuestras necesidades, hemos dividido las empresas en tecnologicas y no tecnologicas, hemos armonizado la columna "total_money_raised" para poder eliminar aquellas empresas con menos de 1.000.000$ y hemos eliminado aquellas empresas cuya latitud o longitud no fuera correcta o no existiera.

# Starbucks

Este dataset lo hemos filtrado para quedarnos solo con aquellas cafeterias en United States, ya que el dataset anterior contenía principalmente datos de empresas americanas.

# Foursquare

Para poder acceder a los datos de esta API nos hemos registrado y hemos obtenido un "client_id" y "client_secret" ambos han sido guardados en un archivo .env que se ha ocultado por seguridad. Las busquedas se han hecho según el categoryId que ofrece la API para cada uno de los datos que queríamos obtener. En este caso también se ha limitado la búsqueda geograficamente a US. La información obtenida se ha guardado en datasets diferenciados por tipo de información.

Una vez teniamos toda la información necesaria se ha incluido en la base de datos MongoDB en distintas colecciones. Para poder trabajar con queries geoespaciales fue necesario crear en cada dataframe una columna llamada "geolocation" para una vez importada la información a la base de datos poder crear un indice geoespacial.

Por útlimo se ha ido filtrando la información de la colección companies a través de geoqueries comenzando primero por las localizaciones más lejanas (en este caso aeropuerto) para ir cerrando cada vez más el radio hasta llegar a la localización ideal para nuestra empresa.


