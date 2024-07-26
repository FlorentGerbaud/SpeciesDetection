import os
import glob
import customtkinter as ctk
from tkinter import filedialog, messagebox

def process_files(repertoire, valeur_remplacement):
    # Ajoute un espace après la valeur de remplacement et enlève les espaces en excès
    valeur_remplacement = valeur_remplacement.strip() + " "

    # Utilisation de glob pour obtenir tous les fichiers .txt dans le répertoire
    fichiers_txt = glob.glob(os.path.join(repertoire, '*.txt'))

    # Parcourir chaque fichier .txt trouvé
    for fichier in fichiers_txt:
        with open(fichier, 'r+') as f:
            lignes = f.readlines()  # Lire toutes les lignes du fichier
            
            # Vérifier si le fichier n'est pas vide
            if lignes:
                f.seek(0)  # Retourner au début du fichier
                f.truncate()  # Effacer le contenu existant (pour réécrire avec les modifications)

                for ligne in lignes:
                    if ligne.strip():  # Vérifier si la ligne n'est pas vide
                        # Remplacer les deux premiers caractères par la valeur choisie avec un espace
                        nouvelle_ligne = valeur_remplacement + ligne[2:].lstrip()
                        f.write(nouvelle_ligne)  # Écrire la ligne modifiée dans le fichier
                    else:
                        f.write('\n')  # Écrire une ligne vide si la ligne était vide dans le fichier original

def select_directory():
    repertoire = filedialog.askdirectory()
    if repertoire:
        valeur_remplacement = entry.get()
        if valeur_remplacement:
            process_files(repertoire, valeur_remplacement)
            messagebox.showinfo("Succès", "Le traitement des fichiers est terminé.")
        else:
            messagebox.showwarning("Avertissement", "Aucune valeur de remplacement spécifiée.")
    else:
        messagebox.showwarning("Avertissement", "Aucun répertoire sélectionné.")

# Configuration de l'interface graphique
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

root = ctk.CTk()
root.title("Sélection du répertoire pour le traitement des fichiers .txt")

frame = ctk.CTkFrame(root)
frame.pack(padx=20, pady=20)

label = ctk.CTkLabel(frame, text="Cliquez sur le bouton pour sélectionner le répertoire contenant les fichiers .txt à traiter.")
label.pack(pady=10)

entry_label = ctk.CTkLabel(frame, text="Entrez la valeur de remplacement :")
entry_label.pack(pady=10)

entry = ctk.CTkEntry(frame)
entry.pack(pady=10)

button = ctk.CTkButton(frame, text="Sélectionner le répertoire", command=select_directory)
button.pack(pady=10)

root.mainloop()
