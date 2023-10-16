# Producto-Consumidor

**By:Dexne**

El problema del productor y consumidor es muy popular en el mundo de la programación paralela. El problema considera tres objetos: un productor, un consumidor, y un contenedor. Las reglas del problema son estas:

- El productor tiene la tarea de producir N productos.
- Cada producto nuevo deberá ser colocado en el contenedor.
- Si el contenedor está lleno, el productor deberá esperar a que el consumidor haga espacio para nuevos productos.
- El consumidor tiene la tarea de procesar los N productos.
- Cada vez que se procesa un producto, se quita del contenedor.
- Si el contenedor está vacío, el consumidor deberá esperar al productor para que haya productos para procesar.

