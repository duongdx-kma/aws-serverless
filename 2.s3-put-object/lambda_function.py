import json
import boto3
from PIL import Image
import io

s3 = boto3.client('s3')

def create_thumbnail(image_data):
    with Image.open(io.BytesIO(image_data)) as image:
        image.thumbnail((128, 128))
        # Convert image to RGB if it has an alpha channel
        if image.mode in ('RGBA', 'LA'):
            background = Image.new('RGB', image.size, (255, 255, 255))
            background.paste(image, mask=image.split()[3]) # 3 is the alpha channel
            image = background
        buffer = io.BytesIO()
        image.save(buffer, 'JPEG')
        buffer.seek(0)
        return buffer

def lambda_handler(event, context):
    # Extract bucket name and object key from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    # Debug
    print('event for debug')
    print(event)
    print(bucket_name)
    print(object_key)
    print('end debug')

    # Ensure the object is in the /images directory
    if not object_key.startswith('images/'):
        return
    
    # Get the image from the source S3 bucket
    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    image_data = response['Body'].read()
    
    # Create a thumbnail of the image
    thumbnail_data = create_thumbnail(image_data)
    
    # Create the target key for the thumbnail
    thumbnail_key = object_key.replace('images/', 'thumbnails/')
    
    # Put the thumbnail back to the target S3 bucket
    s3.put_object(Bucket=bucket_name, Key=thumbnail_key, Body=thumbnail_data, ContentType='image/jpeg')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Thumbnail created successfully')
    }