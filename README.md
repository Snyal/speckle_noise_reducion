VERRIER Thomas  
BORDES Alexandre

## Speckle noise reduction by DNN approch
![presentation](results/final_image_GAN.png)

**--- INFO ---**

Tous les fichiers disponible pour faire marcher les .pynb sont sur : 
https://drive.google.com/drive/folders/1XNnOYVZEzyqDjYsrrJQMzyRx70i-KAoH?usp=sharing

(il reste a votre charge de bien configurer les chemins d'accès)

Lien pour accéder aux images de test :  
https://www.kaggle.com/datasets/aryashah2k/breast-ultrasound-images-dataset/download?datasetVersionNumber=1

Les modèles utilisés :  
(pour essayer ces modèles utiliser les fichiers .ipynb)

- **DLSR** :  
https://github.com/faisalml/DeepLSR  
Vous pouvez trouver les resultats du DLSR dans `./data/results/DLSR`
    * compare : est la concaténation de l'image bruitée et débruitée
    * final : est l'image débruité
    * new : est l'image debruité avant le decoupage

- **RDUNET** :
https://github.com/JavierGurrola/RDUNet

- **DnCNN / BSRGAN** : 
https://github.com/cszn/KAIR

Les résultats sont disponibles ici (un appercu est disponible dans le dossier `./results`):  
https://drive.google.com/drive/folders/1vqLuvH4jQ5YR-P5_dBqRRocuRf0FBFLW?usp=share_link


