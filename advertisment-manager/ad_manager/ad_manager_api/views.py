from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .serializers import ad_Serializer
from django.core.files.storage import default_storage
from .models import ad
import pika
from config import *



class ad_api_view(APIView):
  parser_classes = [MultiPartParser]

  # user send request (want to submit ad)
  def post(self, request, *args, **kwargs):
    data = {
      'description': request.data.get('description'),
      'email': request.data.get('email')
    }
    serializer = ad_Serializer(data=data)
    if serializer.is_valid():
      # adds to database
      serializer.save()
      pic_id = serializer.data['id']
      image = request.FILES.get('image', '')
      # save image on s3
      file_path_within_bucket = str(pic_id) + '.png'
      default_storage.save(file_path_within_bucket, image)
      # send to  rabbitMQ
      connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
      channel = connection.channel()
      channel.queue_declare(queue='ad_requests')
      channel.basic_publish(exchange='', routing_key='ad_requests', body=str(pic_id))
      connection.close()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  # user get request (want to see ad result)
  def get(self, request, *args, **kwargs):
    ad_id = ad.objects.get(id=request.data.get('id'))
    ad_serializer = ad_Serializer(ad_id)
    print(ad_serializer.data)
    if ad_serializer.data.get('state') == 'in progress':
      return Response({"IN PROGRESS": "Your ad in still in progress"}, status=status.HTTP_200_OK)
    elif ad_serializer.data.get('state') == 'ad rejected':
      return Response({"REJECTED ": "Your ad is REJECTED"}, status=status.HTTP_200_OK)
    else:
      ad_id = str(ad_serializer.data.get('id'))
      ad_desc = ad_serializer.data.get('description')
      ad_category = ad_serializer.data.get('category')
      ad_image_address = 'https://ad-image-collector.s3.us-east-2.amazonaws.com/' + str(ad_serializer.data.get('id')) + '.png'
      return_string = f'Your ad with ID : {ad_id} is ACCEPTED, \n with DESCRIPTION : {ad_desc},' \
                      f' \n with CATEGORY : {ad_category}, \n with IMAGE : {ad_image_address} '
      return Response({"SUCCESS ": return_string}, status=status.HTTP_200_OK)
