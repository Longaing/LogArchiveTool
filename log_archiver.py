import os  #os : Pour interagir avec le système de fichiers
import tarfile   #tarfile : Pour créer des archives tar.gz
from datetime import datetime  #datetime : Pour obtenir la date/heure actuelle
import argparse #argparse : Pour gérer les arguments en ligne de commande
import sys

def archive_logs(log_directory):
    # Vérifier si le dossier existe
    if not os.path.isdir(log_directory):
        print(f"Erreur : Le dossier {log_directory} n'existe pas.")
        return False
    
    # Créer le nom de l'archive avec la date/heure
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")  # On crée un timestamp au format AAAAMMJJ_HHMMSS
    archive_name = f"logs_archive_{timestamp}.tar.gz"
    
    # Créer un dossier pour les archives si inexistant
    archive_dir = os.path.join(log_directory, "archives")
    os.makedirs(archive_dir, exist_ok=True)
    
    # Chemin complet de l'archive
    archive_path = os.path.join(archive_dir, archive_name)
    
    # Créer l'archive
    try:
        with tarfile.open(archive_path, "w:gz") as tar:
            for file in os.listdir(log_directory):
                file_path = os.path.join(log_directory, file)
                if os.path.isfile(file_path):  # Ne pas archiver les dossiers
                    tar.add(file_path, arcname=file)
        print(f"Archive créée avec succès : {archive_path}")
        return True
    except Exception as e:
        print(f"Erreur lors de la création de l'archive : {e}")
        return False
    
def main():
    # Configuration de l'analyseur d'arguments
    parser = argparse.ArgumentParser(
        description="Outil d'archivage de journaux - Compresse les logs dans une archive datée.")
    
    parser.add_argument(
        "log_directory",
        help="Chemin vers le dossier contenant les journaux à archiver")
    
    # Analyser les arguments
    args = parser.parse_args()
    
    # Appeler la fonction d'archivage
    archive_logs(args.log_directory)

if __name__ == "__main__":
    main()