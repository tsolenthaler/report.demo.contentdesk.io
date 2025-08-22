from os import getenv
from dotenv import load_dotenv, find_dotenv
from contentdeskreport.check.checkUrlExist import CheckUrlExist
import os

load_dotenv(find_dotenv())

## Load from Job Environment Variables
AKENEO_HOST = getenv('AKENEO_HOST')
AKENEO_CLIENT_ID = getenv('AKENEO_CLIENT_ID')
AKENEO_CLIENT_SECRET = getenv('AKENEO_CLIENT_SECRET')
AKENEO_USERNAME = getenv('AKENEO_USERNAME')
AKENEO_PASSWORD = getenv('AKENEO_PASSWORD')
CDN_URL = getenv('CDN_URL')

APP_ORGANIZATION = getenv('APP_ORGANIZATION')
APP_NAME = getenv('APP_NAME')
APP_WEBSITE= getenv('APP_WEBSITE')
APP_WEBSITE_API = getenv('APP_WEBSITE_API')
APP_ORGANIZATION_WEBSITE = getenv('APP_ORGANIZATION_WEBSITE')
APP_EMAIL = getenv('APP_EMAIL')
APP_REGION = getenv('APP_REGION')

def main():
    path = "docs"
    projectPath = os.path.abspath(os.sep)

    CheckUrlExist(projectPath+path)

if __name__ == '__main__':
    main()