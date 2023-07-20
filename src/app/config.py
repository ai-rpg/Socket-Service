from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

BUILD_VERSION = environ.get("BUILD_VERSION")
METRICS_PATH = environ.get("METRICS_PATH")
NAME = environ.get("NAME")
OPENAPIKEY = environ.get("OPENAPIKEY")
HTTPPORT = environ.get("HTTPPORT")
HOST = environ.get("HOST")
LOKIURL = environ.get("LOKIURL")
AISERVICEURL = environ.get("AISERVICEURL")
REDIS_HOST = environ.get("REDIS_HOST")
REDIS_PORT = environ.get("REDIS_PORT")
REDIS_PASSWORD = environ.get("REDIS_PASSWORD")
ADVENTURESERVICEURL = environ.get("ADVENTURESERVICEURL")
