#!/usr/bin/env python3

import os
import sys
import subprocess

def main():
    # Vérifie que deux arguments sont passés
    if len(sys.argv) != 3:
        print("Usage: {} <path_to_dataset> <dataset_directory>".format(sys.argv[0]))
        sys.exit(1)

    # Assignation des arguments à des variables
    path_to_dataset = sys.argv[1]
    dataset_directory = sys.argv[2]

    # Chemin complet vers le répertoire de dataset
    full_path = os.path.join(path_to_dataset, dataset_directory)

    # Vérifie que le répertoire existe
    if not os.path.isdir(full_path):
        print("Error: Directory {} does not exist.".format(full_path))
        sys.exit(1)

    # Chemin vers le répertoire obj_train_data
    obj_train_data_path = os.path.join(full_path, 'obj_train_data')
    labels_path = os.path.join(full_path, 'labels')

    # Renommer obj_train_data en labels si obj_train_data existe
    if os.path.isdir(obj_train_data_path):
        os.rename(obj_train_data_path, labels_path)
        print("Renamed 'obj_train_data' to 'labels'.")
    elif not os.path.isdir(labels_path):
        print("Error: Neither 'obj_train_data' nor 'labels' directory exists.")
        sys.exit(1)

    # Exécution du script Python avec le chemin complet en argument
    try:
        subprocess.run(['python3', 'editClass.py', labels_path], check=True)
    except subprocess.CalledProcessError as e:
        print("Error: Execution of editClass.py failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
