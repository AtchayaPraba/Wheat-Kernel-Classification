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
DataValidationArtifact = namedtuple(
    "DataValidationArtifact",[
        "schema_file_path",
        "report_file_path",
        "report_page_file_path",
        "is_validated",
        "message"
    ]
)

# DataTransformationArtifact
# ModelTrainerArtifact
# ModelEvaluationArtifact
# ModelPusherArtifact
