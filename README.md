# Seminario de Sistemas Operativos
Pequeño repositorio donde recopilaremos los trabajos de la asignación de Seminario de Sistemas Operativos.

### By: Dexne


[Investigación 01: Procesamiento por lotes](Procesamiento_por_lotes.pdf)

¿Qué es el procesamiento por lotes?
¿Cuándo se usa el procesamiento por lotes?
Ventajas y desventajas del procesamiento por lotes

Con este pequeño repositorio buscamos darle a la comunidad un espacio donde puedan obtener información acerca del procesamiento por lotes o batch, una herramienta que nos ayuda a la optimización de miles de procesos.

Pratica 01  Procesamiento por lotes.
-[Practica 01 procesamiento por lotes CÓDIGO](https://github.com/Dexne/S.S.O/tree/main/Practica%2001%20Procesamiento%20por%20lotes%201)

Investigación 02
-[Algoritmos de planificación de procesos](Algoritmos_de_planificación_de_procesos.pdf)

Los algoritmos de planificación son esenciales en la administración de procesos en sistemas operativos. Definen el orden en que las tareas se ejecutan en la CPU. Destacan el Round Robin, que asigna tiempos de CPU equitativos; SJF (Shortest Job First), priorizando tareas más cortas; FIFO (First-In-First-Out), siguiendo el orden de llegada, y algoritmos basados en prioridades, atendiendo a la importancia.

Algortimos de planificación 1:

- Round Robin
- SJF
- FIFO
- Prioridades

[Algoritmos de planificación](https://github.com/Dexne/S.S.O/tree/main/Algoritmos_de_planificaci%C3%B3n_1)

Aquí una pequeña actualización del código de algoritmos de planificación, ahora en su versión 2 donde se ha añadido la posibilidad de que el usuario pueda agregar nuevos servicios, así mismo, como medida de perseverancia de los datos, los nuevos servicios que se añadan serán almacenandos en el documento txt existente.

[Algoritmos de planificación versión 2](https://github.com/Dexne/S.S.O/tree/main/Algoritmos_de_planificacion_v2)

Algortimos de administración de memoria:

Los algoritmos de administración de memoria son esenciales en sistemas 
informáticos para asignar y liberar recursos de memoria de manera eficiente.

- Primero ajuste
- Mejor ajuste
- Peor ajuste
- Siguiente ajuste

[Algoritmos de administración de memoria](https://github.com/Dexne/S.S.O/blob/main/Algoritmos_de_administracion_de_memoria.pdf)

Algoritmos de administración de memoria

Implementación código

[implementación en código de los algoritmos de administración de memoria](https://github.com/Dexne/S.S.O/tree/main/Algoritmos_de_administracion_de_memoria)


Investigación Hilos y Procesos.

**Hilos** son subprocesos dentro de un proceso principal que comparten recursos y ejecutan tareas de manera independiente, optimizando la multitarea y la concurrencia en software.

**Procesos** son programas en ejecución, cada uno con su espacio de memoria, recursos y variables, que pueden ejecutarse de forma concurrente en un sistema operativo, brindando aislamiento y seguridad.

**Paralelismo** se refiere a la ejecución simultánea de tareas para mejorar el rendimiento en hardware de múltiples núcleos, distribuyendo la carga de trabajo entre ellos.


**Multiprogramación** permite ejecutar varios programas simultáneamente en una computadora, mejorando la utilización del procesador al alternar entre tareas, reduciendo la espera.

[Investigación sobre hilos, procesos, paralelismos y multiprogramación](https://github.com/Dexne/S.S.O/blob/main/Investigaci%C3%B3n.pdf)


Algoritmos de administración de memoria - Version 2

Esta es la versión mejorada del código de algoritmos de planificación de memoria.
Esta es la version mejorada del codigo de implementacion de los algoritmos.

[version mejorada](https://github.com/Dexne/S.S.O/tree/main/Administrador_de_memoria_2)


Práctica 7 - Hilos

Los hilos (threads) en programación son unidades de ejecución dentro de un proceso, que permiten realizar múltiples tareas de forma concurrente. A diferencia de un programa de un solo hilo, los hilos permiten que una aplicación ejecute varias secciones de código de manera simultánea, lo que mejora la eficiencia y el rendimiento. Cada hilo comparte los recursos del proceso principal pero tiene su propio flujo de control. Los hilos son esenciales para tareas como la gestión de interfaces de usuario, la optimización de operaciones en tiempo real y la paralelización de cálculos intensivos, lo que resulta en una programación más eficiente y receptiva.

En esta ocasión la asignación es mover 2 imagenes haciendo uso de los hilos, uno para cada imagen existente.

[Práctica con hilos](https://github.com/Dexne/S.S.O/tree/main/Hilos)

Producto-Consumidor

El problema del productor y consumidor es muy popular en el mundo de la programación paralela. El problema considera tres objetos: un productor, un consumidor, y un contenedor.


[Repositorio con reporte e implementación en código](https://github.com/Dexne/S.S.O/tree/main/Producto-Consumidor)


Producto-Consumidor | Práctica simulación de estacionamiento

El proposito de esta actividad es la de simular el funcionamiento de un estacionamiento
Se debe de poder dar la opción de acelerar la velocidad con la que los autos ingresan y también la velocidad con la que se retiran
Todo esto se logra gracias al uso de hilos para manejar ambos procesos de manera independiente.

[Simulación del estacionamiento](https://github.com/Dexne/S.S.O/tree/main/Prodcuto-Consumidor_Estacionamiento)


Investigación Problema del Lector-Escritor:


El término "lector-escritor" suele utilizarse en el contexto de la informática y la programación, donde se refiere a una estructura que permite a un proceso o hilo (thread) leer y escribir datos en un recurso compartido.

[Investigación problema Lector-Escritor](https://github.com/Dexne/S.S.O/blob/main/Lector-Escritor.pdf)


Implementación del problema del lector-escritor:

El problema de los lectores-escritores se refiere a la sincronización de múltiples procesos que desean acceder a un recurso compartido, en este caso, un archivo, de manera que se cumplan ciertas reglas. El objetivo es garantizar la consistencia y la integridad de los datos al tiempo que se permiten lecturas concurrentes y se evita que las escrituras interfieran con las lecturas y viceversa.

En este código, se ha implementado una versión simple del problema de los lectores-escritores utilizando semáforos para controlar el acceso al archivo compartido. El problema se manifiesta principalmente en las siguientes áreas:

Acceso a la escritura: Se utiliza un semáforo (archivo_mutex) para garantizar que solo un escritor pueda acceder al archivo a la vez. Cuando un escritor está editando y guardando el archivo, se bloquea el acceso tanto a otros escritores como a los lectores.

Acceso a la lectura: Se utiliza otro semáforo (lectores_mutex) para controlar el acceso a la lectura del archivo. Los lectores pueden acceder al archivo simultáneamente, siempre y cuando no haya escritores activos. Cuando un escritor está escribiendo, los lectores deben esperar a que se libere el recurso antes de acceder.

Aqui tenemoos el código fuente de esta pequeña implementación del problema del lector-escritor.

[Lector-Escritor implementación](https://github.com/Dexne/S.S.O/blob/main/lector-escritor.py).

**Practica 10: Algoritmos de planificación de procesos**

Esta es una versión modificada y actualizada de la práctica 4 pero con la diferencial de que een esta entrega de hace uso de hilos y además se ha desarrollado una pequeña interfaz gráfica para el usuario.

Consulta el código fuente [Planificador de procesos GUI](https://github.com/Dexne/S.S.O/tree/main/Planificador_de_procesos_con_hilos).



