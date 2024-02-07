from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# views.py

import os
import cv2
from django.conf import settings
from django.http import HttpResponse
import tempfile

@csrf_exempt
def upload_video(request):
    if request.method == 'POST' and request.FILES.get('file'):
        video_file = request.FILES['file']

        # Save the uploaded video file
        video_path = os.path.join(settings.MEDIA_ROOT, 'videos', video_file.name)
        with open(video_path, 'wb') as f:
            for chunk in video_file.chunks():
                f.write(chunk)

        # Convert video to images
        output_folder = tempfile.mkdtemp()
        convert_video_to_images(video_path, output_folder)

        # Return one of the images as a response
        image_file = os.path.join(output_folder, os.listdir(output_folder)[0])
        with open(image_file, 'rb') as f:
            response = HttpResponse(f.read(), content_type='image/jpeg')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(image_file)
            return response
    else:
        return HttpResponse('No file uploaded', status=400)

def convert_video_to_images(video_path, output_folder, frame_interval=1):
    video_capture = cv2.VideoCapture(video_path)
    success, image = video_capture.read()
    count = 0
    while success:
        if count % frame_interval == 0:
            image_path = os.path.join(output_folder, f"frame_{count}.jpg")
            cv2.imwrite(image_path, image)
        success, image = video_capture.read()
        count += 1
    video_capture.release()
