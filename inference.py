import sys
import os

currentDir=os.path.dirname(os.path.abspath(__file__))
srcDir=os.path.join(currentDir,'src')
sys.path.append(srcDir)

from src.predict import predict_on_images, predict_on_video

# Predict on a set of images using FishInv and MegaFauna models
predict_on_images(
    model_paths=["/media/hdd_stockage/home/user/SpeciesDetection/marine-detect/model/FishInv.pt", 
                 "/home/user/.pyenv/runs/detect/leMeilleur/weights/best.pt"],
    confs_threshold=[0.471, 0.6],
    images_input_folder_path="/media/hdd_stockage/home/user/SpeciesDetection/marine-detect/imageToProcess",
    images_output_folder_path="/media/hdd_stockage/home/user/SpeciesDetection/marine-detect/imagePostProcessing/modelFlo",
)

# Predict on a video using FishInv and MegaFauna models
# predict_on_video(
#     model_paths=["/media/hdd_stockage/home/user/SpeciesDetection/marine-detect/model/FishInv.pt", 
#                  "/home/user/.pyenv/runs/detect/train13/weights/best.pt"],
#     confs_threshold=[0.471, 0.6],
#     input_video_path="/media/hdd_stockage/home/user/SpeciesDetection/marine-detect/videoToProcess/wetransfer_videos-insitucam_2024-06-19_0629/vidéos insitucam/Broadcast_camera_B_CRA_du_04_09_2023_a_06h31_wipe.mp4",
#     output_video_path="/media/hdd_stockage/home/user/SpeciesDetection/marine-detect/videoPostProcessing/modelFlo/LastFineTuning/Broadcast_camera_B_CRA_du_04_09_2023_a_06h31_wipe.mp4",
# )

# in the repertory /home/user/marine-detect/videoToProcess/wetransfer_videos-insitucam_2024-06-19_0629/vidéos insitucam/ if there is a file with tortues inside it, applypredict_on_video on it

# for file in os.listdir("/media/hdd_stockage/home/user/SpeciesDetection/marine-detect/videoToProcess/wetransfer_videos-insitucam_2024-06-19_0629"):
#     if "Tortue" in file:
#         predict_on_video(
#             model_paths=["/media/hdd_stockage/home/user/SpeciesDetection/marine-detect/model/best.pt", "/media/hdd_stockage/home/user/SpeciesDetection/marine-detect/model/MegaFauna.pt"],
#             confs_threshold=[0.471, 0.6],
#             input_video_path="/media/hdd_stockage/home/user/SpeciesDetection/marine-detect/videoToProcess/wetransfer_videos-insitucam_2024-06-19_0629/"+file,
#             output_video_path="/media/hdd_stockage/home/user/SpeciesDetection/marine-detect/videoToProcess/"+file,
#         )
#         print("Tortue video number "+file.split("_")[1].split(".")[0]+"is processed"+" !")