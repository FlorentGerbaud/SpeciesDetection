import os
import shutil
import random
import ultralytics
from tqdm import tqdm  # Importer tqdm pour la barre de progression

#______________________________________________ Function to split the dataset _______________________________________________________________________________________

# brief: Split the dataset into training and validation sets

# param: images_folder (str): Path to the folder containing images
# param: labels_folder (str): Path to the folder containing labels
# param: output_folder (str): Path to the output folder (where you will show the dataset train and val)

#output: None

def split_dataset(images_folder, labels_folder, output_folder):
    # Assurez-vous que les dossiers de sortie existent
    os.makedirs(os.path.join(output_folder, 'train', 'images'), exist_ok=True)
    os.makedirs(os.path.join(output_folder, 'train', 'labels'), exist_ok=True)
    os.makedirs(os.path.join(output_folder, 'val', 'images'), exist_ok=True)
    os.makedirs(os.path.join(output_folder, 'val', 'labels'), exist_ok=True)

    # Récupérer la liste de toutes les images dans le dossier d'entrée
    image_files = [f for f in os.listdir(images_folder) if os.path.isfile(os.path.join(images_folder, f))]

    # Mélanger les fichiers de manière aléatoire
    random.shuffle(image_files)

    # Calculer le nombre de fichiers pour l'ensemble d'entraînement
    split_ratio = 0.9  # 90% des données dans l'ensemble d'entraînement
    train_size = int(len(image_files) * split_ratio)

    # Diviser les fichiers en ensembles d'entraînement et de validation
    train_files = image_files[:train_size]
    val_files = image_files[train_size:]

    # Copier les fichiers d'images dans les dossiers correspondants
    print("Copying training images and labels...")
    for f in tqdm(train_files, desc='Training Images'):
        shutil.copy(os.path.join(images_folder, f), os.path.join(output_folder, 'train', 'images', f))
        # Copier les annotations correspondantes
        label_file = f.replace('.jpg', '.txt').replace('.JPG', '.txt').replace('.png', '.txt').replace('.PNG', '.txt').replace('.JPEG', '.txt').replace(".jpeg", ".txt").replace(".mpo", ".txt")
        shutil.copy(os.path.join(labels_folder, label_file), os.path.join(output_folder, 'train', 'labels', label_file))

    # Copier les fichiers d'images dans les dossiers correspondants
    print("Copying validation images and labels...")
    for f in tqdm(val_files, desc='Validation Images'):
        shutil.copy(os.path.join(images_folder, f), os.path.join(output_folder, 'val', 'images', f))
        # Copier les annotations correspondantes
        label_file = f.replace('.jpg', '.txt').replace('.JPG', '.txt').replace('.png', '.txt').replace('.PNG', '.txt').replace('.JPEG', '.txt').replace(".jpeg", ".txt").replace(".mpo", ".txt")
        shutil.copy(os.path.join(labels_folder, label_file), os.path.join(output_folder, 'val', 'labels', label_file))

    print(f'Total images: {len(image_files)}')
    print(f'Train images: {len(train_files)}')
    print(f'Validation images: {len(val_files)}')


# choice = 1 -> "Repartition of the dataset"
# choice = 2 -> "Training the model"
# choice = 3 -> Fine-tuning the model

choice=1

if choice==1:

    # Utilisation de la fonction pour répartir les données
    images_folder = '/home/user/Téléchargements/Turtles Face/test'
    labels_folder = '/home/user/Téléchargements/Turtles Face/obj_train_data'
    output_folder = '/home/user/Téléchargements/Turtles Face'

    split_dataset(images_folder, labels_folder, output_folder)


# ____________________________________________________ if you wish to train with the best parameters or your own parameters __________________________________________________________________________________________

if choice==2:

    # Initisialisation of the model 
    model = ultralytics.YOLO('/media/hdd_stockage/home/user/SpeciesDetection/marine-detect/model/MegaFauna.pt')  # ou 'path/to/your/model.pt'

    # Define the training parameters
    training_params = {
        'data': '/media/hdd_stockage/home/user/SpeciesDetection/marine-detect/DataSet/MegaFauna-dataset/notebooks/datasets/MegaFauna/test/trainMegaFauna.yaml',  # Chemin vers le fichier de configuration du dataset
        'epochs': 50,  # Nombre d'époques
        'batch': 5,  # Auto mode pour la taille du lot (60% de la mémoire GPU)
        'imgsz': 640,  # Taille des images
        'device': 0,  # Utilisation du premier GPU
        'optimizer': 'AdamW',  # Optimiseur SGD
        'amp': True,  # Activer l'entraînement en précision mixte
        'workers': 8,  # Nombre de threads de travail pour le chargement des données
        'save': True,  # Enregistrer les checkpoints et les poids finaux
        'val': True,  # Activer la validation pendant l'entraînement
        'lr0': 0.00972,
        'lrf': 0.00801,
        'momentum': 0.88422,
        'weight_decay': 0.0006,
        'warmup_epochs': 3.09486,
        'warmup_momentum': 0.95,
        'box': 8.0997,
        'cls': 0.47881,
        'dfl': 1.82474,
        'hsv_h': 0.01385,
        'hsv_s': 0.64343,
        'hsv_v': 0.37346,
        'degrees': 0.0,
        'translate': 0.06724,
        'scale': 0.48052,
        'shear': 0.0,
        'perspective': 0.0,
        'flipud': 0.0,
        'fliplr': 0.38248,
        'bgr': 0.0,
        'mosaic': 1.0,
        'mixup': 0.0,
        'copy_paste': 0.0
    }

    # Lancer l'entraînement
    model.train(**training_params)

if choice==3:
    # fix the parameters of the model which still unmodified during the fine-tuning
    # all the other parameters are modified during the fine-tuning to try to improve the model
    model.tune(data="/media/hdd_stockage/home/user/SpeciesDetection/marine-detect/DataSet/MegaFauna-dataset/notebooks/datasets/MegaFauna/test/trainMegaFauna.yaml",
            epochs=50,
            batch=5,
            optimizer="AdamW")

