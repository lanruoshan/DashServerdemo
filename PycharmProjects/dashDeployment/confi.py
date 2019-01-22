import os
import gevent.monkey
gevent.monkey.patch_all()
#tell our Gunicorn server how to interact with the application
import multiprocessing

debug = True
loglevel = 'debug'
bind = '0.0.0.0:8888' # different IP
pidfile = 'gunicorn.pid'
accesslog = 'log.out/gunicorn_access.log'
errorlog = 'log.out/gunicorn_error.log'
daemon = 'false'

#the number of processes
workers = 2
worker_class = 'gunicorn.workers.ggevent.GeventWorker'
worker_connections = 1024
x_forwarded_for_header = 'X-FORWARDED-FOR'

#gunicorn -w 1 -b 0.0.0.0:8888 app:server -D
# worker: -w
# address:-b
# remote address: h
# -c-config file
# -c /Users/apple/PycharmProjects/dashDeployment/confi.py /Users/apple/PycharmProjects/dashDeployment/app.py:server
#conmand
#python /Users/apple/PycharmProjects/dashDeployment/gunicorn.sh confi.py app:server -D
#python /Users/apple/PycharmProjects/dashDeployment/gunicorn.sh -w 1 -b 0.0.0.0:8888 app:server -D