import azureml.core
from azureml.core import Workspace

ws = Workspace.from_config()


# Registering a model
description = "AutoML trained model"
model = run.register_model(description=description)

# A model ID is now accessible
print(run.model_id)


# Registering a already built model
import os
from azureml.core.model import Model

# assume 'models/' is a relative directory that contains uncompressed ONNX models
model = Model.register(
    workspace=ws,
    model_path="models/world_wines.onnx",
    model_name = "world_wines",
    tags={"onnx": "world-wines"},
    description="Image classification of world-wide wine labels"
)

# Or with command line
# az ml model register --name world_wines --model-path mnist/model.onnx


# Versioning Datasets
from azureml.core import Dataset
csv_url = ("https://automlsamplenotebookdata.blob.core.windows.net"
           "/automl-sample-notebook-data/bankmarketing_train.csv")
dataset = Dataset.Tabular.from_delimited_files(path=csv_url)

dataset = dataset.register(
    workspace=workspace,
    name="bankmarketing_dataset",
    description="Bankmarketing training data",
    create_new_version=True
)
# retrieve using
from azureml.core import Dataset

# Get a dataset by name and version number
bankmarketing_dataset = Dataset.get_by_name(
    workspace=workspace,
    name="bankmarketing_dataset",
    version=1
)