# Trabajo-Practico-Integrador---Organizacion-empresarial
Trabajo Practico Integrador - Organizacion empresarial

Sistema de Gestión de Vacaciones Automatizado

Objetivo\
&emsp;Este proyecto tiene como fin optimizar y simular el proceso de \
gestión de vacaciones interna de una organización. El sistema automatiza las tareas críticas del modelo **TO-BE**, realizando de forma autónoma:
-La verificación de superposiciones de fechas entre empleados del mismo sector (viabilidad operativa).\
-El control y validación del saldo de días disponibles versus 
los solicitados. 

Operativa y Despliegue\
&emsp;El programa de automatización se encuentra listo para ser desplegado. Para ponerlo en marcha, únicamente se deben\
registrar los elementos en la estructura de la base de datos simulada. Para probar su funcionamiento, el código cuenta con\
**datos de ejemplo precargados** (2 sectores con 2 empleados cada uno). Una vez configurados los períodos de vacaciones\
actuales y el saldo de días de cada integrante, el bot queda operativo.

Interfaz del Usuario\
&emsp;El sistema presenta un menú interactivo por consola con robustez a errores, otorgando una experiencia amena,fácil de\
entender y con manejo controlado de errores de entrada (camino\ infeliz).

Como ejecutar el programa
1. Contar con python instalado [Python 3](https://python.org).
2. Clonar este repositorio o descargar el archivo `.py`.
3. Ejecutar el archivo desde tu terminal o editor de codigo:
   

Tecnologías Utilizadas

  El proyecto fue desarrollado utilizando el ecosistema nativo de Python, no se necesitan dependencias externas.

* **Python 3.x**: Lenguaje de programación utilizado.

* **Modulo `datetime` (Nativo)**: Biblioteca estándar utilizada para procesar, validar el formato y calcular la diferencia de días entre fechas de manera precisa. 
