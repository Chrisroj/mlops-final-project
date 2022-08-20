# Initiate a gunicorn server for production

```bash
gunicorn --bind=0.0.0.0:9696 predict.py
```

**Note:** Gunicorn 'Green Unicorn' is a Python WSGI(Web Server Gateway Interface) HTTP Server for UNIX is incompatible with Windows.



```bash
docker build -t stroke-prediction-service:v1 .
```