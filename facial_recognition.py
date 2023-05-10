import streamlit as st
import face_recognition as fr
import cv2


# Fonction pour reconnaître les visages et retourner le résultat sous forme de chaîne de caractères
def recognize_face(user_image):
    # Charger l'image de l'utilisateur et son encodage
    user_image = fr.load_image_file(user_image)
    user_face_encoding = fr.face_encodings(user_image)[0]

    # Créer une liste d'encodages de visages connus et de noms
    known_face_encodings = [user_face_encoding]

    # Initialiser la webcam
    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        st.error("Pas de caméra détectée.")
        return

    while True:
        # Capturer une image de la webcam
        ret, frame = video_capture.read()

        # Convertir l'image en RGB et trouver les emplacements et encodages des visages
        rgb_frame = frame[:, :, ::-1]
        face_locations = fr.face_locations(rgb_frame)
        face_encodings = fr.face_encodings(rgb_frame, face_locations)

        # Vérifier si l'un des visages détectés correspond aux encodages de visages connus
        for face_encoding in face_encodings:
            matches = fr.compare_faces(known_face_encodings, face_encoding)
            if True in matches:
                # Si une correspondance est trouvée, retourner "Identité confirmée"
                return "Identité confirmée."

        # Si aucune correspondance n'est trouvée, afficher le flux vidéo et demander à l'utilisateur de réessayer
        st.image(frame, channels="BGR")
        st.warning("Identité non reconnue.")
        break

    # Libérer la webcam et fermer la fenêtre
    video_capture.release()
    cv2.destroyAllWindows()


# Créer une application Streamlit
st.title("Application de reconnaissance faciale")
st.write("Veuillez importer une photo, puis présentez votre visage à la caméra pour vérifier votre identité.")

# Ajouter un bouton pour démarrer le processus de reconnaissance faciale
confirm_button = st.button("Confirmer")
uploaded_file = st.file_uploader("Importer", type=['jpg', 'jpeg', 'png'])

if confirm_button:
    if uploaded_file is None:
        st.error("Veuillez importer une photo pour continuer.")
    else:
        # Appeler la fonction recognize_face et afficher le résultat
        result = recognize_face(uploaded_file)
        if result is not None:
            st.success(result)
