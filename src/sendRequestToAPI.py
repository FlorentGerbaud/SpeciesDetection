import requests
from typing import Dict, Any, Optional

class SpeciesDetectionAPIClient:
    def __init__(self, base_url: str):
        """
        Initializes the API client with a base URL for the Flask API.

        Args:
            base_url (str): The base URL of the Flask API.
        """
        self.base_url = base_url

    def predict(self, images_input_folder_path: Optional[str] = None,
                input_video_path: Optional[str] = None,
                type_of_data: str = "images") -> Dict[str, Any]:
        """
        Sends a POST request to the API for predictions on images or videos.

        Args:
            images_input_folder_path (Optional[str]): Path to the folder containing input images.
            input_video_path (Optional[str]): Path to the input video file.
            type_of_data (str): Specifies the type of data being sent ("images" or "video").

        Returns:
            Dict[str, Any]: JSON response from the API.
        """
        api_url = f"{self.base_url}/predict_{type_of_data}"
        
        # Map type_of_data to the appropriate data key
        data_map = {
            "images": {"images_input_folder_path": images_input_folder_path},
            "video": {"input_video_path": input_video_path}
        }
        
        # Retrieve data based on type_of_data, or raise an error if type_of_data is invalid
        if type_of_data not in data_map:
            raise ValueError("Invalid type_of_data. Expected 'images' or 'video'.")
        
        data = data_map[type_of_data]

        try:
            response = requests.post(api_url, json=data)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            error_message = f"Erreur de requête pour {type_of_data}: {e}"
            print(error_message)
            return {"error": error_message}

# Exemple d'utilisation
if __name__ == "__main__":
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
