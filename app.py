from flask import Flask, render_template, request, jsonify
import torch
import cv2
from PIL import Image
import io

# Chargement du modèle YOLOv5
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
model.conf = 0.25  # Confiance minimale

app = Flask(__name__)

def analyze_image(image_bytes):
    # Convertir les bytes de l'image en objet PIL
    img_pil = Image.open(io.BytesIO(image_bytes))

    # Utiliser le modèle pour détecter les objets dans l'image
    results = model(img_pil)

    # Extraire les informations des résultats (par exemple, les labels et les positions)
    labels = results.pandas().xyxy[0].to_dict(orient="records")
    
    return labels

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    image_bytes = file.read()
    result = analyze_image(image_bytes)

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)