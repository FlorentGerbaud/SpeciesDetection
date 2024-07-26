from flask import Flask, request, jsonify
from ultralytics import YOLO
import os
import sys
currentDir=os.path.dirname(os.path.abspath(__file__))
srcDir=os.path.join(currentDir,'src')
sys.path.append(srcDir)

from marine_detect.predict import predict_on_images, predict_on_video

app = Flask(__name__)

# Chemins des modèles et seuils de confiance
model_paths = [
    "/media/hdd_stockage/home/user/SpeciesDetection/marine-detect/model/best.pt",
    "/media/hdd_stockage/home/user/SpeciesDetection/marine-detect/model/MegaFauna.pt",
]
confs_threshold = [0.471, 0.6]

# Charger les modèles une seule fois
models = [YOLO(model_path) for model_path in model_paths]

@app.route('/predict_images', methods=['POST'])
def predict_images():
    data = request.json
    images_input_folder_path = data.get('images_input_folder_path')
    images_output_folder_path = "/media/hdd_stockage/home/user/SpeciesDetection/marine-detect/imagePostProcessing"

    try:
        predict_on_images(
            model_paths=model_paths,
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
    output_video_path = "/media/hdd_stockage/home/user/SpeciesDetection/marine-detect/output_video.mp4"

    try:
        predict_on_video(
            model_paths=model_paths,
            confs_threshold=confs_threshold,
            input_video_path=input_video_path,
            output_video_path=output_video_path
        )
        return jsonify({'message': 'Prediction on video completed successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
