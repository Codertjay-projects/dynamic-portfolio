from decouple import config

print(config('DEBUG'))
if config('DEBUG') == 'True':
    from .local import *
else:
    from .production import *
