# ClusterResolver

Este es un ejemplo simple que inspecciona los recursos reservados con Slurm a través del API correspondiente de TF.

Para ejecutar el ejemplo, nos conectamos al FT3 y lanzamos el script de ejecución

```bash
ssh tuusuario@ft3.cesga.es
sbatch sbatch_2nodes_ngpus.sh simple.py 
```

Los resultados se generarán en fichero con la forma jsimple*

Veamos cómo se realiza el lanzamiento. El script sbatch contiene la reserva de recursos.

https://github.com/diegoandradecanosa/CFR24/blob/403de13945f7d99d22ee4dca7b3e4766d6dfc487/tf_dist/002/sbatch_2nodes_ngpus.sh#L2-L10

Básicamente son 2 nodos y 2 GPUs por nodo. Una vez cargado el entorno mytf, tenemos que lanzar el script python a través de srun

https://github.com/diegoandradecanosa/CFR24/blob/403de13945f7d99d22ee4dca7b3e4766d6dfc487/tf_dist/002/sbatch_2nodes_ngpus.sh#L26

El código es extremadamente sencillo, simplemente descubre los recursos reservados a través de un SlurmClusterResolver

https://github.com/diegoandradecanosa/CFR24/blob/436b86fab765781de12caa1b31f4b4a3fd7a79cd/tf_dist/002/simple.py#L1-L5

El siguiente fichero contiene un ejemplo de salida

https://github.com/diegoandradecanosa/CFR24/blob/b3b175a87013d04e79ff4ea3fa9610cc2a29df78/tf_dist/002/jsimple.o5947658#L1-L10




