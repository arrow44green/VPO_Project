import torch
import cv2
from PIL import Image

#Chargement du modèle :
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained = True)

model.conf = 0.25
# for i in range(10):
#     capture = cv2.VideoCapture(i)
#     if capture.isOpened():
#         capture.release()
#     else :
#         print("Erreur")
capture = cv2.VideoCapture(0)
if not capture.isOpened():
    print("Erreur")
    exit()

# Entre dans une boucle infinie pour lire les images de la webcam en continu :
while True :
    ret, frame = capture.read()
    if not ret :
        print("Erreur :Impossible de lire la vidéo !")
        break

    # Convertir l'image capturée de l'espace de couleur BGR(OpenCV) à pillow à RGB :
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convertir l'image RGB en un objet Image de PIL pour le traitement avec YOLO :
    img_pil = Image.fromarray(frame_rgb)

    # Utiliser mon modèle pour détecter les objets dans les images et on va stocker le résultats :
    results = model(img_pil)

    # Récupérer la première image des résultats et on les convertient en uint8 donc 0 et 255 :
    frame_results = results.render()[0].astype('uint8')

    # Convertit l'image des résultats de RGB à BGR :
    frame_bgr = cv2.cvtColor(frame_results, cv2.COLOR_RGB2BGR)

    cv2.imshow('Yolov5 detecte webcam', frame_bgr)

    if cv2.waitKey(1) & 0xFF == ord('q') :
        break

capture.release()
cv2.destroyAllWindows()