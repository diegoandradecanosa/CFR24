# Ejemplo de uso de Callbacks en Lightning

Este ejemplo ilustra la configuración de *callbacks* en un proceso de entrenamiento en Lightning. El lanzamiento se realiza de forma análoga a los otros ejemplos
de Lightning y DDP.
```
sbatch sub.sbatch
```
Si inspeccionamos el script, no encontramos ninguna diferencia notable. La salida, se genera de forma análoga a otros scripts, y el fichero
[slurm-342263.out](https://github.com/diegoandradecanosa/CFR24/blob/main/pytorch_dist/lightning/001/slurm-3422263.out) contiene una salida de ejemplo.

El script de entrenamiento tiene los mismos elementos que el script de ejemplo anterior (el 000) salvo por la introducción de los elementos necesarios para 
incorporar el mecanismo de *callback*. Su incorporación se produce como un argumento del constructor del *trainer*. 

https://github.com/diegoandradecanosa/CFR24/blob/71e7962e6b78654ef123a2f0c5f7e0dcc11d0e59/pytorch_dist/lightning/001/callbacksLI.py#L57-L68

El argumento *callbacks* permite definir una lista
de objetos de tipo *Callback*, algunos de ellos ya están implementados en Lightning (*EarlyStopping, ModelCheckpoint, LearningRateMonitor,Timer*), sin embargo, 
*MySlurmCallback* es un *Callback* creado por el propio usuario.

https://github.com/diegoandradecanosa/CFR24/blob/71e7962e6b78654ef123a2f0c5f7e0dcc11d0e59/pytorch_dist/lightning/001/callbacksLI.py#L11-L16




