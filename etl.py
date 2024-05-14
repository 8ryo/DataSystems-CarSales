import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from dotenv import load_dotenv
import pandas as pd


def get_blob_service_client_token_credential(self):
    # TODO: Replace <storage-account-name> with your actual storage account name
    account_url = "https://newtestdatabase.blob.core.windows.net"
    credential = DefaultAzureCredential()

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient(account_url, credential=credential)

    return blob_service_client



    