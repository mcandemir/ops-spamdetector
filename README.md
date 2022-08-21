## Ops-SpamDetection

### How to run?

1- Create a fresh cluster (I use kind in this case)
    
```shell
$ kind create cluster --name ops-spamdetector-c1
```


2- Create the deployment and service

```shell
$ kubectl create -f ops-spamdetector-depl.yaml
$ kubectl create -f ops-spamdetector-service.yaml
```

3- Forward web-api pod to your localhost port
```shell
$ kubectl port-forward pods/pod-name 8080:5000
```

4- Open your browser and go to 

    http://localhost:8080
