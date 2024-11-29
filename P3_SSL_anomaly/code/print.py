
import os
import re 
import matplotlib.pyplot as plt
from PIL import Image

def display_images_from_folders(path, num_good=1, num_bad=3):
    abs = os.path.abspath("../"+path)
    good_path = os.path.join(abs, '0_good')
    bad_path = os.path.join(abs, '1_defective')

    good_images = sorted([os.path.join(good_path, img) for img in os.listdir(good_path) if img.endswith(('png', 'jpg', 'jpeg'))])
    bad_images = sorted([os.path.join(bad_path, img) for img in os.listdir(bad_path) if img.endswith(('png', 'jpg', 'jpeg'))])

    # Limiter le nombre d'images à afficher
    good_images = good_images[:num_good]
    bad_images = bad_images[:num_bad]

    # Créer une grille pour afficher les images
    total_images = num_good + num_bad
    _, axes = plt.subplots(1, total_images, figsize=(15, 5))

    for i, img_path in enumerate(good_images + bad_images):
        image = Image.open(img_path)

        axes[i].imshow(image)
        if i < num_good:
            axes[i].set_title("Good")
        else:
            img_name = os.path.basename(img_path)  # Récupère le nom du fichier
            title = img_name.split('_', 1)[-1] if '_' in img_name else ''  # Prend ce qu'il y a après "_"
            title = (': '+title.split('.', 1)[0]) if "." in title else ''
            axes[i].set_title("Bad"+title)
        axes[i].axis('off')

    plt.tight_layout()
    plt.show()
    return None