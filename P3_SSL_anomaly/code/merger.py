import os
import shutil

def merge_images(source_dir, dest_dir):
    # Crée le dossier de destination s'il n'existe pas
    os.makedirs(dest_dir, exist_ok=True)

    # Parcourt tous les dossiers et fichiers dans le dossier source
    for dirpath, dirnames, filenames in os.walk(source_dir):
        # Récupère le numéro du sous-dossier
        # On obtient le chemin relatif du dossier par rapport au dossier source
        relative_path = os.path.relpath(dirpath, source_dir)
        subfolder_number = relative_path.replace(os.path.sep, '_')  # Remplace les séparateurs par '_'

        for filename in filenames:
            # Vérifie que c'est une image (ajoutez d'autres extensions si nécessaire)
            if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                # Chemin complet du fichier source
                source_file = os.path.join(dirpath, filename)

                # Ajoute le numéro de sous-dossier au nom du fichier
                base, extension = os.path.splitext(filename)
                new_filename = f"{base}_{subfolder_number}{extension}"

                # Chemin complet du fichier de destination
                dest_file = os.path.join(dest_dir, new_filename)

                # Si un fichier avec le même nom existe déjà, renommez le fichier
                if os.path.exists(dest_file):
                    counter = 1
                    while os.path.exists(dest_file):
                        dest_file = os.path.join(dest_dir, f"{base}_{subfolder_number}_{counter}{extension}")
                        counter += 1

                # Copie le fichier dans le dossier de destination
                shutil.copy2(source_file, dest_file)
                print(f"Copié: {source_file} -> {dest_file}")

# Exemple d'utilisation
source_dir = '../data/engine_wiring/test'  # Remplacez par votre chemin source
dest_dir = '../data/engine_wiring/test_merge'   # Remplacez par votre chemin de destination

merge_images(source_dir, dest_dir)
