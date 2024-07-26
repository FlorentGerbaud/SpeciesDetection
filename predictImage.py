import subprocess

# Chemin de l'image à prédire
image_path = "/media/hdd_stockage/home/user/Vidéos/dauphinImage"

# URL de l'API Flask
api_url = "http://127.0.0.1:5000/predict_image"

# Commande curl pour envoyer la requête POST avec l'image comme données
curl_command = f'curl -X POST -H "Content-Type: application/json" -d \'{{"image_path": "{image_path}"}}\' {api_url}'

# Exécution de la commande curl
process = subprocess.Popen(curl_command, shell=True, stdout=subprocess.PIPE)
process.wait()

# Lecture de la sortie de la commande curl
response = process.stdout.read()

print(response.decode('utf-8'))
