from visa.logger import logging
from visa.exception import USvisaException
import sys

try:
    print(3/0)
except Exception as e:
    raise USvisaException(e, sys)