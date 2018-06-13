from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework import views
from .facerecognition import FaceRecognition
from rest_framework.parsers import MultiPartParser
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.clickjacking import xframe_options_exempt





class EncodeImage(views.APIView):
    """
    This post url encodes Face in an Image.\n
    it accepts two parameters (multipart/form data)\n
    file (image) and name (text)
    """
    parser_classes = (MultiPartParser,)

    @xframe_options_exempt
    def post(self, request):
        try:
            input_dict = dict()
            input_dict['name'] = request.data['name']
            input_dict['file'] = request.data['file']
            fr = FaceRecognition()
            fr.encodeFace(input_dict);
            return Response({'errorCode': '0', 'errorMessage': 'Success'})
        except MultiValueDictKeyError:
            return Response({'errorCode': '400', 'errorMessage': 'Bad Request '})
        except:
            return Response({'errorCode': '500', 'errorMessage': 'Internal Server Error'})



class RecognizeImage(views.APIView):
    """
    This post url recognizes Face in an Image.\n
    it accepts two parameters (multipart/form data)\n
    file (image)

    """
    parser_classes = (MultiPartParser,)

    @xframe_options_exempt
    def post(self, request):
        try:
            file_obj = request.data['file']
            print(request.data)
            fr = FaceRecognition()
            faces = fr.recognizeFaces(file_obj)
            return Response(faces)
        except MultiValueDictKeyError:
            return Response({'errorCode': '400', 'errorMessage': 'Bad Request '})
        except Exception as e:
            return Response({'errorCode': '500', 'errorMessage': 'Internal Server Error'})















