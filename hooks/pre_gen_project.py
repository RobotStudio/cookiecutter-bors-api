import re
import sys

import logging
logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger('pre_gen_project')

APP_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

app_name = '{{cookiecutter.app_name}}'

if not re.match(APP_REGEX, app_name):
    logger.error('Invalid value for app_name "{}"'.format(app_name))
    sys.exit(1)

ALLOWED_VERSIONS = ["1.11", "2.0", "2.1", "master"]

for bors_version in '{{cookiecutter.bors_versions}}'.split(","):
    if str(bors_version).strip() not in ALLOWED_VERSIONS:
        logger.error('Invalid Bors version "{}". '.format(bors_version))
        sys.exit(1)
