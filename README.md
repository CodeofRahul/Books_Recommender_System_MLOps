# End-to-End Book Recommender System MLops

[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/entbappy/End-to-End-Book-Recommender-System?style=social)](https://github.com/entbappy/End-to-End-Book-Recommender-System)
[![LinkedIn](https://img.shields.io/badge/Connect%20on-LinkedIn-blue.svg?logo=linkedin)](YOUR_LINKEDIN_PROFILE_URL_HERE)

## 📚 Project Overview

This repository presents a **robust, end-to-end Machine Learning Operations (MLOps) pipeline** for a Book Recommender System. Leveraging real-world book datasets, this project demonstrates the complete lifecycle of an ML solution, from **data ingestion and validation** to **model training, evaluation, and scalable deployment**.

The primary goal is to provide personalized book recommendations to users based on collaborative filtering principles. Beyond the recommendation logic, a core focus of this project is to exemplify **production-readiness**, **modular coding practices**, and **pipeline automation**, making it an ideal showcase for practical MLOps skills.

### ✨ Key Highlights:

* **Full MLOps Lifecycle:** Covers Data Ingestion, Data Validation, Data Transformation, Model Training, Evaluation, and Deployment.
* **Modular & Scalable Design:** Follows a component-based architecture for easy maintenance and expansion.
* **Automated Pipeline:** Orchestrates the entire ML workflow, reducing manual intervention and ensuring consistency.
* **Production-Ready Deployment:** Containerized application using Docker, prepared for seamless integration into cloud environments.
* **Comprehensive Data Handling:** Robust data validation and preprocessing steps ensure data quality and model reliability.

## 🚀 Features

* **Book Recommendation Engine:** Implements collaborative filtering to suggest books based on user ratings.
* **Automated Data Pipeline:** Scripts for downloading, cleaning, and preparing data for model training.
* **Model Training & Persistence:** Trains a Nearest Neighbors model and saves it efficiently for inference.
* **Performance Monitoring:** Includes basic mechanisms to log training and evaluation metrics.
* **Web Application Interface:** A simple web UI (via `app.py`) for interacting with the deployed recommender system.
* **Containerization:** `Dockerfile` for packaging the application and its dependencies into a portable unit.

## 🛠️ Technical Stack

* **Programming Language:** Python
* **Core Libraries:** `pandas`, `numpy`, `scikit-learn`
* **Web Framework:** Streamlit
* **Configuration Management:** `YAML` files
* **Logging & Exception Handling:** Custom robust logging and exception handling for production tracing.
* **Containerization:** Docker

## 📐 Project Architecture & MLOps Pipeline

This project is structured around a clear, sequential MLOps pipeline, ensuring data integrity, model quality, and efficient deployment.

.
├── artifacts/                  # Stores all pipeline outputs (data, models, processed files) <br>
│   ├── dataset/ <br>
│   │   ├── ingested_data/      # Raw downloaded data <br>
│   │   ├── clean_data/         # Processed and validated data <br>
│   │   └── raw_data/           # Original extracted data <br>
│   └── serialized_objects/     # Trained models, encoders, scalers <br>
├── books_recommender/          # Core source code for the ML pipeline components <br>
│   ├── config/                 # Configuration management (config.yaml, configuration.py) <br>
│   ├── entity/                 # Data classes/Pydantic models for configuration and data objects <br>
│   ├── components/             # Individual MLOps pipeline stages (Data Ingestion, Validation, etc.) <br>
│   ├── pipeline/               # Orchestrates the execution of components <br>
│   └── exception/              # Custom exception handling <br>
│   └── logger/                 # Custom logging utilities <br>
├── config/                     # Project configuration files <br>
│   └── config.yaml             # Main configuration for pipeline stages <br>
├── notebook/                   # Jupyter notebooks for experimentation, EDA, and model prototyping <br>
├── templates/                  # encoded book names <br>
├── .dockerignore               # Files/folders to ignore when building Docker image <br>
├── .gitignore                  # Files/folders to ignore in Git <br>
├── Dockerfile                  # Docker build instructions for containerizing the application <br>
├── README.md                   # Project documentation (this file) <br>
├── app.py                      # Flask/Web application for serving predictions <br>
├── main.py                     # Entry point for running the MLOps training pipeline <br>
├── requirements.txt            # Python dependencies <br>
├── setup.py                    # Setup file for package installation <br>
└── template.py                 # Boilerplate for new components/files <br>




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



### 🤝 Contributing
Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please open an issue or submit a pull request.

### 📧 Contact
Feel free to connect with me for any questions or collaborations!

**Rahul Kumar Sah**

- [GitHub](https://github.com/codeofrahul)

- [LinkedIn](https://www.linkedin.com/in/rahulkumarsah2/)