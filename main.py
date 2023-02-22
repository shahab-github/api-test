from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def myhome():
    manifest = {
        "apiVersion": "v1",
        "kind": "Pod",
        "metadata": {
            "name": "example-pod"
        },
        "spec": {
            "containers": [
                {
                    "name": "example-container",
                    "image": "nginx"
                }
            ]
        }
    }
    return manifest


@app.get("/mydeploy")
def get_mydeploy():
    return FileResponse("mydeploy")

@app.get("/my-endpoint")
def my_endpoint():
    data = {
"name": "John",
"age": 30,
"city": "New York",
"another": "test01"
}
    return data

@app.get("/deploymeny")
def deployment():
    manifest = {
            "kind": "Deployment",
            "apiVersion": "apps/v1",
            "metadata": {
                "name": "mydeploy",
                "creationTimestamp": "null",
                "labels": {
                    "app": "mydeploy"
                }
            },
            "spec": {
                "replicas": 5,
                "selector": {
                    "matchLabels": {
                        "app": "mydeploy"
                    }
                },
                "template": {
                    "metadata": {
                        "creationTimestamp": "null",
                        "labels": {
                            "app": "mydeploy"
                        }
                    },
                    "spec": {
                        "containers": [
                            {
                                "name": "httpd",
                                "image": "httpd",
                                "resources": {}
                            }
                        ]
                    }
                },
                "strategy": {}
            },
            "status": {}
        }
    return manifest


@app.get('/index')
def index02():
    return FileResponse("file.html")