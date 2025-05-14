from django.shortcuts import render
from .forms import ImageUploadForm
from .models import UploadedImage
import random

# Placeholder prediction function (no real AI model needed)
def predict_disease(img_path):
    class_names = ['Blight', 'Rust', 'Healthy']
    advice_list = [
        'Use fungicide X and remove infected leaves.',
        'Apply treatment Y in early morning.',
        'No disease detected, your plant looks healthy.'
    ]

    i = random.randint(0, 2)
    return class_names[i], advice_list[i]

# Main view for upload and prediction
def upload_image(request):
    prediction_result = None
    advice = None

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded = form.save()
            disease, advice = predict_disease(uploaded.image.path)
            prediction_result = f'Predicted Disease: {disease}'
    else:
        form = ImageUploadForm()

    return render(request, 'disease_detection/upload.html', {
        'form': form,
        'prediction_result': prediction_result,
        'advice': advice
    })
