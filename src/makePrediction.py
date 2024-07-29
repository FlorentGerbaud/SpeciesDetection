# main.py

from sendRequestToAPI import SpeciesDetectionAPIClient

def main():
    # URL de base de l'API Flask
    base_url = "http://127.0.0.1:5000"
    
    # Création d'une instance de l'API Client
    client = SpeciesDetectionAPIClient(base_url)
    
    # Chemins des données
    image_path = "../imageToProcess"
    video_path = "/media/hdd_stockage/home/user/SpeciesDetection/SpeciesDetection/videoToProcess/Broadcast_camera_B_CRA_du_04_09_2023_a_06h31_wipe.mp4"
    
    # Prédiction sur les images
    print("Prédiction sur les images...")
    response_images = client.predict(images_input_folder_path=image_path, type_of_data="images")
    print("Réponse de l'API pour les images:", response_images)
    
    # Prédiction sur la vidéo
    print("Prédiction sur la vidéo...")
    response_video = client.predict(input_video_path=video_path, type_of_data="video")
    print("Réponse de l'API pour la vidéo:", response_video)

if __name__ == "__main__":
    main()
