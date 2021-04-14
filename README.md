# 202108-Spike-Assesment
Spike Challenge - Aplicación de delivery

------------------------------------
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/hromanoc/202108-Spike-Assesment">
    <img src="images/spike-logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Spike Delivery App</h3>

  <p align="center">
    Reto realizado exclusivamente bajo los términos indicados en el pdf del presente repositorio 
    <br />
    <a href="https://github.com/hromanoc/202108-Spike-Assesment"><strong>Explora los documentos »</strong></a>
    <br />
    <br />
    <a href="#">Ver Demo</a>
    ·
    <a href="https://github.com/hromanoc/202108-Spike-Assesment/issues">Report Bug</a>
    ·
    <a href="https://github.com/hromanoc/202108-Spike-Assesment/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Contenido</summary>
  <ol>
    <li>
      <a href="#preguntas">Preguntas</a>
      <ol>
        <li><a href="#pregunta-1">Pregunta 1</a></li>
        <li><a href="#pregunta-2">Pregunta 2</a></li>
        <li><a href="#pregunta-3">Pregunta 3</a></li>
        <li><a href="#pregunta-4">Pregunta 4</a></li>
        <li><a href="#pregunta-5">Pregunta 5</a></li>
        <li><a href="#pregunta-6">Pregunta 6</a></li>
      </ol>
    </li>
    <li>
      <a href="#demo">Demo</a>
      <ul>
        <li><a href="#spike-delivery-app">Spike Delivery App</a></li>
        <li><a href="#consultas-historicas">Consultas Históricas</a></li>
      </ul>
    </li>
    <li><a href="#recursos">Recursos</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Preguntas

[![Product Name Screen Shot][product-screenshot]](images/screenshot.png)

Este caso es ficticio y no tiene ninguna relación con los proyectos actuales o pasados de Spike.

### Pregunta 1

Cuéntanos qué piezas de software crees que sea necesario desarrollar para el prototipo funcional y cómo se relacionan estas. Llamamos pieza de software a cada aplicación (web, móvil o de escritorio), cada API, cada proceso batch que se puede desplegar de forma independiente. Apóyate con un diagrama si crees necesario.

* Las piezas de software necesarias para el prototipo funcional vía WebApp lo relicé bajo las siguientes técnologías:
    - Front End: Bootstrap y Jquery
    - Back End: Django
    - Base de datos: SQLite

* Asimismo, se optó por desplegar la solución en: PythonEveryWhere
### Pregunta 2

Cuéntanos sobre el tipo de arquitectura que elegiste para la pregunta (1). ¿Monolítica? ¿Micro-servicios? ¿Algún intermedio? ¿Otra? Comenta en qué te basaste para tomar esta decisión

* La arquitectura utilizada fue de Web service por temas de optimizar el tiempo necesario de presentación del presente reto; aunque podría ser mejorada, notablemente, usando una arquitectura _Serverless_ y hostearla en _Amazon AWS_ usando _Lambda functions_ + _API Gateway_ y para el Front End usar _React_. De esa manera se optimizaría costos y el servicio se podría brindar de manera masiva a medida que se requiera aumentar las capacidades en momentos de picos de uso, sin afectar la disponibilidad del servicio. Además, al usar un API en el backend podría servir para alimentar de información a otros tipos de aplicaciones tales como móviles, escritorio, etc.
### Pregunta 3

Describe la metodología de trabajo que usarías para el desarrollo. Puede ser alguna metodología conocida (Scrum, XP, RUP), una adaptación, o una mezcla entre varias metodologías. Lo que sea que tu experiencia te haya mostrado que funciona. Cuéntanos por qué crees que esta forma es adecuada para nuestro problema.

* Haría uso de una metodología ágil, la cual sea ampliamente implementada, con el objetivo de disminuir la curva de aprendizaje durante el proceso de _onboarding_ de un nuevo miembro al equipo. Elegiría Scrum y trabajar bajo el esquema de springs quincenales.
### Pregunta 4

Describe el workflow que usarías para colaborar usando Git. Al igual que con (3), puedes usar algo conocido o una adaptación.

* Primero: Estandarizaría el uso de los sistemas operativos para evitar algún conflicto durante el envío de commits u alguna otra acción.
* Segundo: En conjunto con el equipo, seleccionaríamos una plataforma en nube para compartir el proyecto tales como github, gitlab u otro, quizás hacer uso de Docker (contenedores) para facilitar la compatibilidad de diferentes entornos de desarrollo.
* Tercero: Posterior a ello, crearía almenos 3 tipos de branches para la puesta de producción, developement y pruebas.
* Cuarto: Seleccionaríamos a un único responsable (Team leader) que se encargue de revisar y solucionar los problemas de conflictos en el repositorio.
### Pregunta 5

¿Crees que sea necesario agregar algún integrante extra al equipo durante el desarrollo del prototipo? ¿Cuál sería su rol? ¿Crees que sería necesario agregar nuevos integrantes después de la fase de prototipo? ¿Cuándo y por qué?

* Durante la etapa de desarrollo del prototipo: Sumaría a un _semi senior developer_ que pueda ayudar con nuevos requerimientos que escapen del scope principal del prototipo y para acelerar la etapa de _prototyping_, haría uso de un _Data Scientist / ML engineer_ a tiempo completo por un periodo muy corto de tiempo 3/4 días. Las "ayudas para temas puntuales" no suelen terminar de la mejor manera.
* Posterior a la fase de prototipo: Se requeriría de al menos 2 personas más con un nivel de expertise Junior para que tengan oportunidad de crecer junto con el producto.
### Pregunta 6

¿Qué otras consideraciones tendrías para hacer el proceso de desarrollo robusto y eficiente?

* Básicamente lo mencionado en la pregunta 5. La ayuda de un Data Scientist y un ML Engineer ayudaría a pasar de "prototyping" a "rapid prototyping", lo cual beneficiaría muchísimo a todos los involucrados tantos a los clientes internos como externos. 

<!-- GETTING STARTED -->
## Demo

Para comprobar el resultado, acceder a los siguientes Links:

### Spike Delivery App

* Spike Delivery App: [https://example.com](https://example.com)
### Consultas Historicas

1. Ingresar al siguiente Link: [https://example.com](https://example.com)
2. Colocar el usuario y contraseña:
   
_Por temas de seguridad, las credenciales serán compartidas por correo/chat_

<!-- ACKNOWLEDGEMENTS -->
## Recursos
* [Geopy](https://pypi.org/project/geopy/)
* [Django-with-Geolocation](https://github.com/hellopyplane/Django-with-Geolocation)
* [Django](https://www.djangoproject.com/)
* [Python Everywhere](https://www.pythonanywhere.com/)
* [Bootstrap](https://getbootstrap.com/)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/hernan-romano/
[product-screenshot]: images/screenshot.png