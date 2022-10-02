from distutils.command.config import config
import os,sys
from wheat.logger import logging
from wheat.exception import WheatException
from wheat.config.configuration import Configuration
from wheat.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from wheat.component.data_ingestion import DataIngestion
from wheat.component.data_validation import DataValidation


class Pipeline():

    def __init__(
        self,
        config:Configuration = Configuration()
    ) -> None:
        try:
            self.config = config
        except Exception as e:
            raise WheatException(e,sys) from e

    # Start DATA INGESTION componet
    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(
                data_ingestion_config=self.config.get_data_ingestion_config()
            )
            return data_ingestion.initiate_data_ingestion() # returns DataIngestionArtifact
        except Exception as e:
            raise WheatException(e,sys) from e

    # Start DATA VALIDATION componet
    def start_data_validation(
        self,
        data_ingestion_artifact:DataIngestionArtifact
    ) -> DataValidationArtifact:
        try:
            data_validation = DataValidation(
                data_ingestion_artifact=data_ingestion_artifact, 
                data_validation_config=self.config.get_data_validation_config()
            )
            return data_validation.initiate_data_validation()
        except Exception as e:
            raise WheatException(e,sys) from e


    # Start DATA TRANSFORMATION componet
    def start_data_transformation(self):
        pass

    # Start MODEL TRAINER componet
    def start_model_trainer(self):
        pass

    # Start MODEL EVALUATION componet
    def start_model_evaluation(self):
        pass

    # Start MODEL PUSHER componet
    def start_model_pusher(self):
        pass

    # Top level function that calls the other functions one by one in a sequence
    # This is the entire pipeline calling each componet one by one in a sequence
    def run_pipeline(self):
        try:
            # data ingestion
            data_ingestion_artifact = self.start_data_ingestion()
            # data validation
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
        except Exception as e:
            raise WheatException(e,sys) from e
            