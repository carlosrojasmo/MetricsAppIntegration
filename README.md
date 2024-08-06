# Metrics App

Este proyecto es una aplicacion web de Python construida sobre con Flask que proveee metricas basicas del sistema como uso de CPU y RAM.

## Descarga
Clonar el repositorio:
   ```bash
   git clone https://github.com/your-username/Metrics-app.git
   cd Metrics-app
   ```
## Ejecución en python
```bash
python -m venv venv
source venv/bin/activate  # En windows usar venv\Scripts\activate`
pip install -r requirements.txt
python .\src\app.py
```
## Deployment

Para realizar el deploy de la app:

```bash
docker build -t metrics-app .
docker run -d -p 5000:5000 --name metrics-app-container --restart always metrics-app    
```

## Deploy via script deploy.sh
Para realizar el deploy via el script deploy.sh se le deben dar los permisos de ejecución y luego ejecutarlo lo cual creara la imagen en docker y luego levantara un contener con esta:
```bash
chmod +x deploy.sh
./deploy.sh
```
