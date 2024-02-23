
# Actividad un nodo dos GPUs

Conéctate al FT3 

```bash
ssh tuusuario@ft3.cesga.es
```



Abre una sesión interactiva con 1 nodo y 2 GPUs A100

```bash
./interactive_1node_2gpus.sh 
```

Activar el entorno, entrar en el directorio del ejemplo y arrancar jupyter lab

```bash
source $STORE/mytf/bin/activate
cd $STORE/CFR24/tf_dist/003
jupyter lab --ip `hostname -i` --no-browser
```

Abrir sucesivamente los notebook simple2GPUsOrig, simple2GPUsSol y simple2GPUsSol2 y apreciar las diferencias entre ellos.

Las diferencia apreciables se deben a que:

- simple2GPUsOrig no está configurado para usar ninguna estrategia de entrenamiento distribuido.
- simple2GPUsSol está configurado para usar una estrategia espejo del tipo MirroredStrategy (no recomendada, incluso dentro de un único nodo)
- simple2GPUSol2 está configurado para usar una estrategia espejo del tipo MultiworkerMirroredStrategy (la recomendada para proporcionar paralelismo de datos)

También se pueden ejecutar las versiones .py de los mismos códigos usando ipython

- ipython simple2GPUsOrig.py 
- ipython simple2GPUsSol.py 
- ipython simple2GPUsSol2.py 

Inspecciona el código relevante en las versiones preparadas para usar varias GPUs

El siguiente fragmento de código se asegura de que utilizamos 64 hilos por nodo, para hacer uso de todos los cores de un nodo

https://github.com/diegoandradecanosa/CFR24/blob/e339603203222abf5f88e075803b0b3e96c6efc2/tf_dist/003/simple2GPUsSol.py#L20-L31

La entrada salida del *dataset* se realizar en LUSTRE para mejorar el rendimiento

https://github.com/diegoandradecanosa/CFR24/blob/e339603203222abf5f88e075803b0b3e96c6efc2/tf_dist/003/simple2GPUsSol.py#L33-L36  

Seleccionamos la MirroredStrategy

https://github.com/diegoandradecanosa/CFR24/blob/e339603203222abf5f88e075803b0b3e96c6efc2/tf_dist/003/simple2GPUsSol.py#L43

La carga de datos se efectúa utilizando prebúsqueda

https://github.com/diegoandradecanosa/CFR24/blob/e339603203222abf5f88e075803b0b3e96c6efc2/tf_dist/003/simple2GPUsSol.py#L63-L64

Nos aseguramos de recuperar, y tener acceso, a todas las GPUs del Nodo

https://github.com/diegoandradecanosa/CFR24/blob/e339603203222abf5f88e075803b0b3e96c6efc2/tf_dist/003/simple2GPUsSol.py#L69-L78

El entrenamiento se realiza dentro del entorno de la MirroredStrategy

https://github.com/diegoandradecanosa/CFR24/blob/e339603203222abf5f88e075803b0b3e96c6efc2/tf_dist/003/simple2GPUsSol.py#L80

Llamamos a la función *fit* (de Keras) con el callback de profiling

https://github.com/diegoandradecanosa/CFR24/blob/e339603203222abf5f88e075803b0b3e96c6efc2/tf_dist/003/simple2GPUsSol.py#L96-L98

En la versión Sol2, la principal diferencia es que usamos la estrategia MultiworkerMirroredStrategy 

https://github.com/diegoandradecanosa/CFR24/blob/e339603203222abf5f88e075803b0b3e96c6efc2/tf_dist/003/simple2GPUsSol2.py#L53





