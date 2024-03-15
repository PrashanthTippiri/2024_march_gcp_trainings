import os

from google.cloud import storage

client = storage.Client()

bucket = client.bucket("testgcpmarch-trainings01")

source_file_name = "C:/test/f1.txt"

destination_blob_name = "data/input/f1_local.txt"

blob = bucket.blob(destination_blob_name)

    # Optional: set a generation-match precondition to avoid potential race conditions
    # and data corruptions. The request to upload is aborted if the object's
    # generation number does not match your precondition. For a destination
    # object that does not yet exist, set the if_generation_match precondition to 0.
    # If the destination object already exists in your bucket, set instead a
    # generation-match precondition using its generation number.
#generation_match_precondition = 0

print(blob.upload_from_filename(source_file_name))

#print(
#    f"File {source_file_name} uploaded to {destination_blob_name}."
#)


