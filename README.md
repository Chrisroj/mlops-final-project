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