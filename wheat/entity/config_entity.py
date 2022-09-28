from collections import namedtuple

# DataIngestionConfig
DataIngestionConfig = namedtuple(
    "DataIngestionConfig", [
        "dataset_download_url", # URL from which dataset is to be downloaded
        "tgz_download_dir", # Location where the compressed file is to be downloaded
        "raw_data_dir", # Location where the extracted file is to be saved
        "ingested_train_dir", # Location where the train dataset is to be saved
        "ingested_test_dir" # Location where the test dataset is to be saved
    ]
)

# DataValidationConfig 
DataValidationConfig = namedtuple(
    "DataValidationConfig", [
        "schema_file_path" # Location where the schema.yaml file is saved
    ]
)

# DataTransformationConfig 
DataTransformationConfig = namedtuple(
    "DataTransformationConfig", [
        "add_bedroom_per_room", # Not for this project
        "transformed_train_dir", # Location where the transformed train dataset is to be saved
        "transformed_test_dir", # Location where the transformed test dataset is to be saved
        "preprocessed_object_file_path" # Location where the data transformation (FEATURE ENGINEEING) pickle file is to be saved
    ]
)

# ModelTrainerConfig 
ModelTrainerConfig = namedtuple(
    "ModelTrainerConfig", [
        "base_accuracy", # Threshold value of accuracy. The model is to be accepted only when (model_accuracy > base_accuracy)
        "trained_model_file_path" # Location where the accepted trained model pickle file is to be saved
    ]
)

# ModelEvaluationConfig 
ModelEvaluationConfig = namedtuple(
    "ModelEvaluationConfig", [
        "trained_evaluation_file_path", # Location where the information about all the model in the production is saved
        "time_stamp" # Time stamp of model evaluation. 
    ]
)

# ModelPusherConfig 
ModelPusherConfig = namedtuple(
    "ModelPusherConfig", [
        "export_dir_path" # Location where the "model for deployed" is to be saved
    ]
)

# TrainingPipelineConfig
TrainingPipelineConfig = namedtuple(
    "TrainingPipelineConfig", [
        "artifact_dir" # Location where the generated atrifacts (outputs) is to be saved
    ]
)

# NOTE: The values for the above nametuples are specified in a "json" or ".yaml" or ".csv" file or DB
# NOTE: This file is read using Config/Config and the values for each Config variable is assigned form the ("json" or ".yaml" or ".csv" file or DB) respectively
# NOTE: Thus object of each Config variable is created