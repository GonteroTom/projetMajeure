# Application de reconnaissance faciale

Ce projet est une application de reconnaissance faciale réalisée avec les librairies Streamlit, face_recognition et OpenCV.


## Utilisation

1.  Clonez le dépôt

```bash
git clone https://github.com/GonteroTom/projetMajeure.git
```
2.  Installez les dépendances 

```
pip install -r requirements.txt
```

3.  Lancez l'application 

```arduino
streamlit run facial_recognition.py
```


## Comment utiliser l'application

* Importez une photo en cliquant sur le bouton "Importer" et en choisissant une image dans votre ordinateur
* Présentez votre visage à votre webcam ou caméra afin que l'application confime votre identité (vérifiez que votre anti-virus autorise l'accès de la caméra à l'application)
* Cliquez sur le bouton "Confirmer" pour lancer le processus de reconnaissance faciale

Si l'identité est confirmée, un message de succès s'affiche, sinon le flux vidéo est affiché avec un message d'erreur.


## Fonctionnement 

La fonction ***'recognize_face(user_image)'*** utilise la bibliothèque ***'face_recognition'*** pour reconnaître les visages dans le flux vidéo de la webcam.
Elle prend en entrée une image de l'utilisateur, qui est utilisée pour créer une liste d'encodages de visages connus et de noms.
Après, elle initialise la webcam et commence à capturer des images. 

Pour chaque image capturée, elle convertit l'image en RGB et trouve les emplacements et encodages des visages.
Elle compare ensuite les encodages des visages détectés aux encodages de visages connus pour vérifier si l'utilisateur est bien le même que le visage de la photo. 
Si une correspondance est trouvée, elle retourne "Identité confirmée". Sinon, elle capture une image du flux de la webcam et affiche un message d'erreur "Identité non reconnue".

Enfin, elle libère la webcam et ferme la fenêtre.
