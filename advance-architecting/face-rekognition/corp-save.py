from PIL import Image
from datetime import datetime

import boto3
import io
import json


photo='Group.jpg'
collectionId='beyoung-demo'
threshold=70
maxFaces=2
client=boto3.client('rekognition')

if __name__ == "__main__":

    #Get image width and height
    image = Image.open(open(photo,'rb'))
    width, height = image.size

    print ('Image information: ' + photo)
    print ('Image Height: ' + str(height)) 
    print('Image Width: ' + str(width))    

    # convert to image binary
    stream = io.BytesIO()
    if 'exif' in image.info:
        exif=image.info['exif']
        image.save(stream,format=image.format, exif=exif)
    else:
        image.save(stream, format=image.format)    
    image_binary = stream.getvalue()

    # Call detect faces api to get the bounding boxes
    response = client.detect_faces(Image={'Bytes': image_binary},Attributes=['DEFAULT'])
    print('Detected ' + photo + ' with ' + str(len(response['FaceDetails'])) + ' faces')

    for faceDetail in response['FaceDetails']:
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        print('BoundingBox')
        print(faceDetail['BoundingBox'])
        x, y = width * faceDetail['BoundingBox']['Left'], height * faceDetail['BoundingBox']['Top']
        right, bottom = x + width * faceDetail['BoundingBox']['Width'], y + height * faceDetail['BoundingBox']['Height']
        print('corping image: left, top, right bottm')
        print(x, y, right, bottom)
        
        cropped = image.crop( (x, y, right, bottom) )
        cropped.save('./' + time + '.jpg', format=image.format)
        stream2 = io.BytesIO()
        cropped.save(stream2, format=image.format)
        image_binary2 = stream2.getvalue()
        
        response = client.search_faces_by_image(CollectionId=collectionId,
                                Image={'Bytes': image_binary2},
                                FaceMatchThreshold=threshold,
                                MaxFaces=maxFaces)
        
        if len(response['FaceMatches']) > 0:
            faceMatches=response['FaceMatches']
            print ('Matching faces')
            for match in faceMatches:
                    print ('FaceId:' + match['Face']['FaceId'])
                    print ('ExternalImageId:' + match['Face']['ExternalImageId'])
                    print ('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
                    print
