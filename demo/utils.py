from requests.auth import _basic_auth_str as basic_auth_str
import base64
import coloredlogs
import logging
import json

# setup logger
formatter = "%(asctime)s %(name)s %(levelname)s\t%(message)s"
coloredlogs.install(fmt=formatter, level='DEBUG')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Disable some warnings about self signed certs
import urllib3
urllib3.disable_warnings()