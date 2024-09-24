# DDP 101

This directory contains a basic example of *DataParallelism* and *DistributedDataParallelism* in the form of a [notebook](./pytorchDP101.ipynb).

Regarding the example of DataDistributedParallel (DDP), the more complex one, we must start by initializing the backend, in this case **nccl**:

https://github.com/diegoandradecanosa/CFR24/blob/6bee2ad14a551d7145d8074393672833ee010ba4/pytorch_dist/DDP/000/ddp.py#L28

Then, we take the **rank** of the current process and use it to select the device we will use. This example assumes a reservation of 1 node - n devices.

https://github.com/diegoandradecanosa/CFR24/blob/6bee2ad14a551d7145d8074393672833ee010ba4/pytorch_dist/DDP/000/ddp.py#L30-L34

Next, we construct the `ddp_model` through the DDP method, to which we pass:
- The original Pytorch model
- A list with the IDs of the devices used (global_rank)
- A list with the output devices (global_rank)

  https://github.com/diegoandradecanosa/CFR24/blob/6bee2ad14a551d7145d8074393672833ee010ba4/pytorch_dist/DDP/000/ddp.py#L40
  
  Data loading is done through a distributed **sampler**:

  https://github.com/diegoandradecanosa/CFR24/blob/6bee2ad14a551d7145d8074393672833ee010ba4/pytorch_dist/DDP/000/ddp.py#L42-L45  

  The optimizer uses the *ddp_model* as a parameter:

https://github.com/diegoandradecanosa/CFR24/blob/6bee2ad14a551d7145d8074393672833ee010ba4/pytorch_dist/DDP/000/ddp.py#L49

  The training loop has no peculiarities, except for associating the data with the Nvidia GPU:

  https://github.com/diegoandradecanosa/CFR24/blob/6bee2ad14a551d7145d8074393672833ee010ba4/pytorch_dist/DDP/000/ddp.py#L51-L62

# DDP 101

Este directorio contiene un ejemplo básico de *DataParallelism* y *DistributedDataParallelism* en forma de [notebook](./pytorchDP101.ipynb)

Respecto al ejemplo de DataDistributedParallel (DDP), el más complejo. Debemos empezar inicializando el backend, en este caso **nccl**

https://github.com/diegoandradecanosa/CFR24/blob/6bee2ad14a551d7145d8074393672833ee010ba4/pytorch_dist/DDP/000/ddp.py#L28

Luego, cogemos el **rank** del proceso actual y lo usamos para seleccionar el dispositivo que usaremos. Este ejemplo asume una reserva
de un 1 nodos - n dispositivos

https://github.com/diegoandradecanosa/CFR24/blob/6bee2ad14a551d7145d8074393672833ee010ba4/pytorch_dist/DDP/000/ddp.py#L30-L34

A continuación, construimos el ddp_model a través del método DDP, al cual le pasamos:
- El modelo original de Pytorch
- Una lista con los ids de los dispositivos utilizados (global_rank)
- Una lista con los dispositivos de salida (global_rank)

  https://github.com/diegoandradecanosa/CFR24/blob/6bee2ad14a551d7145d8074393672833ee010ba4/pytorch_dist/DDP/000/ddp.py#L40
  
  La carga de los datos se realiza a través de un **sampler** distribuido

  https://github.com/diegoandradecanosa/CFR24/blob/6bee2ad14a551d7145d8074393672833ee010ba4/pytorch_dist/DDP/000/ddp.py#L42-L45  

  El optimizador usa el *ddp_model* como parámetro

https://github.com/diegoandradecanosa/CFR24/blob/6bee2ad14a551d7145d8074393672833ee010ba4/pytorch_dist/DDP/000/ddp.py#L49

  El bucle de entrenamiento no tiene ninguna peculiaridad, salvo la asociación de los dastos con la GPU de Nvidia

  https://github.com/diegoandradecanosa/CFR24/blob/6bee2ad14a551d7145d8074393672833ee010ba4/pytorch_dist/DDP/000/ddp.py#L51-L62

