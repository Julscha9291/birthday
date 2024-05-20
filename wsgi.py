import os
import django
from django.core.wsgi import get_wsgi_application
import sys

sys.path.append('/home/pi/birthday') 


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'birthday.settings')

application = get_wsgi_application()

