from moviepy.editor import VideoFileClip

# Charger la vidéo d'origine
input_video = "/home/user/marine-detect/videoToProcess/wetransfer_videos-insitucam_2024-06-19_0629/vidéos insitucam/banc_raie_InsituCam.mp4"
output_video = "/home/user/marine-detect/videoToProcess/wetransfer_videos-insitucam_2024-06-19_0629/vidéos insitucam/banc_raie_InsituCamCut.mp4"

# Charger le clip vidéo
clip = VideoFileClip(input_video)

# Couper le clip à 30 secondes
clip = clip.subclip(5, 10)  # de 0 à 30 secondes

# Convertir la vidéo à 10 fps
# new_clip = clip.set_fps(10)

# Sauvegarder la vidéo convertie et coupée
clip.write_videofile(output_video, fps=10)
