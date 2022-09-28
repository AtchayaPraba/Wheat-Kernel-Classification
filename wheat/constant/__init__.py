import os
from datetime import datetime

# Declaring Hardcoded variables

ROOT_DIR = os.getcwd() # to get current working directory
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}" # to get current timestamp

# Config related variable:
CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)

# Training pipeline related variable:
TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_NAME_KEY = "pipeline_name"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY  = "artifact_dir"

# Data ingestion related variable:
DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY = "tgz_download_dir"
DATA_INGESTION_INGESTED_DIR_KEY = "ingested_dir"
DATA_INGESTION_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_TEST_DIR_KEY = "ingested_test_dir"

# Data Validation related variable:
DATA_VALIDATION_CONFIG_KEY = "data_validation_config"
DATA_VALIDATION_SCHEMA_FILE_NAME_KEY = "schema_file_name"

# Data Validation transformation variable:
DATA_TRANSFORMATION_CONFIG_KEY = "data_transformation_config"
DATA_TRANSFORMATION_ARTIFACT_DIR = "data_transformation"
# DATA_TRANSFORMATION_ADD_BED_ROOM_PER_ROOM_KEY = "add_bedroom_per_room" # Not for this project
DATA_TRANSFORMATION_TRANSFORMED_DIR_KEY = "transformed_dir"
DATA_TRANSFORMATION_TRANSFORMED_TRAIN_DIR_KEY = "transformed_train_dir"
DATA_TRANSFORMATION_TRANSFORMED_TEST_DIR_KEY = "transformed_test_dir"
DATA_TRANSFORMATION_PREPROCESSING_DIR_KEY = "preprocessing_dir"
DATA_TRANSFORMATION_PREPROCESSED_OBJECT_FILE_NAME_KEY = "preprocessed_object_file_name"

# Model Trainer variable:
MODEL_TRAINER_CONFIG_KEY = "model_trainer_config"
MODEL_TRAINER_ARTIFACT_DIR = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR_KEY = "trained_model_dir"
MODEL_TRAINER_TRAINED_MODEL_FILE_NAME_KEY = "trained_model_file_name"
MODEL_TRAINER_BASE_ACCURACY_KEY = "base_accuracy"
MODEL_TRAINER_MODEL_CONFIG_FILE_NAME_KEY = "model_config_file_name"

#  Model Evaluation variable:
MODEL_EVALUATION_CONFIG_KEY = "model_evaluation_config"
MODEL_EVALUATION_FILE_NAME_KEY = "model_evaluation_file_name"

#  Model Pusher variable:
MODEL_PUSHER_CONFIG_KEY = "model_pusher_config"
MODEL_PUSHER_ARTIFACT_DIR = "model_pusher"
MODEL_PUSHER_MODEL_EXPORT_DIR_KEY = "model_export_dir"  
