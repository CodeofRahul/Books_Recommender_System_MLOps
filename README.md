# Books_Recommender_System_MLOps
This project showcases a complete, end-to-end book recommender system, demonstrating the entire MLOps lifecycle. It covers data processing, model training, evaluation, and deployment. With a modular codebase and pipeline automation, this repository highlights practical skills in building and deploying production-ready ML applications.


## Workflow

- config.yaml
- entity
- config/configuration.py
- components
- pipeline
- main.py
- app.py


# How to run?

### STEPS:

Clone the repository:

```bash
git clone https://github.com/CodeofRahul/Books_Recommender_System_MLOps.git
```

### STEP 01: Create a conda environment:

```bash
conda create -p books python=3.7.10 -y
```

```bash
conda activate books/
```

### STEP 02: Install the required packages:

```bash
pip install -r requirements.txt
```

Now run,

```
streamlit run app.py
```

**Create folder/dir**

```bash
mkdir notebook
```

**Create a file**

```bash
null> notebook/research.ipynb
```

**Dataset Link**: https://www.kaggle.com/datasets/saurabhbagchi/books-dataset


# Streamlit app Docker Image Deployment

### 1. Login with your AWS console and launch an EC2 instance

### 2. Run the following commands

**Note**: Do the port mapping to this port:- 8501

```bash
sudo apt-get update -y

sudo apt-get upgrade

#Install Docker

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

```bash
git clone "your-project"
```

```
docker build -t rahul130/bookrec:latest . 
```

```
docker images -a  
```

```
docker run -d -p 8501:8501 rahul130/bookrec 
```

```
docker ps  
```

```
docker stop container_id
```

```
docker rm $(docker ps -a -q)
```

```
docker login 
```

```
docker push rahul130/bookrec:latest 
```

```
docker rmi rahul130/bookrec:latest
```

```
docker pull rahul130/bookrec
```
