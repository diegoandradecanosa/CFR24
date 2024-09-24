# Lightning Fabric Example

This example illustrates the basic use of the **Lightning Fabric** library on a platform managed with SLURM.

The two launch scripts, the main one ([submit.sbatch](https://github.com/diegoandradecanosa/CFR24/blob/main/pytorch_dist/fabric/submit.sbatch)) and the secondary one ([mnist.sh](https://github.com/diegoandradecanosa/CFR24/blob/main/pytorch_dist/fabric/mnist.sh)), are not substantially different from those used in the **Lightning** examples.

The code is launched with the command:
```
sbatch submit.sbatch
```

The output is saved in a file that follows the usual naming convention *slurm-xxx.out*, and the file [slurm-3431901.out](https://github.com/diegoandradecanosa/CFR24/blob/main/pytorch_dist/fabric/slurm-3431902.out) contains an example of the output.

In the training script, the use of Fabric first involves creating a *Fabric* object, specifying the available computational resources, and launching it (*launch*).

https://github.com/diegoandradecanosa/CFR24/blob/cec76daebbbd60d4ecdf4a3757147a3fab4d8ccb/pytorch_dist/fabric/mnist.py#L114-L115

Next, we need to configure Fabric using the model (Pytorch) and the optimizer we want to associate with it.

https://github.com/diegoandradecanosa/CFR24/blob/cec76daebbbd60d4ecdf4a3757147a3fab4d8ccb/pytorch_dist/fabric/mnist.py#L141-L152

The main training loop also contains some specific elements conditioned by the use of Fabric, such as the backward pass being called through the *fabric* object.

https://github.com/diegoandradecanosa/CFR24/blob/cec76daebbbd60d4ecdf4a3757147a3fab4d8ccb/pytorch_dist/fabric/mnist.py#L39-L54


# Ejemplo de Lightning Fabric

Este ejemplo ilustra el uso básico de la librería **Lightning Fabric** en una plataforma ordenada con SLURM.

Los 2 scripts de lanzamiento, el principal ([submit.sbatch](https://github.com/diegoandradecanosa/CFR24/blob/main/pytorch_dist/fabric/submit.sbatch)) 
y el secundario ([mnist.sh](https://github.com/diegoandradecanosa/CFR24/blob/main/pytorch_dist/fabric/mnist.sh)), 
no difieren sustancialmente de los usados en los ejemplos de **Lightning**.

El lanzamiento del código se realiza con el comando.
```
sbatch submit.sbatch
```

La salida se obtiene en un fichero que sigue la nomenclatura habitual *slurm-xxx.out* y el fichero [slurm-3431901.out](https://github.com/diegoandradecanosa/CFR24/blob/main/pytorch_dist/fabric/slurm-3431902.out) 
contiene un ejemplo de salida.

En el script de entrenamiento, el uso de Fabric implica en primer lugar la creación de un objeto *Fabric* indicando los recursos computacionales disponibles
y su lanzamiento (*launch*).

https://github.com/diegoandradecanosa/CFR24/blob/cec76daebbbd60d4ecdf4a3757147a3fab4d8ccb/pytorch_dist/fabric/mnist.py#L114-L115

A continuación debemos hacer la configuración de fabric usando el modelo (Pytorch) y el optimizador que queremos asociar.

https://github.com/diegoandradecanosa/CFR24/blob/cec76daebbbd60d4ecdf4a3757147a3fab4d8ccb/pytorch_dist/fabric/mnist.py#L141-L152

El bucle de entrenamiento principal también consta de algunos elementos puntuales que están condicionados por el uso de fabric, como que la pasada backward
se llama a través del objeto *fabric*.

https://github.com/diegoandradecanosa/CFR24/blob/cec76daebbbd60d4ecdf4a3757147a3fab4d8ccb/pytorch_dist/fabric/mnist.py#L39-L54










