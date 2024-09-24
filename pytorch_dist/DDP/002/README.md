# Fully-Sharded Data Parallel Example

This example illustrates the use of a Fully-Sharded Data Parallel (FSDP) strategy, which is supported by Pytorch's native support for distributed training.

The launch scripts [ddpsrunSBATCH.sh](https://github.com/diegoandradecanosa/CFR24/blob/main/pytorch_dist/DDP/002/ddpsrunSBATCH.sh) and [trainfsdp.sh](https://github.com/diegoandradecanosa/CFR24/blob/main/pytorch_dist/DDP/002/trainfsdp.sh) are analogous to those from the DDP example.

The execution is performed by running the command:

```
sbatch ddpsrunSBATCH.sh
```
and the output would be generated in a file named *slurm-xxx.out* where *xxx* is the job identifier in SLURM.
The file [slurm-3413292](https://github.com/diegoandradecanosa/CFR24/blob/main/pytorch_dist/DDP/002/slurm-3413292.out) contains an example of the output generated during the execution.

The training script is where the most notable difference with the DDP example is concentrated. All the code is analogous to that example, except when applying the distributed training to the model, we use *FSDP()* instead of *DDP()*.

https://github.com/diegoandradecanosa/CFR24/blob/a09e3853f0e31223b19e9225dd648d7bfab4144d/pytorch_dist/DDP/002/fsdp.py#L143

# Ejemplo Fully-Sharded Data Parallel

Este ejemplo ilustra el uso de una estrategia Fully-Sharded Data Parallel (FSDP) que está soportada por el soporte nativo de Pytorch para entrenamientos distribuidos.

Los scripts de lanzamiento [ddpsrunSBATCH.sh](https://github.com/diegoandradecanosa/CFR24/blob/main/pytorch_dist/DDP/002/ddpsrunSBATCH.sh) y [trainfsdp.sh](https://github.com/diegoandradecanosa/CFR24/blob/main/pytorch_dist/DDP/002/trainfsdp.sh)
son análogos a los del ejemplo DDP.

La ejecución se realiza ejecutando el comando
```
sbatch ddpsrunSBATCH.sh
```
y la salida se generaría en un fichero con el nombre *slurm-xxx.out* donde *xxx* es el identificador del trabajo en SLURM.
El fichero [slurm-3413292](https://github.com/diegoandradecanosa/CFR24/blob/main/pytorch_dist/DDP/002/slurm-3413292.out) contiene un ejemplo de la salida generada durante la ejecución.

El script de entrenamiento es donde se concentran la diferencia más notable con el ejemplo DDP. Todo el código es análogo a aquel ejemplo, salvo que a la hora
de aplicar al modelo el entrenamiento distribuido, utilizadmos *FSDP()* en vez de *DDP()*.

https://github.com/diegoandradecanosa/CFR24/blob/a09e3853f0e31223b19e9225dd648d7bfab4144d/pytorch_dist/DDP/002/fsdp.py#L143



