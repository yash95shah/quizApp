import os
project_id = os.getenv('PROJ')
bucket_name = "testy-bucks"

from google.cloud import storage
storage_client = storage.Client(project_id)
bucket = storage_client.get_bucket(bucket_name)

# def download_blob(source_blob_name, destination_file_name):
#     """Downloads a blob from the bucket."""
#     blob = bucket.blob(source_blob_name)

#     blob.download_to_filename(destination_file_name)

#     print('Blob {} downloaded to {}.'.format(
#         source_blob_name,
#         destination_file_name))

def list_blobs(bucket_name="testy-bucks"):
    """Lists all the blobs in the bucket."""
    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)
    for blob in blobs:
        print(blob.name)


# def upload_file(image_file, public):
#     blob = bucket.blob(image_file.filename)
#     blob.upload_from_string(
#         data= image_file.read(),
#         content_type = image_file.content_type
#     )

list_blobs()
