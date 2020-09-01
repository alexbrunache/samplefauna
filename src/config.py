import os
from dotenv import load_dotenv
from pathlib import Path
from faunadb.client import FaunaClient
from google.cloud import secretmanager


def getSecret():
    # Get the base directory
    basepath = Path()
    basedir = str(basepath.cwd())

    # Load the environment variables
    envars = basepath.cwd() / '.env'
    load_dotenv(envars)
    print(envars)
    # Read an environment variable.
    secret = os.getenv('API_SECRET')
    print(secret)
    return secret


def getGCPSecret():
    google_client = secretmanager.SecretManagerServiceClient()
    secret_name = "API_SECRET"
    project_id = os.getencv("testfaunaserverless")
    resource_name = f"projects/{project_id}/secrets/{secret_name}/versions/latest"
    response = google_client.access_secret_version(resource_name)
    return response.payload.data.decode('UTF-8')


# client = FaunaClient(secret=getSecret())
client = FaunaClient(secret=getGCPSecret())