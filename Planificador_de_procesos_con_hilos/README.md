# Planificador de procesos con hilos

### By: Dexne

**Round Robin:**

Es un algoritmo de planificación de procesos que asigna a cada proceso un intervalo de tiempo de CPU, luego los ejecuta secuencialmente en ciclos circulares. Proporciona un trato justo a todos los procesos, asignando tiempos iguales de ejecución en turnos sucesivos.

**SJF:**

(Shortest Job First) es un algoritmo de planificación de procesos que prioriza la ejecución del proceso con el menor tiempo de ejecución. Ordena los trabajos por duración y ejecuta primero aquel con el menor tiempo estimado, minimizando el tiempo de espera y mejorando la eficiencia del sistema operativo.

**FIFO:**

(First In, First Out) es un algoritmo de gestión de colas que procesa elementos en el mismo orden en que llegaron. Funciona como una estructura de datos tipo cola, donde el primer elemento en entrar es el primero en ser atendido o eliminado, manteniendo la secuencia original de llegada.

**Prioridades:**

El algoritmo de planificación por prioridades asigna tareas según un valor predefinido que determina su importancia relativa. Los procesos con la prioridad más alta se ejecutan primero, brindando atención preferencial a las tareas críticas o marcadas como más urgentes, mejorando así la respuesta del sistema operativo.

La elección del algoritmo depende del contexto y los requisitos específicos del sistema operativo o aplicación. La implementación precisa y la selección adecuada del algoritmo pueden mejorar significativamente el rendimiento y la capacidad de respuesta del sistema en entornos con múltiples hilos de ejecución. Es esencial considerar factores como la equidad, la minimización del tiempo de espera y la eficiencia al elegir un algoritmo de planificación de hilos para una aplicación particular.
