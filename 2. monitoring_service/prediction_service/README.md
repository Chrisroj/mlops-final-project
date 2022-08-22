# Initiate a gunicorn server for production

# ESTE README NO ES NECESARIO PRA LAS NOTAS FINALES PORQUE SE USARÁ DOCKER COMPOSE
```bash
gunicorn --bind=0.0.0.0:9696 predict.py
```

**Note:** Gunicorn 'Green Unicorn' is a Python WSGI(Web Server Gateway Interface) HTTP Server for UNIX is incompatible with Windows.



```bash
docker build -t churn-prediction-service:v1 .
```


```bash
docker run -it --rm -p 9696:9696  churn-prediction-service:v1
```



You need to make sure that the previous container you launched is killed, before launching a new one that uses the same port.

```bash
docker container ls
docker rm -f <container-name>
```