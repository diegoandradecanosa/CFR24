# Initial Lightning Example

This code contains a basic example of how to launch distributed training in Lightning within a distributed environment managed by SLURM.

The example is run by executing the command:

```
sbatch sampleLI.sbatch
```

It should generate an output similar to [slurm-3417863.out](https://github.com/diegoandradecanosa/CFR24/blob/main/pytorch_dist/lightning/000/slurm-3417863.out), but with the name corresponding to the SLURM job ID.

The training script is the file [sampleLI.py](https://github.com/diegoandradecanosa/CFR24/blob/main/pytorch_dist/lightning/000/sampleLI.py).

In the training script, the model definition must be done within a *LightningModule*:

https://github.com/diegoandradecanosa/CFR24/blob/40f1fbc4602610e2e2fe60f760f5b2d1bb99ba30/pytorch_dist/lightning/000/sampleLI.py#L10

which provides implementations for several methods:
- The constructor *__init__*, which contains the model definition.
- The implementation of the *forward* pass.
- The method to configure the optimizer(s): *configure_optimizers*.
- The definition of a *training_step*. Let's see its content in the code:
  https://github.com/diegoandradecanosa/CFR24/blob/40f1fbc4602610e2e2fe60f760f5b2d1bb99ba30/pytorch_dist/lightning/000/sampleLI.py#L30-L37

- The definition of a *validation_step*. Let's see its content in the code:

  https://github.com/diegoandradecanosa/CFR24/blob/40f1fbc4602610e2e2fe60f760f5b2d1bb99ba30/pytorch_dist/lightning/000/sampleLI.py#L39-L45

  By providing implementations for all these methods, using Lightning is really simple and involves just a few lines of code:

  https://github.com/diegoandradecanosa/CFR24/blob/40f1fbc4602610e2e2fe60f760f5b2d1bb99ba30/pytorch_dist/lightning/000/sampleLI.py#L48-L60

  Additionally, we see that Lightning can automatically detect and manage the *world_size* and *rank* provided by SLURM.

# Ejemplo inicial de Lightning

Este código contiene un ejemplo básico de cómo lanzar un entrenamiento distribuido en Lightning en un entorno distribuido gestionado con SLURM.

El ejemplo se lanza ejecutando el comando

```
sbatch sampleLI.sbatch
```
y debería generar una salida similar a [slurm-3417863.out](https://github.com/diegoandradecanosa/CFR24/blob/main/pytorch_dist/lightning/000/slurm-3417863.out)
pero con el nombre correspondiente al id del trabajo SLURM.

El script de entrenamiento es el fichero [sampleLI.py](https://github.com/diegoandradecanosa/CFR24/blob/main/pytorch_dist/lightning/000/sampleLI.py)

En el script de entrenamiento la definición del modelo se debe hacer dentro de un *LightningModule*

https://github.com/diegoandradecanosa/CFR24/blob/40f1fbc4602610e2e2fe60f760f5b2d1bb99ba30/pytorch_dist/lightning/000/sampleLI.py#L10

a través del cual se proporciona una implementación para varios métodos:
- El constructor *__init__* que contiene la definición del modelo
- La implementación de la pasada *forward*
- El método para configurar el/los optimizadores *configure_optimizers*
- La definición de un *training_step*. Veamos su contenido en el código.
  https://github.com/diegoandradecanosa/CFR24/blob/40f1fbc4602610e2e2fe60f760f5b2d1bb99ba30/pytorch_dist/lightning/000/sampleLI.py#L30-L37
  
- La definición de un *validation_step*. Veamos su contenido en el código.

  https://github.com/diegoandradecanosa/CFR24/blob/40f1fbc4602610e2e2fe60f760f5b2d1bb99ba30/pytorch_dist/lightning/000/sampleLI.py#L39-L45

  Si proporcionamos una implementación para todos esos métodos, el uso de Lightning es realmente sencillo e involucra unas pocas líneas de código

  https://github.com/diegoandradecanosa/CFR24/blob/40f1fbc4602610e2e2fe60f760f5b2d1bb99ba30/pytorch_dist/lightning/000/sampleLI.py#L48-L60

  Además, vemos que lightning es capaz de detectar y gestionar automáticamente el *world_size* y el *rank* proporcionados por SLURM.
  
