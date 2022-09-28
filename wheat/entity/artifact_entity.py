# Contains the outpu information for every component

from collections import namedtuple

# DataIngestionArtifact 
DataIngestionArtifact = namedtuple(
    "DataIngestionArtifact",[
        "train_file_path",
        "test_file_path",
        "is_ingested",
        "message"
    ]
)

# DataValidationArtifact 
# DataTransformationArtifact
# ModelTrainerArtifact
# ModelEvaluationArtifact
# ModelPusherArtifact



