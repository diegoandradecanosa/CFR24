# Pytorch Profiler with Lightning

This example illustrates how to enable the use of Pytorch Profiler from Lightning.

To run the example, we need to:
- Open an interactive session on a computational node with a GPU (e.g., A100).
- Navigate to the example directory.
- Activate the `mytorchdist` environment.
- Run the training script.

```
srun --gres=gpu:a100:1 --time=00:59:00 --mem=16G -c 64 --pty bash
cd Cesga2023Courses/pytorch_dist/lightning/003
source $STORE/mytorchdist/bin/activate
python transformer.py
```

The profiler outputs will be generated in a directory named `lightning_logs`.
The files `fit-perf-logs.txt` and `test-perf-logs.txt` contain example profiler outputs for training and testing, respectively.

Regarding the example's code, the file [TransformerM.py](https://github.com/diegoandradecanosa/CFR24/blob/main/pytorch_dist/lightning/003/TransformerM.py) contains supporting definitions related to the model (Transformer type) and the dataset (WikiText2). These are not essential for understanding the example.

In the file [transformer.py](https://github.com/diegoandradecanosa/CFR24/blob/main/pytorch_dist/lightning/003/transformer.py), you can find the relevant code for this example, which is relatively simple:

https://github.com/diegoandradecanosa/CFR24/blob/7417c05f2a951cbfe6950f31710fbcd869f50cdd/pytorch_dist/lightning/003/transformer.py#L59-L60

A *PytorchProfiler* object is created, and this object is passed as an additional parameter to Lightning's *Trainer*.


# Pytorch Profiler con Lightning

Este ejemplo ilustra cómo habilitar el uso de Pytorch Profiler desde Lightning. 

Para ejecutar el ejemplo debemos:
- Abrir una sesión interactiva en un nodo computacional con una GPU (por ejemplo, A100)
- Entrar en el directorio del ejemplo
- Habilitar el entorno mytorchdist
- Ejecutar el script de entrenamiento

```
srun --gres=gpu:a100:1 --time=00:59:00 --mem=16G -c 64 --pty bash
cd Cesga2023Courses/pytorch_dist/lightning/003
source $STORE/mytorchdist/bin/activate
python transformer.py
```

Las salidas del profiler se generar en un directorio llamado lightning_logs.
Los ficheros fit-perf-logs.txt y test-perf-logs.txt contienen ejemplos de salida del profiler para entrenamiento y test respectivamente.

Respecto al código del ejemplo, el fichero [TransformerM.py](https://github.com/diegoandradecanosa/CFR24/blob/main/pytorch_dist/lightning/003/TransformerM.py)
contiene unas definiciones de apoyo relacionadas con el modelo a utilizar (tipo Transformer) y el conjunto de datos (WikiText2). No son relevantes para entender el ejemplo.

En el código del fichero [transformer.py](https://github.com/diegoandradecanosa/CFR24/blob/main/pytorch_dist/lightning/003/transformer.py)
es donde se encuentra el código relevante para el ejemplo que es relativamente sencillo:

https://github.com/diegoandradecanosa/CFR24/blob/7417c05f2a951cbfe6950f31710fbcd869f50cdd/pytorch_dist/lightning/003/transformer.py#L59-L60

Se crea un objeto de tipo *PytorchProfiler* y este objeto se pasa como un parámetro más del *Trainer* de Lightning.
