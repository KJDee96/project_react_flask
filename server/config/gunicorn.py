import os

bind = os.getenv('WEB_BIND', '0.0.0.0:8000')
reload = True if os.getenv('FLASK_ENV') == 'development' else False

accesslog = '-' if os.getenv('FLASK_ENV') == 'development' else 'logs/gunicorn.log'
errorlog = '-' if os.getenv('FLASK_ENV') == 'development' else 'logs/gunicorn.error.log'
loglevel = 'error'
capture_output = True
