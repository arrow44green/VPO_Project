document.getElementById('analyze-button').addEventListener('click', function() {
    const input = document.getElementById('image-upload');
    const formData = new FormData();
    formData.append('file', input.files[0]);

    // Afficher l'image téléversée
    const reader = new FileReader();
    reader.onload = function(e) {
        const imgPreview = document.getElementById('image-preview');
        imgPreview.src = e.target.result;
        imgPreview.style.display = 'block';
    }
    reader.readAsDataURL(input.files[0]);

    fetch('/analyze', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        let resultText = 'Résultats de l\'analyse :<br>';
        data.result.forEach(item => {
            resultText += `Objet détecté: ${item.name} (Confiance: ${item.confidence.toFixed(2)})<br>`;
        });
        document.getElementById('result').innerHTML = resultText;
    })
    .catch(error => {
        console.error('Erreur:', error);
        document.getElementById('result').textContent = 'Erreur lors de l\'analyse de l\'image.';
    });
});