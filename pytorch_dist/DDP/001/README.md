# DDP Example n-nodes n-gpus

This example illustrates the use of DDP when a reservation of n-nodes is made on a supercomputer managed by the SLURM queue system, where each node has several GPUs (2 in this case).

First, let's look at the contents of the scripts that handle the SLURM reservation and launch the Python training script with that reservation.

The main script (`ddpsrunSBATCH.sh`) contains a preamble where we reserve:
- 2 nodes
- 2 tasks per node
- 1 A100 GPU per task
- 64 GB of RAM per node
- 32 cores for each task

https://github.com/diegoandradecanosa/CFR24/blob/cedf8e9165ed5fb79566ad5b39a72cf279695717/pytorch_dist/DDP/001/ddpsrunSBATCH.sh#L1-L9

This script must be launched with the command:

```
sbatch ddpsrunSBATCH.sh
```

The output will be collected in a file named *slurm-xxx.out* where *xxx* is the job identifier (an integer) in SLURM. The file [slurm-3396279.out](https://github.com/diegoandradecanosa/CFR24/blob/main/pytorch_dist/DDP/001/slurm-3396279.out) contains an example output.

Within the launch script, values relevant to the distributed execution are retrieved via SLURM environment variables and set through environment variables:
- The *MASTER_PORT* is set based on a calculation using the SLURM job PID.
- The *WORLD_SIZE* is retrieved directly from the *SLURM_NPROCS* environment variable.
- The *MASTER_ADDR* is retrieved using a SLURM command.

https://github.com/diegoandradecanosa/CFR24/blob/cedf8e9165ed5fb79566ad5b39a72cf279695717/pytorch_dist/DDP/001/ddpsrunSBATCH.sh#L11-L17

Finally, a secondary script, *mnist_classify_ddp.sh*, is launched with `srun`.

https://github.com/diegoandradecanosa/CFR24/blob/96bb2ead2b3eaaf88f754da818e762ac2555e848/pytorch_dist/DDP/001/ddpsrunSBATCH.sh#L22

The secondary script loads the conda environment and launches the training script, passing the number of epochs as a parameter.

https://github.com/diegoandradecanosa/CFR24/blob/96bb2ead2b3eaaf88f754da818e762ac2555e848/pytorch_dist/DDP/001/mnist_classify_ddp.sh#L3

## Training Script

Each worker from which the training script is launched (there will be as many copies launched as there are workers, 2x2 in the example) must execute the `init_process_group` method, initializing the backend and specifying its *rank*.

https://github.com/diegoandradecanosa/CFR24/blob/bc21128df69f854a297964b883275b3f54ea462b/pytorch_dist/DDP/001/mnist_classify_ddp.py#L73-L77

These values are obtained through environment variables set in the launch script or by SLURM.

https://github.com/diegoandradecanosa/CFR24/blob/bc21128df69f854a297964b883275b3f54ea462b/pytorch_dist/DDP/001/mnist_classify_ddp.py#L128-L131

Since we have several workers, each with a GPU per node, we need to establish which GPU each worker will use.

https://github.com/diegoandradecanosa/CFR24/blob/bc21128df69f854a297964b883275b3f54ea462b/pytorch_dist/DDP/001/mnist_classify_ddp.py#L140-L141

Again, efficient data loading is achieved by configuring a *DistributedSampler*.

https://github.com/diegoandradecanosa/CFR24/blob/bc21128df69f854a297964b883275b3f54ea462b/pytorch_dist/DDP/001/mnist_classify_ddp.py#L144-L147

DDP is called with the Pytorch model, specifying the *device_id* that the current worker will use.

https://github.com/diegoandradecanosa/CFR24/blob/bc21128df69f854a297964b883275b3f54ea462b/pytorch_dist/DDP/001/mnist_classify_ddp.py#L150

The training loop has nothing special except that, as in the previous case, we ensure that each batch goes to the correct device.

https://github.com/diegoandradecanosa/CFR24/blob/bc21128df69f854a297964b883275b3f54ea462b/pytorch_dist/DDP/001/mnist_classify_ddp.py#L39-L53

At the end of the training, it is a good practice to ensure the destruction of the distributed environment.

https://github.com/diegoandradecanosa/CFR24/blob/bc21128df69f854a297964b883275b3f54ea462b/pytorch_dist/DDP/001/mnist_classify_ddp.py#L162


# Ejemplo DDP n-nodos n-gpus

Este ejemplo ilustra el uso de DDP cuando se hace una revista de n-nodos en un supercomputador gestionado a través del sistema de colas SLURM. 
En el que a su vez cada nodo dispone de varias GPUs (2 en este caso).

Primero, veamos los contenidos de los scripts que realizan la reserva de SLURM y el lanzamiento del script python de entrenamiento con esa reserva.

El script principal (ddpsrunSBATCH.sh) contiene un preámbulo en el que reservamos:
- 2 nodos
- 2 tareas por nodo
- 1 gpu a100 por tarea
- 64 G de RAM por nodo
- y 32 núcleos para cada tarea

https://github.com/diegoandradecanosa/CFR24/blob/cedf8e9165ed5fb79566ad5b39a72cf279695717/pytorch_dist/DDP/001/ddpsrunSBATCH.sh#L1-L9

Este script debe ser lanzado con el comando:
```
sbatch ddpsrunSBATCH.sh
```
La salida se recogerá en un fichero con el nombre *slurm-xxx.out* donde *xxx* es el identificador (número entero) del trabajo en SLURM. 
El fichero [slurm-3396279.out](https://github.com/diegoandradecanosa/CFR24/blob/main/pytorch_dist/DDP/001/slurm-3396279.out)
contiene una salida de ejemplo.

Dentro del script de lanzamiento, se recuperan a través de variables de entorno de SLURM y se fijan a través de variables de entorno, valores que
serán relevante para la ejecución distribuida:
- Se establece el *MASTER_PORT* en base a un cálculo basado en el PID del trabajo SLURM
- Se recupera el *WORLD_SIZE* directamente de la variable de entorno *SLURM_NPROCS*
- Se recupera la *MASTER_ADDR* con un comando de SLURM

https://github.com/diegoandradecanosa/CFR24/blob/cedf8e9165ed5fb79566ad5b39a72cf279695717/pytorch_dist/DDP/001/ddpsrunSBATCH.sh#L11-L17

Finalmente, se lanza un script secundario, *mnist_classify_ddp.sh*, con srun.

https://github.com/diegoandradecanosa/CFR24/blob/96bb2ead2b3eaaf88f754da818e762ac2555e848/pytorch_dist/DDP/001/ddpsrunSBATCH.sh#L22

El script secundario carga el entorno conda y lanza el script de entrenamiento, pasando como parámetro el número de epochs

https://github.com/diegoandradecanosa/CFR24/blob/96bb2ead2b3eaaf88f754da818e762ac2555e848/pytorch_dist/DDP/001/mnist_classify_ddp.sh#L3

## Script de entrenamiento

Cada trabajador desde el que se lanza el script de entrenamiento (se van a lanzar tantas copias como trabajadores tengamos, 2x2 en el ejemplo) tiene que ejecutar
el método *init_process_group* inicializando el backend y especificando su *rank*

https://github.com/diegoandradecanosa/CFR24/blob/bc21128df69f854a297964b883275b3f54ea462b/pytorch_dist/DDP/001/mnist_classify_ddp.py#L73-L77

Estos valores se obtiene a través de variables de entorno fijadas en el script de lanzamiento o por SLURM

https://github.com/diegoandradecanosa/CFR24/blob/bc21128df69f854a297964b883275b3f54ea462b/pytorch_dist/DDP/001/mnist_classify_ddp.py#L128-L131

Al ser un entorno en el que tenemos varios trabajadores, cada uno con una GPU, por nodo, necesitamos establecer qué GPU usará cada uno.

https://github.com/diegoandradecanosa/CFR24/blob/bc21128df69f854a297964b883275b3f54ea462b/pytorch_dist/DDP/001/mnist_classify_ddp.py#L140-L141

De nuevo, la carga eficiente de los datos se hace configurando un *DistributedSampler*

https://github.com/diegoandradecanosa/CFR24/blob/bc21128df69f854a297964b883275b3f54ea462b/pytorch_dist/DDP/001/mnist_classify_ddp.py#L144-L147

Se llama a DDP con el modelo Pytorch y especificando el dispositivo *device_id* que utilizará el trabajador actual.

https://github.com/diegoandradecanosa/CFR24/blob/bc21128df69f854a297964b883275b3f54ea462b/pytorch_dist/DDP/001/mnist_classify_ddp.py#L150

El bucle de entrenamiento no tiene nada especial salvo que, como en el caso anterior, nos aseguramos de que cada batch vaya al dispositivo adecuado.

https://github.com/diegoandradecanosa/CFR24/blob/bc21128df69f854a297964b883275b3f54ea462b/pytorch_dist/DDP/001/mnist_classify_ddp.py#L39-L53

Al final del entrenamiento, es una buena práctica asegurarnos la destrucción del entorno distribuido

https://github.com/diegoandradecanosa/CFR24/blob/bc21128df69f854a297964b883275b3f54ea462b/pytorch_dist/DDP/001/mnist_classify_ddp.py#L162







