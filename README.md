# rickandmortyapp
Simple python app which getting all characters that:
```
1. They are alive.
2. They are humans.
3. Their origins is Earth.
```

### To run the app locally:
```
1. clone the repository.
2. run: pip install -r requirements.txt
3. run: python app.py
```
### To run app in a Container:
```
1. Build the containter:
   docker build -t rickapp .

2. run the container:
   docker run -d --name rickappv1 --publish 3000:3000 rickapp
```
### To run app in k8s:
```
1. Install and start minikube.
2. Run kubectl apply -f yaml/
3. Browse to the host specified in ingress.yaml
```