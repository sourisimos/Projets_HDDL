from PIL import Image
import os

# Chemin du dossier racine contenant les fichiers PNG
root_folder = '../data_jpg/'

# Parcourt tous les dossiers et sous-dossiers
for dirpath, _, filenames in os.walk(root_folder):
    for filename in filenames:
        if filename.endswith('.png'):  # Vérifie si le fichier est un PNG
            img_path = os.path.join(dirpath, filename)
            
            # Ouvre l'image PNG
            with Image.open(img_path) as img:
                # Convertit l'image en mode RGB (nécessaire pour JPG)
                img = img.convert('RGB')
                
                # Définit le nom du fichier JPG
                jpg_filename = os.path.splitext(filename)[0] + '.jpg'
                
                # Sauvegarde dans le même dossier que le PNG
                jpg_path = os.path.join(dirpath, jpg_filename)
                
                # Sauvegarde l'image en JPG
                img.save(jpg_path, 'JPEG')
                print(f"Converti : {img_path} -> {jpg_path}")
                os.remove(img_path)
                print(f"Supression : {img_path}")
