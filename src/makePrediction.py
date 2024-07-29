# main.py
from pathlib import Path
from sendRequestToAPI import SpeciesDetectionAPIClient

def get_mp4_files(directory):
    """Récupère tous les chemins des fichiers .mp4 dans le répertoire spécifié."""
    return [str(file) for file in Path(directory).rglob('*.mp4')]

def main():
    # URL de base de l'API Flask
    base_url = "http://127.0.0.1:5000"
    
    # Création d'une instance de l'API Client
    client = SpeciesDetectionAPIClient(base_url)
    
    # Chemins des données
    image_path = "../imageToProcess"
    video_path = "../videoToProcess"
    
    choice=2
    
    if choice==1:
        
        # Prédiction sur les images
        print("Prédiction sur les images...")
        response_images = client.predict(images_input_folder_path=image_path, type_of_data="images")
        print("Réponse de l'API pour les images:", response_images)
        
    else:
        print("get mp4 files")
        mp4Files = get_mp4_files(video_path)
        print("files", mp4Files)
        # Prédiction sur la vidéo
        for videoPath in mp4Files:
            print("Prédiction sur la vidéo : ", videoPath)
            response_video = client.predict(input_video_path=videoPath, type_of_data="video")
            print("Réponse de l'API pour la vidéo:", response_video)
        

if __name__ == "__main__":
    main()
