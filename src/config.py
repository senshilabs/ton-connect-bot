from os import environ as env

from dotenv import load_dotenv
load_dotenv()

TOKEN = env['TOKEN']
MANIFEST_URL = env['MANIFEST_URL']
CONTRACT_ADDRESS = env['CONTRACT_ADDRESS']
