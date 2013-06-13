import os

# os.environ["DJANGO_SETTINGS_MODULE"] = "djangoBlog.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoBlog.settings")

#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
