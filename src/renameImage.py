import os
import cv2
import customtkinter as ctk
from tkinter import filedialog, messagebox

def extract_frames(video_path, output_folder):
    # Ouvrir la vidéo
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Erreur lors de l'ouverture de la vidéo")
        return

    # Créer le dossier de sortie s'il n'existe pas
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Sauvegarder le cadre en tant que PNG
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:06d}.png")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

        print(f"Frame {frame_count} sauvegardé: {frame_filename}")

    cap.release()
    print("Extraction des images terminée")

def rename_images_and_labels(image_folder, label_folder, new_name):
    # Lister tous les fichiers images dans le dossier de sortie
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.png')]
    image_files.sort()  # Assurer que les fichiers sont triés

    for index, image_file in enumerate(image_files):
        # Construire le nouveau nom de fichier d'image
        new_image_filename = os.path.join(image_folder, f"{new_name}_{index:06d}.png")
        old_image_filename = os.path.join(image_folder, image_file)
        os.rename(old_image_filename, new_image_filename)
        print(f"Renamed image {old_image_filename} to {new_image_filename}")

        # Construire le nom du fichier label correspondant
        old_label_filename = os.path.join(label_folder, image_file.replace('.png', '.txt'))
        new_label_filename = os.path.join(label_folder, f"{new_name}_{index:06d}.txt")
        
        # Vérifier si le fichier label existe avant de renommer
        if os.path.exists(old_label_filename):
            os.rename(old_label_filename, new_label_filename)
            print(f"Renamed label {old_label_filename} to {new_label_filename}")

def select_video_path():
    video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi")])
    if video_path:
        video_path_entry.delete(0, ctk.END)
        video_path_entry.insert(0, video_path)

def select_image_folder():
    image_folder = filedialog.askdirectory()
    if image_folder:
        image_folder_entry.delete(0, ctk.END)
        image_folder_entry.insert(0, image_folder)

def select_label_folder():
    label_folder = filedialog.askdirectory()
    if label_folder:
        label_folder_entry.delete(0, ctk.END)
        label_folder_entry.insert(0, label_folder)

def process():
    video_path = video_path_entry.get()
    image_folder = image_folder_entry.get()
    label_folder = label_folder_entry.get()
    new_name = new_name_entry.get()
    
    if not (video_path and image_folder and label_folder and new_name):
        messagebox.showwarning("Avertissement", "Veuillez remplir tous les champs.")
        return

    extract_frames(video_path, image_folder)
    rename_images_and_labels(image_folder, label_folder, new_name)
    messagebox.showinfo("Succès", "Traitement terminé.")

# Configuration de l'interface graphique
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

root = ctk.CTk()
root.title("Extraction et renommage des images")

frame = ctk.CTkFrame(root)
frame.pack(padx=20, pady=20)

video_path_label = ctk.CTkLabel(frame, text="Chemin de la vidéo :")
video_path_label.pack(pady=5)
video_path_entry = ctk.CTkEntry(frame, width=400)
video_path_entry.pack(pady=5)
video_path_button = ctk.CTkButton(frame, text="Sélectionner la vidéo", command=select_video_path)
video_path_button.pack(pady=5)

image_folder_label = ctk.CTkLabel(frame, text="Dossier des images :")
image_folder_label.pack(pady=5)
image_folder_entry = ctk.CTkEntry(frame, width=400)
image_folder_entry.pack(pady=5)
image_folder_button = ctk.CTkButton(frame, text="Sélectionner le dossier", command=select_image_folder)
image_folder_button.pack(pady=5)

label_folder_label = ctk.CTkLabel(frame, text="Dossier des labels :")
label_folder_label.pack(pady=5)
label_folder_entry = ctk.CTkEntry(frame, width=400)
label_folder_entry.pack(pady=5)
label_folder_button = ctk.CTkButton(frame, text="Sélectionner le dossier", command=select_label_folder)
label_folder_button.pack(pady=5)

new_name_label = ctk.CTkLabel(frame, text="Nouveau nom :")
new_name_label.pack(pady=5)
new_name_entry = ctk.CTkEntry(frame, width=400)
new_name_entry.pack(pady=5)

process_button = ctk.CTkButton(frame, text="Lancer le traitement", command=process)
process_button.pack(pady=20)

root.mainloop()
