SETUP: 
1. Install requirements.txt with "pip install -r requirements.txt"
3. In your Django project's settings.py:
	a. Add "django_user_agents" to the INSTALLED_APPS list. 
	b. Add "django_user_agents.middleware.UserAgendMiddleware" to the MIDDLEWARE or MIDDLEWARE_CLASSES list. 
2. Import the __init__.py into your Django project

USAGE: 
1. In your view, use the syntax "UserAgent(request)" to use the UserAgent class from the __init__.py file in this repository. 
	This will return a UserAgent object which has information about the browser, ip, device, touch capabilities, and os. 