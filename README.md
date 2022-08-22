# Churn Prediction Service

Churn is defined in business terms as ‘when a client cancels a subscription to a service they have been using.’

Source: [Churn Prediction](https://www.analyticsvidhya.com/blog/2021/08/churn-prediction-commercial-use-of-data-science/)

## Objective

Predict customers behavior is important to retain customers, then the idea of this project is to build a system to predict the customer churn in the telco market(customers have signed up for: phone, internet, treaming TV, etc.) to help telco companies to detect customers with potential churn and take right decisions to retain them.

To do that, in this project a classification model for churn is built, deployed and monitored.

## Data Source
Each row represents a customer, each column contains customer’s attributes described on the column Metadata.

The data set includes information about:

- Customers who left within the last month – the column is called Churn
- Services that each customer has signed up for – phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies
- Customer account information – how long they’ve been a customer, contract, payment method, paperless billing, monthly charges, and total charges
- Demographic info about customers – gender, age range, and if they have partners and dependents

Source: [Kaggle Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

## Technologies and Tools
- Cloud - [**Amazon Web Services**](https://aws.amazon.com/)
- Containerization - [**Docker**](https://www.docker.com) and [**Docker Compose**](https://docs.docker.com/compose/)
- Pre-Load Transformation - [**pandas**](https://pandas.pydata.org/)
- Model Development, Experiment Tracking, and Registration - [**scikit-learn**](https://scikit-learn.org/) and [**MLflow**](https://www.mlflow.org/)
- Model Monitoring - [**Evidently AI**](https://evidentlyai.com/)

## Setup








# Hacer instrucciones hasta para instalar jupyter

en el eda hay un churn report
The environment.yml will create and churn-env

# Primero
mlflow ui --backend-store-uri sqlite:///mlflow.db
y despues el tranining notebook

cuando corra de nuevo ver que el performance del modelo es el mismo
borrar mlruns y mldb

conda environtment to phase 1 and for prepare phase


Cosas a mejorar:
- Usar el mismo environment para el eda, entrenamiento y la de web service
-  Poner preprocesamiento de target de churn(cuando cambio yes por 1 y no por 0) en otro script(tal vez el de send_data o evidently_service).
- utilizar pipfile en evidently service y en docker-compose. Solo utilicé pipfile in prediction service
- Usar terraform

# Que mi proximo sea de predicción de bicis de la cdmx