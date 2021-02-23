## Laboratorio 1. Inversión de Capital

### Abtract

Este proyecto fue elaborado por **Andrea Jiménez Orozco**, como un trabajo parcial para la materia de **Microestructura y Sistemas de Trading**, la cual es parte del curriculum de la licenciatura en **Ingeniería Financiera**, ofertada por la universidad **ITESO**. En el presente trabajo se plantea la respuesta a la siguiente pregunta: *¿Qué estrategia de inversión propondrías si tu trabajo fuera administrar 1 Millón de pesos?*

### Objetivos

La intención del presente trabajo es hacer una comparativa simple entre utilizar una inversión **Pasiva Vs. Activa** en el mismo periodo de tiempo. El cual comprende del **31 enero del 2018 al 31 de dicembre del 2020.**

Para crear una cartera de inversión pasiva, nos apoyaremos de un **ETF** *(exchange-trade-fund)* **NAFTRAC iShares** de **BlackRock** el cual réplica el índice mexicano **S&P - BMV**, cuya información disponible y archivos utilizados para el análsis se pueden encontrar en el siguiente link: 

- https://www.blackrock.com/mx/intermediarios/productos/251895/ishares-naftrac-fund

### Para facilitar la lectura, comentarios y conclusiones descargar y/o consultar el archivo de notebook.py/notebook.html 

## Estructura de proyecto

La estructura de proyecto se basa en crear diferentes archivos de Python los cuales mandamos llamar al inicio en una sola línea dentro del cuaderno de Jupyter. Cada función tiene un objetivo distinto, consecutivo y complementario para la creación del análisis. Esto nos permite obtener como resultado una organización más limpia, funcional y eficiente, lo que se traduce en una mejor comprensión para el lector.

Los elementos son los siguientes:

- **main.py**
  *contiene el orden secuencial de las funciones principales para correr el análisis.*
- **functions.py**
  *contiene todas las funciones referentes al cálculo de ambas estrategias.*
- **data.py**
  *contiene todas las funciones referentes a la descarga y manejo de datos.*
- **visualizations.py**
  *contiene todas las funciones correspondientes a la creación de gráficas y/o elementos visuales.*

## Instalar dependencias

Instalar todas las dependencias que se encuentran en el archivo **requirements.txt**, solo corra el siguiente comando en su terminal:

        pip install -r requirements.txt
   
## Licencia
**GNU General Public License v3.0**

Los permisos de esta licencia están condicionados a poner a disposición el código fuente completo de los trabajos con licencia y las modificaciones, que incluyen trabajos más grandes que utilizan un trabajo con licencia, bajo la misma licencia. Se deben conservar los avisos de derechos de autor y licencias. Los contribuyentes proporcionan una concesión expresa de derechos de patente.

## Contacto

¿Qué es Ingeniería Financiera? En Ingeniería Financiera aprendes a formular estrategias comerciales y proyectos de inversión que puedan asegurar la viabilidad y rentabilidad de los planes de generación de riqueza de empresas, gobiernos y particulares. Desarrollas competencias para construir modelos matemáticos de diferentes escenarios de negocio considerando los objetivos de los inversores y los riesgos que puedan surgir, permitiendo así que empresas y comunidades se transformen en espacios de bienestar y desarrollo. Aplicas los conocimientos adquiridos a problemas como el desarrollo de nuevos productos financieros, propones estrategias para estimular el crecimiento de las empresas, y tomas decisiones basadas en la ciencia de datos y la simulación de escenarios de negocio que convierten los riesgos en oportunidades de crecimiento y competitividad.

¿Qué es ITESO? ITESO es la Universidad Jesuita de Guadalajara. Fundada en 1957, pertenece a una red de más de 228 universidades jesuitas de todo el mundo. Todos comparten una tradición de 450 años de educación jesuita, una tradición que históricamente ha estado en el centro del pensamiento mundial, conocida por educar líderes en todos los campos de la ciencia y el arte. El ITESO es conocido por su excelencia académica, una profunda preocupación por los contextos tanto locales como globales, y su compromiso con la mejora de las condiciones de vida de las personas. Su proyecto educativo integral busca desarrollar la inteligencia y la sensibilidad, formar jóvenes libres y socialmente responsables de por vida, en un entorno ideal para el descubrimiento y el crecimiento. https://www.iteso.mx/

Para tener mas información acerca de este repositorio y su funcionalidad favor de ponerse en contacto al siguiente correo: if706970@iteso.mx
