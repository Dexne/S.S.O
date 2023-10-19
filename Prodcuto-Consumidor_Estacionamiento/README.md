# Producto-Consumidor Simuación de estacionamiento

**By: Dexne**

¿Qué es Producto-Consumidor en programación?

El problema del productor-consumidor es un patrón clásico en la programación concurrente y la teoría de la concurrencia. Representa una situación en la que dos tipos de hilos o procesos, 
conocidos como "productores" y "consumidores," comparten un área de almacenamiento o un búfer para la transferencia de datos.

En este escenario, los productores generan datos y los colocan en el búfer, mientras que los consumidores retiran esos datos del búfer. La idea principal es que los productores y consumidores
deben trabajar de manera cooperativa y en paralelo, sin interferirse mutuamente.

El problema del productor-consumidor se utiliza comúnmente para ilustrar y abordar temas relacionados con la sincronización, la concurrencia y la comunicación entre hilos o procesos en sistemas
multi-hilo o multi-proceso.

**Problematica**

Se nos pide simular el proceso de cómo funciona un estacionamiento, se tienen los métodos de ingresar y retirar autos del estacionamiento, los cuales toman un valor
random entre las opciones de 0.5, 1 y 2 segundos.
También se tienes las funciones de moficar la frecuencia de inserciones y salidas mediante botones desplegables

Estas acciones se logran gracias al uso de hilos, manejando un hilo para las inserciones y otro para las reducciones.
