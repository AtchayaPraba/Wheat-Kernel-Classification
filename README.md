# Wheat-Kernel-Classification
## Wheat Kernel Classification - Internship 01

## Software and account Resquirement
1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)

## Install .ipynb kernel
```
pip install ipykernel
```

## Steps in Creating an End-to-End Machine Learing project:
### Step 01:
1. Create a GitHub Repository
2. Add README.md, .gitignore and LICENSE files

### Step 02:
1. Clone the GitHub Repository
```
git clone <github_repo_link>
```
2. Open in VS code. Launch VS Code in the pwd
```
code .
```

### Step 03: VIRTUAL ENVIRONMENT 
1. Create conda virtual environment 
```
conda create -p venv python==3.7 -y
```
2. Activate conda virtual environment
```
conda activate venv
```
OR
```
conda activate venv/
```
3. Initialize virtual environment 
```
conda init cmd.exe
```
>> NOTE: close and reopen VS code

### Step 04: "requirements.txt" FILE
1. Create requirements.txt file
2. Install requirements.txt file
```
pip install -r requirements.txt
``` 

### Step 05: CREATE app.py

### Step 06: GitHub COMMANDS
1. Check remote url
```
git remote -v
```
2. Check branch of repository
```
git branch
```
3. Add files to GitHub repository
```
git add <file_name>
```
OR
```
git add <file_name1>, <file_name2>, <file_name3>, ...<file_namen>
```
OR
```
git add .
```
4. Check file status
```
git status
```
5. Save / commit the changes in GitHub for version control 
```
git commit
```
OR 
```
git commit -m "any_message"
```
6. View the versions in GitHub
```
git log
```
7. Ssend version / changes to github repo
```
git push origin main
```
8. Download files form remote url
```
git pull
```
OR
```
git fetch
```
9. Check the difference
```
git diff
```
10. Restore file
```
git restore --staged <file_name>
```
>>NOTE: [MORE GIT COMMANDS](https://git-scm.com/docs/gittutorial)

### Step 07: ESTABLISH CI/CD PIPELINE 
1. Create a new application in Heroku
2. Three information form "heroku" to setup CI/CD pipeline
    1. HEROKU_EMAIL = 
    2. HEROKU_APP_KEY = 
    3. HEROKU_APP_NAME = 

### Step 08: DOCKER IMAGE and DOCKER COMMANDAS
1. Create Docker file 
2. Create .dockerignore files and mention the files to be ignored by docker
3. List of Docker image
```
docker images
```
4. Build Docker image
```
docker build -t <image_name>:<tagname> .
```
>> NOTE: image_name is always "lowercase"
5. Run Docker image
```
docker run -p 5000:5000 -e PORT=5000 <image_id>
```
6. Check running containers in Docker 
```
docker ps
```
7. List of containers in Docker
```
docker ps -a
```
8. Stop running container
```
docker stop <container_id>
```
>>NOTE: [MORE DOCKER COMMANDS](https://docs.docker.com/engine/reference/commandline/docker/)

### Step 09: CONTINOUS DEPLOYMENT
1. Create a folder .github
2. In .github create a folder workflows
3. In workflows create a file main.yaml 
    >> NOTE: Here we write the code for github actions
    >> NOTE: Bsically the tirgger we bind
    >> NOTE: The trigger automatically creates a docker image whenever changes are made in the main branch and automatically send the docker image to the deployment enviroment
    >>NOTE: The github actions are already mcreated by someone else and we are using it

### Step 10: CREATE setup.py FILE
1. Create folder wheat and inside wheat folder create __init__.py file
    >> NOTE: wheat is the root folder where the project code is present
    >> NOTE: Similar to the creation of library in sklearn so that we can inport the wheat folder anywhere as required
2. Create file setup.py
    >> NOTE: "pip install -r requirements.txt" 
    >> NOTE: Useful during deployment of project as a library
```
python setup.py install
```
    >> NOTE: any file (.py) is konwn as module and folder is known as package

### Step 11: CREATING FOLDERS INSIDE wheat FOLDER
1. logger
2. exception
3. pipeline
4. component
5. config
6. entity
>> NOTE: Each folder is created as a package and each folder shoul contain __init__.py file

### Step 12: LOGGER FOLDER
>> NOTE: To track all the progress during execution
1. Write code for logging in __init__.py file

### Step 13: EXCEPTION FOLDER
>> NOTE: To track the errors and unexpected behaviours during execution
>> NOTE: Capture the exceptional events
1. Write code for costum exception handling in __init__.py file

### Step 14: COMPONENT FOLDER
1. Create a module (.py file) for each componet of the ML pipeline in "component" folder
    1. data_ingestion.py (DATA INGESTION)
    2. data_validation.py (DATA VALIDATION)
    3. data_transformation.py (DATA TRANSFORMATION)
    4. model_trainer.py (MODEL SELECTION)
    5. model_evaluation.py (MODEL EVELUATION)
    6. model_pusher.py (PUSH MODEL)
>> NOTE: Each component module (.py file) perform its respective tasks

### Step 15: PIPELINE FOLDER
1. Create a module (.py file) for the entire ML pipeline in "pipeline" folder
    1. pipeline.py (MACHINE LEARNING PIPELINE)

### Step 16: CONFIG-INFO FOLDER
1. Create "config" folder outside the "wheat" folder (root dir). This contains the "json" or ".yaml" or ".csv" file or DB.

### Step 17: ENTITY FOLDER
1. In the "entity" folder the artifact and config for each and every component of the ML PIPELINE is define 

>> NOTE: The information/details about the "INPUTS" gievn to the components in the ML pipeline is konwn as config
>> NOTE: The config is prepared based on the source of inputs to the components. It contains the basic structure (parameters required) for inputs
>> NOTE: Config is like providing initial inputs to the components so that it can perform its tasks
2. Create config file: "config_entity.py" and create nametuples of variables:
    1. DataIngestionConfig (DATA INGESTION)
    2. DataValidationConfig (DATA VALIDATION)
    3. DataTransformationConfig (DATA TRANSFORMATION)
    4. ModelTrainerConfig (MODEL SELECTION)
    5. ModelEvaluationConfig (MODEL EVELUATION)
    6. ModelPusherConfig (PUSH MODEL)
    7. TrainingPipelineConfig (MACHINE LEARNING PIPELINE)
>> NOTE: The values for the above nametuples are specified in a "json" or ".yaml" or ".csv" file or DB
>> NOTE: This file is read using config/configuration.py and the values for each Config variable is assigned form the ("json" or ".yaml" or ".csv" file or DB) respectively
>> NOTE: Thus object of each Config variable is created

3. Create "json" or ".yaml" or ".csv" file or DB in which the values for above nametuples are specified. This stores the Config info (values for above nametuples). Create this in Config folder which is outside the "wheat" folder (root dir)

>> NOTE: When a machine learning pipeline is triggered it generates some outputs in every step.
>> NOTE: Each component in machine learning pipeline generates some "OUTPUTS" when triggered.These outputs are known as artifacts. Eg: file, image, report, etc
>> NOTE: When data ingestion component is triggered it produce X_train, y_train, X_test and y_test files as outputs. These outputs known as artifacts.
>> NOTE: Pickled model object is also an artifact
4. Create artifact file: "artifact_entity.py" 
    1. DataIngestionArtifact (DATA INGESTION)
    2. DataValidationArtifact (DATA VALIDATION)
    3. DataTransformationArtifact (DATA TRANSFORMATION)
    4. ModelTrainerArtifact (MODEL SELECTION)
    5. ModelEvaluationArtifact (MODEL EVELUATION)
    6. ModelPusherArtifact (PUSH MODEL)

### Step 18: CONFIG FOLDER
1. Reads the structure form the entity/config_entity.py file
2. Reads the config_info form the Config/config.yaml
3. Creates objects (functions) for each entity/confif_entity.py using the config_info form the Config/config.yaml
4. Provides the objects to config/configuration.py when required. This helps to configure every component of the pipeline.
5. Centralized configuration for the entire project

### Step 19: CONSTANT FOLDER
1. Create "constant" folder under "wheat" folder.
2. It contains all the "Hardcoded variables" and the "KEY"s for all the config/config.yaml file keys

### Step 20: 

### Step 21: 


### PICKLE FILE
>> NOTE: Creating an object of the class
>> NOTE: Saving/dump the object into a file is called serialization
>> NOTE: Loading object from a file is called de-serialization
>> NOTE: Pickle, dill and joblib are library that preforms serialization and de-serialization
>> NOTE: Model is also a "class" for which we have to create an "object" in order to perform serialization and de-serialization
