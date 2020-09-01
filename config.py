import os
from dotenv import load_dotenv
from pathlib import Path


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
