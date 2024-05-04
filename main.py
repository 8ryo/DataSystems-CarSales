import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from dotenv import load_dotenv 
from utils.datasetup import *
import pandas as pd 
from utils.dimensions_classes import *

load_dotenv() 

model = ModelAbstract()
model.dimension_generator("Model", columns=['Title', 'Brand', 'Year'])
