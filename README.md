# Wheat-Kernel-Classification
## Wheat Kernel Classification - Internship 01

## Software and account Resquirement
1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)

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

### Step 07: ESTABLISH CI/CD PIPELINE 
1. Create a new application in Heroku
2. Three information form "heroku" to setup CI/CD pipeline
    - 1. HEROKU_EMAIL = 
    - 2. HEROKU_APP_KEY = 
    - 3. HEROKU_APP_NAME = 

### Step 08: DOCKER IMAGE and DOCKER COMMANDAS
1. Create Docker file
2. Create .dockerignore file
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
>> NOTE: [MORE DOCKER COMMANDS](https://docs.docker.com/engine/reference/commandline/docker/)
