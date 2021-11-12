from .base import *

# Import Productions Config
from .production import *

# Import Local if exists
try:
    from .local import *
except ModuleNotFoundError as mnf:
    print(mnf)
