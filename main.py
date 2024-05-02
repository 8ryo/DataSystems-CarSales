import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from dotenv import load_dotenv 
from utils.datasetup import *
import pandas as pd 

load_dotenv() 

account_storage = os.environ.get('ACCOUNT_STORAGE')
#print(account_storage) 

azureDB = AzureDB()
azureDB.access_container("car-dataset")
azureDB.list_blobs() 
df = azureDB.access_blob_csv("car_prices.csv")
print(df) 
