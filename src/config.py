import os
from dotenv import load_dotenv
from pathlib import Path
from faunadb.client import FaunaClient


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
    return os.getenv('API_SECRET')


client = FaunaClient(secret=getSecret())