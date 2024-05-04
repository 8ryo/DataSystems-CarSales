from utils.datasetup import *
import pandas as pd

blob_name =  "car_prices.csv"
database = AzureDB()
database.access_container("car-dataset"); 
df = database.access_blob_csv(blob_name= blob_name)

class ModelAbstract():
    def __init__(self):
        self.columns = None
        self.dimension_table = None
        
    def dimension_generator(self, name:str, columns:list):
        dim = df[columns]
        dim = dim.drop_duplicates()
        # Creating primary key for dimension table
        dim[f'{name}_id'] = range(1, len(dim) + 1)

        self.dimension_table = dim
        self.name = name
        self.columns = columns
        
        dim.to_csv(self.name + '.csv') 
        
    def load(self):
        if self.dimension_table is not None:
            # Upload dimension table to data warehouse
            database.upload_dataframe_sqldatabase(f'{self.name}_dim', blob_data=self.dimension_table)
        
            # Saving dimension table as separate file
            self.dimension_table.to_csv(f'./data/{self.name}_dim.csv')
        else:
            print("Please create a dimension table first using dimension_generator") 

class DimStaff(ModelAbstract):
    def __init__(self):
        super().__init__()
        self.dimension_generator('Model', ['Title', 'Brand', 'Year'])
            

