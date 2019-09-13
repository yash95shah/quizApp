import os
project_id = os.getenv('PROJ')
bucket_name = os.getenv("BUCK")

from google.cloud import storage

storage_client = storage.Client(project_id)
bucket = storage_client.get_bucket(bucket_name)

def upload_file(image_file, public):
    blob = bucket.blob(image_file.filename)
    blob.upload_from_string(
        data= image_file.read(),
        content_type = image_file.content_type
    )
