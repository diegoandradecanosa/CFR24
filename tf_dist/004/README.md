# Varios nodos varias GPUs

Para seguir este nodo debemos empezar conectándonos al FT3 y al directorio correspondiente

```bash
ssh tusuario@ft3.cesga.es
cd $STORE/CFR24/tf_dist/004
```

Luego lanzamos la ejecución mediante el comando

```bash
sbatch sbatch_2nodes_ngpus.sh simple2NodesSol2.py
```

Al finalizar la ejecución inspeccionamos la salida (ficheros jsimple*)

Ahora vamos a explicar los puntos claves del código que realizan el entrenamiento usando varios nodos y varios dispositivos.

En el script de lanzamiento, una vez especificados los recursos requeridos (básicamente 2 nodos y 2 GPUs por nodo) tenemos que activar el entorno mytf

https://github.com/diegoandradecanosa/CFR24/blob/0fdf682bbc9b504f3884da91fc5cce1f79d4b470/tf_dist/004/sbatch_2nodes_ngpus.sh#L14

El lanzamiento hay que hacer con srun

https://github.com/diegoandradecanosa/CFR24/blob/0fdf682bbc9b504f3884da91fc5cce1f79d4b470/tf_dist/004/sbatch_2nodes_ngpus.sh#L25

En el script python con el entrenamiento, tenemos que comprobar si en cada nodo tenemos acceso a las GPUs solicitadas para cada nodo

https://github.com/diegoandradecanosa/CFR24/blob/0fdf682bbc9b504f3884da91fc5cce1f79d4b470/tf_dist/004/simple2NodesSol2.py#L16-L22

Utilizamos un ClusterResolver de Slurm (SlurmClusterResolver) para encontrar automáticamente la configuración de los recursos disponibles.

https://github.com/diegoandradecanosa/CFR24/blob/0fdf682bbc9b504f3884da91fc5cce1f79d4b470/tf_dist/004/simple2NodesSol2.py#L38

La función set_tf_config establece la configuración adecuada para la variable TF_CONFIG en base a los recursos encontrados por SlurmClusterResolver

https://github.com/diegoandradecanosa/CFR24/blob/0fdf682bbc9b504f3884da91fc5cce1f79d4b470/tf_dist/004/simple2NodesSol2.py#L24-L36

Luego, configuramos una MultiworkerMirrorStrategy para hacer uso de todos los recursos

https://github.com/diegoandradecanosa/CFR24/blob/0fdf682bbc9b504f3884da91fc5cce1f79d4b470/tf_dist/004/simple2NodesSol2.py#L41

Para utilizar estos recursos durante la ejecución, debemos hacer el entrenamiento dentro del scope de la estrategia 

https://github.com/diegoandradecanosa/CFR24/blob/0fdf682bbc9b504f3884da91fc5cce1f79d4b470/tf_dist/004/simple2NodesSol2.py#L85-L86

El [siguiente fichero](https://github.com/diegoandradecanosa/CFR24/blob/main/tf_dist/004/jsimple.o4913776) contiene un ejemplo de salida.

