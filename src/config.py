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
    name = google_client.secret_version_path("testfaunaserverless", "API_SECRET", "latest")
    response = client.access_secret_version(name)
    return response.payload.data.decode('UTF-8')


# if __name__ == '__main__':
#     getGCPSecret()


# client = FaunaClient(secret=getSecret())
client = FaunaClient(secret=getGCPSecret())
