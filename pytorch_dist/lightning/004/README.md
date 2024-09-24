# Example of Custom Datasets

This example illustrates the use of *DataModules* in Lightning to create our own custom datasets. The code is distributed across two files:
- [mnist_datamodule.py](https://github.com/diegoandradecanosa/Cesga2023Courses/blob/main/pytorch_dist/lightning/004/mnist_datamodule.py) Contains the definition of the *DataModule*. In this case, it is a *DataModule* for the MNIST *DataSet*.
- [mnist_sample.py](https://github.com/diegoandradecanosa/Cesga2023Courses/blob/main/pytorch_dist/lightning/004/mnist_sample.py) Contains the code for distributed training in Lightning that uses this *DataModule*.

To run the example, we follow these steps:
```
compute  --gpu
source $STORE/mypython/bin/activate
python mnist_sample.py
```
- Request a node with a GPU.
- Activate the course environment.
- Execute the script directly with Python.

The definition of a custom *DataModule* in Lightning is done by defining a class that inherits from *LightningDataModule*:

https://github.com/diegoandradecanosa/CFR24/blob/22e5354139f7d35a4cfe27429b567750afbcff29/pytorch_dist/lightning/004/mnist_datamodule.py#L147

Implementations must be provided for all or several of these elements: *prepare_data, setup, train_dataloader, val_dataloader, test_dataloader*, and *predict_dataloader*.

Let's look at an example of the implementation of one of these methods for our example:

https://github.com/diegoandradecanosa/CFR24/blob/22e5354139f7d35a4cfe27429b567750afbcff29/pytorch_dist/lightning/004/mnist_datamodule.py#L207-L246

The defined *DataModule* is used in the main code as an additional argument to call the *MNISTDataModule*:

https://github.com/diegoandradecanosa/CFR24/blob/22e5354139f7d35a4cfe27429b567750afbcff29/pytorch_dist/lightning/004/mnist_sample.py#L56-L61


# Ejemplo de conjuntos de datos propios

Este ejemplo ilustra el uso de *DataModules* en Lightning para crear nuestros conjuntos de datos personalizados.
El código está distribuido en dos ficheros:
- [mnist_datamodule.py](https://github.com/diegoandradecanosa/Cesga2023Courses/blob/main/pytorch_dist/lightning/004/mnist_datamodule.py) Contiene la definición del 
*DataModule*. En este caso se trata de un *DataModule* para el *DataSet* MNIST.
- [mnist_sample.py](https://github.com/diegoandradecanosa/Cesga2023Courses/blob/main/pytorch_dist/lightning/004/mnist_sample.py) Contiene el código de un entrenamiento 
distribuido en Lightning que hace uso de ese *DataModule*.

Para ejecutar el ejemplo debemos seguir los siguientes pasos:
```
compute  --gpu
source $STORE/mypython/bin/activate
python mnist_sample.py
```
- Pedimos un nodo con una GPU 
- Activamos el entorno del curso
- Ejecutamos el script directamente con Python

La definición de un *DataModule* propio en Lightning se realiza definiendo una clase que hereda de *LightningDataModule*

https://github.com/diegoandradecanosa/CFR24/blob/22e5354139f7d35a4cfe27429b567750afbcff29/pytorch_dist/lightning/004/mnist_datamodule.py#L147

Se deben definir implementaciones para todos o varios de estos elementos: *prepare_data,setup,train_dataloader,val_dataloader,test_dataloader* y *predict_dataloader*.

Veamos un ejemplo de implementación de uno de estos métodos para nuestro ejemplo

https://github.com/diegoandradecanosa/CFR24/blob/22e5354139f7d35a4cfe27429b567750afbcff29/pytorch_dist/lightning/004/mnist_datamodule.py#L207-L246

El *DataModule* definido se usa en el código principal como un argumento más para llamar al *MNISTDataModule* 

https://github.com/diegoandradecanosa/CFR24/blob/22e5354139f7d35a4cfe27429b567750afbcff29/pytorch_dist/lightning/004/mnist_sample.py#L56-L61

