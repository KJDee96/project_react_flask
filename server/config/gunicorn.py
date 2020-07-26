import os
from distutils.util import strtobool


bind = os.getenv('WEB_BIND', '0.0.0.0:8000')
reload = bool(strtobool(os.getenv('WEB_RELOAD', 'false')))
