from datetime import timedelta
from typing import Optional

from google.cloud.storage import Client

# 5mb
DEFAULT_MAX_CONTENT_SIZE = int(5e6)


def make_signed_upload_url(
        bucket: str,
        blob: str,
        *,
        exp: Optional[timedelta] = None,
        content_type="application/octet-stream",
        min_size=1,
        max_size=DEFAULT_MAX_CONTENT_SIZE
):
    """
    Compute a GCS signed upload URL without needing a private key file.
    """
    if exp is None:
        exp = timedelta(hours=1)

    client = Client.from_service_account_json('./fir-45c5d-0605d8168f14.json')
    bucket = client.get_bucket(bucket)
    blob = bucket.blob(blob)
    return blob.generate_signed_url(
        version='v4',
        expiration=exp,
        method='PUT',
        headers={
            'X-Goog-Content-Length-Range': f'{min_size},{max_size}',
            'Content-Type': content_type,
        }
    )
