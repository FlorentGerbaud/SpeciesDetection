from flask import Flask, request, jsonify
from ultralytics import YOLO
import os
import sys
currentDir=os.path.dirname(os.path.abspath(__file__))
srcDir=os.path.join(currentDir,'src')
sys.path.append(srcDir)

from predict import predict_on_images, predict_on_video

app = Flask(__name__)

# Chemins des modèles et seuils de confiance
model_paths = [
    "../model/FishInv.pt",
    "../model/MegaFauna/bestFineTune.pt",
]
confs_threshold = [0.471, 0.6]

# Charger les modèles une seule fois
models = [YOLO(model_path) for model_path in model_paths]

@app.route('/predict_images', methods=['POST'])
def predict_images():
    data = request.json
    images_input_folder_path = data.get('images_input_folder_path')
    images_output_folder_path = "../imagePostProcessing/modelFlo"

    try:
        predict_on_images(
            models=models,
            confs_threshold=confs_threshold,
            images_input_folder_path=images_input_folder_path,
            images_output_folder_path=images_output_folder_path
        )
        return jsonify({'message': 'Prediction on images completed successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/predict_video', methods=['POST'])
def predict_video():
    data = request.json
    input_video_path = data.get('input_video_path')
    # Extraction du nom du fichier vidéo sans extension
    video_name = os.path.splitext(os.path.basename(input_video_path))[0]
    # Construction du chemin de la vidéo de sortie
    output_video_path = f"../videoPostProcessing/modelFlo/{video_name}.mp4"

    try:
        predict_on_video(
            models=models,
            confs_threshold=confs_threshold,
            input_video_path=input_video_path,
            output_video_path=output_video_path
        )
        return jsonify({'message': 'Prediction on video completed successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
