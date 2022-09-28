import os, sys
import re
from wheat.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, \
    ModelTrainerConfig, ModelEvaluationConfig, ModelPusherConfig, TrainingPipelineConfig
from wheat.constant import *
from wheat.util.util import read_yaml_file
from wheat.logger import logging
from wheat.exception import WheatException


class Configuration:

    def __init__(
        self,
        config_file_path:str = CONFIG_FILE_PATH,
        current_time_stamp:str = CURRENT_TIME_STAMP,
    ) -> None:
        try:
            self.config_info = read_yaml_file(config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_time_stamp
        except Exception as e:
            raise WheatException(e,sys) from e
    
    # for DataIngestionConfig
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            data_ingestion_config = self.config_info[DATA_INGESTION_CONFIG_KEY]
            dataset_download_url = data_ingestion_config[DATA_INGESTION_DOWNLOAD_URL_KEY]
            # All the folders created for outputs goes to "artifact" folder in training_pipeline_config
            data_ingestion_artifact_dir = os.path.join(
                self.training_pipeline_config.artifact_dir,
                DATA_INGESTION_ARTIFACT_DIR,
                self.time_stamp
            )
            tgz_download_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_config[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY]
            )          
            raw_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_config[DATA_INGESTION_RAW_DATA_DIR_KEY]
            )  
            ingested_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_config[DATA_INGESTION_INGESTED_DIR_KEY]
            )
            ingested_train_dir = os.path.join(
                ingested_dir,
                data_ingestion_config[DATA_INGESTION_TRAIN_DIR_KEY]
            )  
            ingested_test_dir = os.path.join(
                ingested_dir,
                data_ingestion_config[DATA_INGESTION_TEST_DIR_KEY]
            )  

            data_ingestion_config = DataIngestionConfig(
                dataset_download_url=dataset_download_url,
                tgz_download_dir=tgz_download_dir, 
                raw_data_dir=raw_data_dir, 
                ingested_train_dir=ingested_train_dir, 
                ingested_test_dir=ingested_test_dir
            )
            logging.info(f"Data Ingestion Config: {data_ingestion_config}")
            return data_ingestion_config
        except Exception as e:
            raise WheatException(e,sys) from e

    # for DataValidationConfig
    def get_data_validation_config(self) -> DataValidationConfig:
        try:
            pass
            data_validation_config = self.config_info[DATA_VALIDATION_CONFIG_KEY]
            schema_file_path = os.path.join(
                ROOT_DIR,
                CONFIG_DIR,
                data_validation_config[DATA_VALIDATION_SCHEMA_FILE_NAME_KEY]
            )
            
            data_validation_config = DataValidationConfig(
                schema_file_path=schema_file_path
            )
            logging.info(f"Data Validation Config: {data_validation_config}")
            return data_validation_config
        except Exception as e:
            raise WheatException(e,sys) from e


    # for DataTransformationConfig
    def get_data_transformation_config(self) -> DataTransformationConfig:
        try:
            pass
            data_transformation_config = self.config_info[DATA_TRANSFORMATION_CONFIG_KEY]
            # All the folders created for outputs goes to "artifact" folder in training_pipeline_config
            data_transformation_artifact_dir = os.path.join(
                self.training_pipeline_config.artifact_dir,
                DATA_TRANSFORMATION_ARTIFACT_DIR,
                self.time_stamp
            )
            transformed_dir = os.path.join(
                data_transformation_artifact_dir,
                data_transformation_config[DATA_TRANSFORMATION_TRANSFORMED_DIR_KEY]
            )
            transformed_train_dir= os.path.join(
                transformed_dir,
                data_transformation_config[DATA_TRANSFORMATION_TRANSFORMED_TRAIN_DIR_KEY]
            )
            transformed_test_dir =  os.path.join(
                transformed_dir,
                data_transformation_config[DATA_TRANSFORMATION_TRANSFORMED_TEST_DIR_KEY]
            )
            preprocessing_dir = os.path.join(
                data_transformation_artifact_dir,
                data_transformation_config[DATA_TRANSFORMATION_PREPROCESSING_DIR_KEY]
            )
            preprocessed_object_file_path = os.path.join(
                preprocessing_dir,
                data_transformation_config[DATA_TRANSFORMATION_PREPROCESSED_OBJECT_FILE_NAME_KEY]
            )


            data_transformation_config = DataTransformationConfig(
                transformed_train_dir=transformed_train_dir, 
                transformed_test_dir=transformed_test_dir, 
                preprocessed_object_file_path=preprocessed_object_file_path
            )
            logging.info(f"Data Transformation Config: {data_transformation_config}")
            return data_transformation_config
        except Exception as e:
            raise WheatException(e,sys) from e

    # for ModelTrainerConfig
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        try:
            model_trainer_config = self.config_info[MODEL_TRAINER_CONFIG_KEY]
            base_accuracy = model_trainer_config[MODEL_TRAINER_BASE_ACCURACY_KEY]
            model_trainer_artifact_dir = os.path.join(
                self.training_pipeline_config.artifact_dir,
                MODEL_TRAINER_ARTIFACT_DIR
            )
            trained_model_file_path = os.path.join(
                model_trainer_artifact_dir,
                model_trainer_config[MODEL_TRAINER_TRAINED_MODEL_DIR_KEY],
                model_trainer_config[MODEL_TRAINER_TRAINED_MODEL_FILE_NAME_KEY]
            )
            
            model_trainer_config = ModelTrainerConfig(
                base_accuracy=base_accuracy, 
                trained_model_file_path=trained_model_file_path
            )
            logging.info(f"Mode Trainer Config: {model_trainer_config}")
            return model_trainer_config
        except Exception as e:
            raise WheatException(e,sys) from e

    # for ModelEvaluationConfig
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        try:
            model_evaluation_config = self.config_info[MODEL_EVALUATION_CONFIG_KEY]
            trained_evaluation_file_path = os.path.join(
                ROOT_DIR,
                CONFIG_DIR,
                model_evaluation_config[MODEL_EVALUATION_FILE_NAME_KEY]
            )
            time_stamp = self.time_stamp

            model_evaluation_config =ModelEvaluationConfig(
                trained_evaluation_file_path=trained_evaluation_file_path,
                time_stamp=time_stamp
            )
            logging.info(f"model_evaluation_config: {model_evaluation_config}")
            return model_evaluation_config
        except Exception as e:
            raise WheatException(e,sys) from e


    # for ModelPusherConfig
    def get_model_pusher_config(self) -> ModelPusherConfig:
        try:
            model_pusher_config = self.config_info[MODEL_PUSHER_CONFIG_KEY]
            model_pusher_artifact_dir = os.path.join(
                self.training_pipeline_config.artifact_dir,
                MODEL_PUSHER_ARTIFACT_DIR
            )
            export_dir_path = os.path.join(
                model_pusher_artifact_dir,
                model_pusher_config[MODEL_PUSHER_MODEL_EXPORT_DIR_KEY]
            )
            
            model_pusher_config = ModelPusherConfig(export_dir_path=export_dir_path)
            logging.info(f"Model Pusher Config: {model_pusher_config}")
            return model_pusher_config
        except Exception as e:
            raise WheatException(e,sys) from e


    # for TrainingPipelineConfig
    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(
                ROOT_DIR,
                training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
                training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )
            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training Pipeline Config: {training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise WheatException(e,sys) from e



# When a function() is called its corresponding output is obtainted.
# To get DataIngestionConfig call get_data_ingestion_config()
# To get DataValidationConfig call get_data_validation_config()
# To get DataTransformationConfig call get_data_transformation_config()
# To get ModelTrainerConfig call get_model_trainer_config()
# To get ModelEvaluationConfig call get_model_trainer_config()
# To get ModelPusherConfig call get_model_pusher_config()
# To get TrainingPipelineConfig call get_training_pipeline_config()

# DataIngestionConfig 
# DataValidationConfig
# DataTransformationConfig 
# ModelTrainerConfig 
# ModelEvaluationConfig 
# ModelPusherConfig 
# TrainingPipelineConfig