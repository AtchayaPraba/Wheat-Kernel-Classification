import os, sys
from six.moves import urllib
import tarfile
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit
from wheat.exception import WheatException
from wheat.logger import logging
from wheat.entity.config_entity import DataIngestionConfig
from wheat.entity.artifact_entity import DataIngestionArtifact

class DataIngestion():

    def __init__(
        self,
        data_ingestion_config:DataIngestionConfig,
    ) -> None:
        try:
            logging.info(f"{'='*20}Data Ingestion log started{'='*20}")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
                raise WheatException(e,sys) from e

    # Function for data download
    def download_wheat_data(self):
        try:
            # URL to download dataset
            # Download URL obtained form entity/config_entity->DataIngestionConfig
            download_url = self.data_ingestion_config.dataset_download_url

            # Folder location to save the download file
            # Obtained form entity/config_entity->DataIngestionConfig
            tgz_download_dir = self.data_ingestion_config.tgz_download_dir

            # Remove folder if already exist
            if os.path.exists(tgz_download_dir):
                os.remove(tgz_download_dir)

            # Create the folder to save the download file
            os.makedirs(tgz_download_dir, exist_ok=True)

            # Extract file name from "download_url"
            wheat_file_name = os.path.basename(download_url)

            # Complete file path to save the download file
            tgz_file_path = os.path.join(tgz_download_dir,wheat_file_name)

            logging.info(f"Downloading file from: [{download_url}] into dir: [{tgz_file_path}]")

            # Download the data
            urllib.request.urlretrieve(download_url, tgz_file_path)

            logging.info(f"[{tgz_file_path}] has been downloaded successfully")

            return tgz_file_path
        except Exception as e:
            raise WheatException(e,sys) from e

    # Function for data extration
    def extract_tgz_file(
        self, 
        tgz_file_path:str
    ):
        try:
            # Folder location to save the extracted data
            # Obtained form entity/config_entity->DataIngestionConfig
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            # Remove folder if already exist
            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)

            # Create the folder to save the extracted data
            os.makedirs(raw_data_dir, exist_ok=True)

            logging.info(f"Extracting tgz_file from: [{tgz_file_path}] into dir: [{raw_data_dir}]")

            # Extract the data
            with tarfile.open(tgz_file_path) as wheat_tgz_file_obj:
                 wheat_tgz_file_obj.extractall(path=raw_data_dir)

            logging.info(f"Extraction of [{tgz_file_path}] is completed successfully")
        except Exception as e:
            raise WheatException(e,sys) from e

    # # Function for split data 
    def split_data_as_train_test(self)->DataIngestionArtifact:
        try:
            # Folder location where the extracted data is saved
            # Obtained form entity/config_entity->DataIngestionConfig
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            # Get the name of the file in raw_data_dir. raw_data_dir contains only one file
            file_name = os.listdir(raw_data_dir)[0]

            # Complete file path of extracted data
            wheat_file_path = os.path.join(raw_data_dir,file_name)

            logging.info(f"Reading .csv file: [{wheat_file_path}]")

            # Read the extracted data as dataframe
            wheat_data_frame = pd.read_csv(wheat_file_path)

            # Train-Test split
            # Create a new colunm in dataframe based on which StratifiedShuffleSplit is done
            wheat_data_frame["income_cat"] = pd.cut(wheat_data_frame["median_income"], 
                bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf], 
                labels=[1,2,3,4,5]
                )

            # Declaring Stratified train and test set
            strat_train_set = None
            strat_test_set = None

            logging.info(f"Split data into train and test")

            # Create an object for StratifiedShuffleSplit
            split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
            
            # Itterate over the dataframe
            for train_index, test_index in split.split(wheat_data_frame, wheat_data_frame["income_cat"]):
                strat_train_set = wheat_data_frame.loc[train_index].drop("income_cat", axis=1)
                strat_test_set = wheat_data_frame.loc[test_index].drop("income_cat", axis=1)

            # Complete train and test file path
            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir, file_name)
            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir, file_name)

            if strat_train_set is not None:
                # Create train folder
                os.makedirs(self.data_ingestion_config.ingested_train_dir, exist_ok=True)
                logging.info(f"Exporting train dataset to file: [{train_file_path}]")
                # Save train dataframe in train folder
                strat_train_set.to_csv(train_file_path, index=False)

            if strat_test_set is not None:
                # Create test folder
                os.makedirs(self.data_ingestion_config.ingested_test_dir, exist_ok=True)
                logging.info(f"Exporting test dataset to file: [{test_file_path}]")
                # Save test dataframe in test folder
                strat_test_set.to_csv(test_file_path, index=False)

            # Create an object of DataIngestionArtifact
            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path, 
                                                            test_file_path=test_file_path, 
                                                            is_ingested=True,
                                                            message=f"Data ingestion completed successfully"
                                                            )

            logging.info(f"Data Ingestion Artifact: [{data_ingestion_artifact}]")

            return data_ingestion_artifact
        except Exception as e:
            raise WheatException(e,sys) from e

    # Top level function that calls the other functions one by one in a sequence
    def initiate_data_ingestion(self)->DataIngestionArtifact:
        try:
            tgz_file_path = self.download_wheat_data()
            self.extract_tgz_file(tgz_file_path=tgz_file_path)
            self.split_data_as_train_test() 
        except Exception as e:
            raise WheatException(e,sys) from e

    def __del__(self):
        logging.info(f"Data Ingestion log completed".center(100,"="))
        