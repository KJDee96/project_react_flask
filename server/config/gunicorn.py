import os

bind = os.getenv('WEB_BIND', '0.0.0.0:8000')
reload = True if os.getenv('FLASK_ENV') == 'development' else False

access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(T)s "%(f)s" "%(a)s"'
accesslog = '-' if os.getenv('FLASK_ENV') == 'development' else 'logs/gunicorn.log'
errorlog = '-' if os.getenv('FLASK_ENV') == 'development' else 'logs/gunicorn.error.log'
loglevel = 'error'
capture_output = True
timeout = 300
