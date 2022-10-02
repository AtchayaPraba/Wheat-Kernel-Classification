import os, sys
import numpy as np
import pandas as pd
from deepdiff import DeepDiff
from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab
import json
from wheat.logger import logging
from wheat.exception import WheatException
from wheat.util.util import read_yaml_file
from wheat.entity.config_entity import DataValidationConfig
from wheat.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact


# Class for DataValidationy
class DataValidation():

    def __init__(
        self,
        data_ingestion_artifact:DataIngestionArtifact,
        data_validation_config:DataValidationConfig
    ) -> None:
        try:
            logging.info(f"{'='*20}Data Validation log started{'='*20}")
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise WheatException(e,sys) from e

    # Function to check for avilablity of train and test file
    def is_train_test_file_exists(self)->bool:
        try:
            logging.info("Checking if training and test file is available")
            # Initializing the existance of train and test files
            is_train_file_exist = False
            is_train_file_exist = False

            # Get actual train and test file path from data_ingestion_artifact
            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path
            
            # Check for avilablity of train and test file and re-declaring "is_train_file_exist" & "is_train_file_exist"
            is_train_file_exist = os.path.exists(train_file_path)
            is_test_file_exist = os.path.exists(test_file_path)

            # Check weather both train and test file are present ("True and True"  -> True)
            is_available =  is_train_file_exist and is_test_file_exist

            logging.info(f"Is train and test file exists?-> {is_available}")

            # If is_available is "False"
            if not is_available:
                # Get actual train and test file path from data_ingestion_artifact
                training_file = self.data_ingestion_artifact.train_file_path
                testing_file = self.data_ingestion_artifact.test_file_path

                # Raise exception
                message=f"Training file: {training_file} or Testing file: {testing_file} is not present"
                raise Exception(message)

            # Else return avilable
            return is_available
        except Exception as e:
            raise WheatException(e,sys) from e

    # Function to read the train and test dataframe
    def get_train_and_test_df(self):
        try:
            # Read the train and test dataframe
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)

            return train_df,test_df
        except Exception as e:
            raise WheatException(e,sys) from e

    # Function to validate dataset schema
    def validate_dataset_schema(self)->bool:
        try:
            # Initializing the validation status as Flase
            validation_status = False

            # Read schema.yaml file
            schema_file_path = self.data_validation_config.schema_file_path
            schema = read_yaml_file(schema_file_path)

            # Read train and test dataframe
            train_df, test_df = self.get_train_and_test_df()

            # Assigment validate training and testing dataset using schema file
            # 1. Number of Columns and name each column
            # Columns for train_df and test_df
            train_df_col = list(train_df.columns)
            test_df_col = list(test_df.columns)

            # Sort list
            train_df_col.sort()
            test_df_col.sort()

            # datatype from schema.yaml file
            schema_col = list(schema["columns"].keys())

            # Sort list
            schema_col.sort()
            
            # Check for schema_match
            if (train_df_col == schema_col) and (test_df_col == schema_col):
                schema_match = True
            else:
                message=f"Training file or Testing file: NO schema_match"
                raise Exception(message)
            
            # 2. Check the domain value of target
            # From train_df and test_df
            train_df_domain_value_target = list(train_df['target'].unique())
            test_df_domain_value_target = list(test_df['target'].unique())

            # Sort list
            train_df_domain_value_target.sort()
            test_df_domain_value_target.sort()

            # From schema.yaml file
            schema_domain_value_target = schema['domain_value']['target']

            # Sort list
            schema_domain_value_target.sort()

            # Check for domain_value match
            if (train_df_domain_value_target == schema_domain_value_target) and (test_df_domain_value_target == schema_domain_value_target):
                domain_value_match = True
            else:
                message=f"Training file or Testing file: NO domain_value_match"
                raise Exception(message)

            # Re-assign validation_status as True
            validation_status = schema_match and domain_value_match

            # If validation_status is "False"
            if not validation_status:
                # Get actual train and test file path from data_ingestion_artifact
                training_file = self.data_ingestion_artifact.train_file_path
                testing_file = self.data_ingestion_artifact.test_file_path

                # Raise exception
                message=f"Training file: {training_file} or Testing file: {testing_file} does not match the schema"
                raise Exception(message)

            return validation_status
        except Exception as e:
            raise WheatException(e,sys) from e

    # Function to get and save data drift report
    def get_and_save_data_drift_report(self):
        try:
            # Create an object for DataDriftProfileSection() using Profile()
            profile = Profile(sections=[DataDriftProfileSection()])

            # Get train and test dataframe
            train_df,test_df = self.get_train_and_test_df()

            # Calculate data drift
            profile.calculate(train_df,test_df)

            # Generate datadrift report in .json format
            report = json.loads(profile.json())

            # Filepath to save the generated report
            report_file_path = self.data_validation_config.report_file_path

            # Get dir name to save the generated report from "report_file_path"
            report_dir = os.path.dirname(report_file_path)

            # Create dir
            os.makedirs(report_dir,exist_ok=True)

            # Write/dump the generated report to "report_file_path"
            with open(report_file_path,"w") as report_file:
                json.dump(report, report_file, indent=6)

            return report
        except Exception as e:
            raise WheatException(e,sys) from e

    def save_data_drift_report_page(self):
        try:
            # Create a object for DataDriftTab() using Dashboard()
            dashboard = Dashboard(tabs=[DataDriftTab()])

            #  # Get train and test dataframe
            train_df,test_df = self.get_train_and_test_df()

             # Calculate data drift
            dashboard.calculate(train_df,test_df)

            # Filepath to save the html page report
            report_page_file_path = self.data_validation_config.report_page_file_path

            # Get dir name to save the html page report from "report_page_file_path"
            report_page_dir = os.path.dirname(report_page_file_path)

            # Create dir
            os.makedirs(report_page_dir,exist_ok=True)

            # Save the html page report in "report_page_file_path"
            dashboard.save(report_page_file_path)
        except Exception as e:
            raise WheatException(e,sys) from e

    # Function to check for data drift
    def is_data_drift_found(self)->bool:
        try:
            # Call function get_and_save_data_drift_report()
            report = self.get_and_save_data_drift_report()

            # Call function save_data_drift_report_page()
            self.save_data_drift_report_page()

            # Write code based on the "report"
            #

            return True
        except Exception as e:
            raise WheatException(e,sys) from e

    # Top level function that calls the other functions one by one in a sequence
    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            # Call validation function is_available()
            self.is_train_test_file_exists()

            # Call validation function validate_dataset_schema()
            self.validate_dataset_schema()

            # Call validation function is_data_drift_found()
            self.is_data_drift_found()

            # DataValidationArtifact
            data_validation_artifact = DataValidationArtifact(
                schema_file_path=self.data_validation_config.schema_file_path, 
                report_file_path=self.data_validation_config.report_file_path, 
                report_page_file_path=self.data_validation_config.report_page_file_path, 
                is_validated=True,
                message="Data Validation performed successully"
            )
            
            logging.info(f"data_validation_artifact: {data_validation_artifact}")

            return data_validation_artifact
        except Exception as e:
            raise WheatException(e,sys) from e

    def __del__(self):
        logging.info(f"{'>>'*30}Data Valdaition log completed.{'<<'*30} \n\n")
